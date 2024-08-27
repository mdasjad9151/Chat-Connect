from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password =  serializers.CharField(write_only = True)

    def create(self, validated_data):
        User = get_user_model().objects.create_user(
            email = validated_data['email'],
            password  = validated_data['password'],
            first_name = validated_data.get('first_name',""),
            second_name = validated_data.get('second_name',"")
        )
        return User
    class Meta:
        model = get_user_model()
        fields = ['email','password','first_name', 'second_name']
        extra_kwargs = {'password', {'write_only': True}}