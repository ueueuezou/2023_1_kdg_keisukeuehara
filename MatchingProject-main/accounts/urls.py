from django.urls import path
from django.conf import settings
from . import views

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.SignUpView.as_view(), name='signup'),
  path('edit/', views.CustomUserEdit, name='edit'),
  path('detail/<int:id>', views.CustomUserDetail, name='detail'),
]

