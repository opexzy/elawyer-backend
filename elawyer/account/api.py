from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Account
from .serializers import AccountSerializer

class AccountViewSet(ModelViewSet):
    """
    Model Viewset that provides standard actions for:
    retrive, create, list, update, destroy and partial_update and
    also custom actions to set account password
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    #def create(self, request):
    """
        Use this endpoint to create a new account.
        This endpoint will first create a auth user and then a new account

        Sample Data
        -----------
        {   
            "email": "string",
            "first_name": "string",
            "last_name": "string",
            "password": "password",
            "retype_password": "password",
            "gender": "string",
            "phone_number": "string",
            "birth_date": "string",
            "country": "string",
            "state": "string",
            "city": "string",
            "address": "string",
            "service_interest": [
                "string"
            ],
            "occupation": "string",
            "level_of_education": "string",
            "heard_about_us": "string",
            "email_verified": true,
            "user": 0
        }
    """
    #pass