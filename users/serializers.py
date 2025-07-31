from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'nickname')

    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data.get('email'),
            nickname = validated_data.get('nickname')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user