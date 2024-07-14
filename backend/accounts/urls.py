# accounts/urls.py
from django.urls import path
from .views import UserProfileView, ChangePasswordView, UpdateUserPointsView, LogoutAndSavePointsView, UserPointsView

urlpatterns = [
    path('update_points/', UpdateUserPointsView.as_view(), name='update_points'),
    path('logout_and_save_points/', LogoutAndSavePointsView.as_view(), name='logout_and_save_points'),
    path('user_points/', UserPointsView.as_view(), name='user_points'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]

