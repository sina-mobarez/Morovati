
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.models import Alarm, CoinScout, Conditions, Filter, Permium, CustomUser, Rank, StockScout
from django.contrib.auth.password_validation import validate_password

 



class PermiumAccount(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Permium
        fields = '__all__'
        depth = 2




class UserModelSerializer(serializers.ModelSerializer):

    
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = CustomUser
        fields = ['email', 'phone','username', 'password', 'mac_address', 'last_name']
        
    
    def create(self, validated_data):
        user = CustomUser.objects.create(
            phone=validated_data['phone'],
            email=validated_data['email'],
            username=validated_data['username']
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
        
        
        
        
class AlarmSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Alarm
        fields = '__all__'
        
        
        
class StockScoutSeriallizer(serializers.ModelSerializer):
    
    class Meta:
        model = StockScout
        fields = '__all__'
        
        

class CoinScoutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoinScout
        fields = '__all__'