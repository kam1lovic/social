from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
]
