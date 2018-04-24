from django.shortcuts import render
from django.middleware.csrf import get_token
from rest_framework.response import Response
from rest_framework.views import APIView


class CSRFGeneratorView(APIView):
    def get(self, request):
        csrf_token = get_token(request)
        return Response(csrf_token)