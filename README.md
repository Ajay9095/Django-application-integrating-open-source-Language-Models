# Django-application-integrating-open-source-Language-Models
---
This project is a web application that allows users to perform text generation and text summarization using various models. It provides a user-friendly interface for inputting text, receiving model-generated responses, and viewing historical interactions.

## Features

- **Text Generation:**
  - Choose between different models (e.g., Meta-Llama-3, falcon-7).
  - Input text and receive model-generated responses.
  - View and clear chat history.

- **Text Summarization:**
  - Input text for summarization.
  - Receive summarized output.
  - View and clear summarization history.

- **History Panels:**
  - View detailed history for both text generation and summarization.
  - Close panels to focus on main application.

## Technologies Used

- **Frontend:**
  - HTML, CSS (Bootstrap)
  - JavaScript (jQuery)

- **Backend/API:**
  - Django (Python)
  - RESTful API for handling model interactions
  - **Imports:**
    ```python
    from django.shortcuts import render
    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    import requests
    from django.conf import settings
    from .models import ChatHistory
    ```

- **Database:**
  - mongodb (default Django configuration)

## Getting Started

To run the project locally, follow these steps:

1. **Create and activate a virtual environment:**
   ```
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

2. **Run migrations:**
   ```
   python manage.py migrate
   ```

3. **Start the Django development server:**
   ```
   python manage.py runserver
   ```

4. **Access the application:**
   Open a web browser and go to `http://localhost:8000` to view the application.

## Django Administrative Commands

- **Create a new Django app:**
  ```
  python manage.py startapp <app-name>
  ```

- **Create a new Django superuser:**
  ```
  python manage.py createsuperuser
  ```

- **Run Django development server:**
  ```
  python manage.py runserver
  ```

- **Perform database migrations:**
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

## Usage

1. **Text Generation:**
   - Select a model from the dropdown list.
   - Enter text in the input field.
   - Click "Send" to see the model's response.
   - Use "Clear" to clear the input and history.

2. **Text Summarization:**
   - Enter text in the summarization textarea.
   - Click "Proceed" to receive a summarized output.
   - Summarization history is shown in the panel.

3. **History Panels:**
   - Click "View Text Generation History" or "View Text Summarization History" to open respective panels.
   - Close panels by clicking "Close" or outside the panel area.

## Folder Structure

- **/static/**: Contains static files (CSS, JavaScript, images).
- **/templates/**: HTML templates.
- **manage.py**: Django project management script.
- **requirements.txt**: Python dependencies.

## Additional Notes

- Ensure proper internet connectivity for model interactions.
- Adjust configurations (`settings.py`) for production deployment.
- Customize frontend styling and functionality as needed.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the [MIT License](LICENSE).

---
