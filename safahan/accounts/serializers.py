from dataclasses import field
from multiprocessing import Condition
from rest_framework import serializers

from accounts.models import Conditions, Filter, Permium, CustomUser, Rank
from django.contrib.auth.password_validation import validate_password

 



class PermiumAccount(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Permium
        fields = '__all__'
        depth = 2




class UserModelSerializer(serializers.ModelSerializer):



    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = CustomUser
        fields = ['phone','last_name', 'mac_address']
        
    
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
        
        
        

class FilterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Filter
        fields = '__all__'
        
        
        
class ConditionsSerializer(serializers.ModelSerializer):
    filter = FilterSerializer
    class Meta:
        model = Conditions
        fields = ['type', 'value', 'filter']
        depth = 2
        
        
        
class RankSerializer(serializers.ModelSerializer):
    filter = FilterSerializer
    
    
    class Meta:
        model = Rank
        fields = ['rate', 'user', 'filter']
        depth = 2 





class VerifyPhoneNumberSerializer(serializers.ModelSerializer):
    otp_code = serializers.CharField(required=True, max_length=6)
    
    class Meta:
        model = CustomUser
        fields = ['phone', 'otp_code']
        
        
        
        
class GetCodeVerifyPhoneNumberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['phone',]