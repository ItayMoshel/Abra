from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from messagesApp.models import Message, User
from messagesApp.serializers import MessageSerializer, UserSerializer
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser
)
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_403_FORBIDDEN
)
from django.contrib.auth.models import User


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if user is not None:
        try:
            token = Token.objects.get(user_id=user.id)
        except Token.DoesNotExists:
            token = Token.objects.create(user=user)
        return Response(token.key)
    else:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def register_user(request):
    user = User.objects.create_user(
        username=request.data.get("username"),
        password=request.data.get("password"))
    user.save()

    if user is not None:
        token = Token.objects.create(user=user)
        print(token.key)
        print(user)
        return Response(token.key)
    else:
        return Response([], status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_message(request):
    message = MessageSerializer(data=request.data)
    if message.is_valid():
        message.save()
        return JsonResponse(message.data)
    return JsonResponse(message.errors)


@permission_classes([IsAdminUser])
@api_view(['GET'])
def view_messages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def user_unread_messages(request):
    user = request.user
    messages = Message.objects.filter(receiver=user, is_read=False)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def user_sent_messages(request):
    user = request.user
    messages = Message.objects.filter(sender=user)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def user_messages(request):
    user = request.user
    messages = Message.objects.filter(receiver=user)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


# @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def user_to_user_messages(request, receiver):
#     user = request.user
#     receiver = User.objects.filter(username=receiver)
#     messages = Message.objects.filter(sender=user, receiver=receiver)
#     serializer = MessageSerializer(messages, many=True)
#     return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def view_users(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return JsonResponse({'message': 'User deleted.'}, status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def read_message(request, message_id):
    message = Message.objects.get(id=message_id)
    message.is_read = True
    message.save()
    serializer = MessageSerializer(message, many=False)
    return Response(serializer.data)


@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)
    message.delete()
    return JsonResponse({'message': 'Message deleted.'}, status=status.HTTP_204_NO_CONTENT)
