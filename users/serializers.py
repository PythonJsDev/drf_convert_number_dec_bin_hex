from rest_framework import serializers
from converts.serializers import ConvertSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'is_staff', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}
    

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user


