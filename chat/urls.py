from django.contrib import admin
from django.urls import path
from chat.views import chat_with_model, summarize_text, get_chat_history  

urlpatterns = [
    path('chat/', chat_with_model, name='chat_with_model'),  
    path('summarize_text/', summarize_text, name='summarize_text'),  
    path('chat/history/<str:user_id>/', get_chat_history, name='get_chat_history'),  
]


