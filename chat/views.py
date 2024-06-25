from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings
from .models import ChatHistory

API_URL1 = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
API_URL2 = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
SUMMARIZATION_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

@api_view(['POST'])
def chat_with_model(request):
    model_name = request.data.get('model_name')
    user_input = request.data.get('user_input')
    user_id = request.data.get('user_id')

    if model_name == 'Meta-Llama-3':
        api_url = API_URL1
    elif model_name == 'falcon-7':
        api_url = API_URL2
    else:
        return Response({'error': 'Invalid model name'}, status=400)

    try:
        headers = {"Authorization": f"Bearer {settings.HUGGINGFACE_API_TOKEN}"}
        response = requests.post(api_url, headers=headers, json={"inputs": user_input})
        response.raise_for_status()
        generated_text = response.json()[0]["generated_text"]

        chat_history = ChatHistory(
            user_id=user_id,
            model_name=model_name,
            user_input=user_input,
            model_response=generated_text
        )
        chat_history.save()

        return Response({'response': generated_text})
    except requests.exceptions.RequestException as e:
        return Response({'error': str(e)}, status=503)

@api_view(['POST'])
def summarize_text(request):
    user_input = request.data.get('user_input')

    try:
        headers = {"Authorization": f"Bearer {settings.HUGGINGFACE_API_TOKEN}"}
        payload = {"inputs": user_input}

        response = requests.post(SUMMARIZATION_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        summarized_text = response.json()[0]["summary_text"]

        chat_history = ChatHistory(
            user_id=request.data.get('user_id'),  
            model_name='Summarization Model',
            user_input=user_input,
            model_response=summarized_text
        )
        chat_history.save()

        return Response({'summary': summarized_text})
    
    except requests.exceptions.RequestException as e:
        return Response({'error': str(e)}, status=503)

@api_view(['GET'])
def get_chat_history(request, user_id):
    history = ChatHistory.objects.filter(user_id=user_id, model_name__in=['Meta-Llama-3', 'falcon-7']).order_by('-timestamp')
    data = [{'user_input': h.user_input, 'model_response': h.model_response, 'timestamp': h.timestamp} for h in history]
    return Response(data)

@api_view(['GET'])
def get_summarization_history(request, user_id):
    history = ChatHistory.objects.filter(user_id=user_id, model_name='Summarization Model').order_by('-timestamp')
    data = [{'user_input': h.user_input, 'model_response': h.model_response, 'timestamp': h.timestamp} for h in history]
    return Response(data)

def chat_view(request):
    return render(request, 'chat.html')
