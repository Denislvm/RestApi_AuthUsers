from rest_framework import serializers
from authapp.models import AuthUsers


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUsers
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUsers
        fields = '__all__'

