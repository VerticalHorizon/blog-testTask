from rest_framework import serializers
from django.contrib.auth import get_user_model  # In case we will want to change default User model to custom


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data: dict) -> UserModel:

        user = UserModel.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user

    class Meta:
        model = UserModel
        fields = ("id", "email", "username", "password",)
