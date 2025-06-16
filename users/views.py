from datetime import timezone
from django.shortcuts import render
from .serializers import CuentaSerializer
from .models import Cuenta
from django.contrib.auth import login as dj_login

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth


@api_view(['POST'])
def signup(request):
    serializer = CuentaSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data.get('name')
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
     
        new_user = Cuenta.objects.create_user(
            name=name,
            email=email,
            password=password,
        )

        new_user.save()
        return Response(
        {
            "success": True,
            "message": "Tu cuenta ha sido creada exitosamente",
        },
        status=status.HTTP_201_CREATED)   
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login (request):
    email = request.data.get('email')
    password = request.data.get('password')     
    user = auth.authenticate(email=email, password=password)    
    if user is not None:
        dj_login(request._request, user) # Actualiza el inicio de sesión=last_login
        token = RefreshToken.for_user(user)
        return Response(
            {
                "success": True,
                "message": f"Bienvenido {user.name}",
                "token": str(token.access_token),
            },
            status=status.HTTP_200_OK,
        )
    else:            
        return Response(
            {"error": True, "message": "Las credenciales son incorrectas"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

# @permission_classes([IsAuthenticated])
@api_view(['POST'])
def logout(request):
    try:
        refresh_token = request.data.get("refresh_token")
        token = RefreshToken(refresh_token)
        token.blacklist() 
        return Response({"success": True, "message": "Sesión cerrada correctamente"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"error": True, "message": "Token inválido o ya caducado"}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def listUsers(request):
    users = Cuenta.objects.all()
    serializer = CuentaSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
