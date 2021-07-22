from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, max_length=50)
    new_password = serializers.CharField(required=True, max_length=50)
    confirm_password = serializers.CharField(required=True, max_length=50)

    def validate(self, data):
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')
        errors = {}

        if not self.context['request'].user.check_password(old_password):
            errors['old_password'] = ['Old password is wrong.']
        # check password length and match
        if data.get("password") != data.get("retype_password"):
            errors["password"] = "Password mismatch"
        if len(data.get("password")) < 8:
            errors["password"] = "Password must be 8 characters or more"

        if errors:
            raise serializers.ValidationError(errors)

        return data