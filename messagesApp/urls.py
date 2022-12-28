from django.urls import path
from . import views


urlpatterns = [
    # "Login/ Register panel"
    path('api/create_user/', views.register_user),
    path('api/login/', views.login),
    
    # "User functions"
    path('api/get_user/', views.get_user), # To see user details
    path('api/create_message/', views.create_message), # To create message
    path('api/read_message/<str:message_id>/', views.read_message), # To read message
    path('api/user_inbox/', views.user_inbox), # To see all messages received
    path('api/user_sent_messages/', views.user_sent_messages), # To see all messages sent
    path('api/user_unread_messages/', views.user_unread_messages), # To see all unrread messages
    path('api/delete_message/<str:message_id>/', views.delete_message), # To delete a message as owner/ receiver
    

    # "Admin panel"
    path('api/delete_user/<str:user_id>/', views.delete_user), # To delete a user
    path('api/view_users/', views.view_users), # To see all users in db
    path('api/view_messages/', views.view_messages), # To view all messages in db
]
