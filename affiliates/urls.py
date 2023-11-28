from django.urls import path
from .views import user_profile_list_create_view, user_profile_detail_view

urlpatterns = [
    path('profiles/', user_profile_list_create_view, name='user_profile_list_create'),
    path('profiles/<int:pk>/', user_profile_detail_view, name='user_profile_detail'),
]