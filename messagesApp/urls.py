from django.urls import path
from . import views


urlpatterns = [
    path('api/login/', views.login),
    path('api/create_message/', views.create_message),
    path('api/create_user/', views.register_user),
    path('api/get_user/', views.get_user),
    path('api/view_users/', views.view_users),
    path('api/view_messages/', views.view_messages),
    path('api/read_message/<str:message_id>/', views.read_message),
    path('api/user_inbox/', views.user_inbox),
    path('api/user_sent_messages/', views.user_sent_messages),
    # path('api/user_to_user_messages/<str:receiver>/', views.user_to_user_messages),
    path('api/user_unread_messages/', views.user_unread_messages),
    path('api/delete_message/<str:message_id>/', views.delete_message),
    path('api/delete_user/<str:user_id>/', views.delete_user),

]
