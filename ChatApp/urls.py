from django.contrib import admin
from django.urls import include, path
from chat.views import chat_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chat_view, name='chat_view'),
    path('api/', include('chat.urls')),
]
