from django.urls import path
from .views import ChatView

urlpatterns = [
  path("text/", ChatView.as_view(), name='getResponseChatgpt')
]