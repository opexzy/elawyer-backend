from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    retype_password = serializers.CharField(required=True)

    class Meta:
        model = Account
        fields = ["id","email","first_name","last_name","password", "retype_password","gender",
            "phone_number","birth_date","age","country", "state", "city", "address", "service_interest", 
            "occupation", "level_of_education","heard_about_us","email_verified", "date_joined"
        ]
        write_only_fields = ["password", "retype_password"]
    
    def create(self, validated_data):
        #create user object
        user = User.objects.create(email=validated_data.pop(email), password=validated_data.pop(password))
        #create account
        account = Account.objects.create(user=user, **validated_data)
        return account

    def update(self, instance, validated_data):
        #update user object
        instance.user.first_name = validated_data.get("first_name", instance.user.first_name)
        instance.user.last_name = validated_data.get("last_name", instance.user.last_name)
        instance.user.save()
        validated_data.pop("email")
        validated_data.pop("first_name")
        validated_data.pop("last_name")
        #update account
        super().update(self, instance, validated_data)

    def validate(self, data):
        """
            Validate account data
        """
        errors = dict({})
        # check if email already exists
        try:
            User.objects.get(email=data.get("email"))
            errors["email"] = "Email already exist"
        except User.DoesNotExist:
            pass

        # check password length and match
        if data.get("password") != data.get("retype_password"):
            errors["password"] = "Password mismatch"
        if len(data.get("password")) < 8:
            errors["password"] = "Password must be 8 characters or more"

        if errors:
            raise serializers.ValidationError(errors)
        
        return data
