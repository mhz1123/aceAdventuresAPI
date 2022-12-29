from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.userRegistration),
    path('login/', views.userlogin),
    path('profile/', views.userprofile),
    path('changepassword/', views.change_password),
    path('send-reset-password/', views.sendPassResetEmail),
    path('password-reset/<uid>/<token>/', views.PasswordReset),
]