from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

def get_login_status(request):
    if request.user.is_authenticated:
        data = {
            'is_authenticated': True,
            'username': request.user.username,
            'email': request.user.email,
        }
    else:
        data = {
            'is_authenticated': False,
        }
    return JsonResponse(data)

class LoginStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            'is_authenticated': True,
            'username': user.username,
            'email': user.email,
        }
        return Response(data)