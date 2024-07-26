from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'username', 'photo', 'email', 'role', 'password', 'confirm_password']
        extra_kwargs = {
            'role': {'required': False},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        print(validated_data)
        validated_data.pop('confirm_password', None)
        user = User.objects.create(
            full_name=validated_data.get('full_name'),
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            role=validated_data.get('role', 'user'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({
            'user': {
                'full_name': self.user.full_name,
                'username': self.user.username,
                'email': self.user.email,
                'role': self.user.role,
            }
        })
        
        return data

