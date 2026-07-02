from django.urls import path
from .views import UserAPIView

urlpatterns = [
    # The healthy organism pattern: Nouns for resources
    path('users/', UserAPIView.as_view(), name='user-api'),
]