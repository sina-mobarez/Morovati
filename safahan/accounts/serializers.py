from rest_framework import serializers

from accounts.models import Permium, CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

 



class PermiumAccount(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Permium
        fields = '__all__'
        depth = 2




class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['phone',]

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = CustomUser
        fields = ['phone', 'password']
        
    
    def create(self, validated_data):
        user = CustomUser.objects.create(
            phone=validated_data['phone'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

       
       
        
class UserModelLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['phone', 'password']
        
