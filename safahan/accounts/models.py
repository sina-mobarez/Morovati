from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.core.validators import RegexValidator



import pyotp


class UserManager(BaseUserManager):
   
    def create_user(self,phone, password, **extra_fields):
        """
        Create and save a User with the given email, phone number and password.
        """
        if not phone:
            raise ValueError('The Phone must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        """
        Create and save a SuperUser with the given email, phone number and password.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone, password, **extra_fields)






class CustomUser(AbstractUser):
    phone_regex = RegexValidator( regex = '^9\d{9}$', message ="Phone number must be entered in the format 9999999999. Up to 10 digits allowed.")
    phone = models.CharField('Phone number',validators =[phone_regex], max_length=14, unique=True,null=True)
    is_verified = models.BooleanField('verified', default=False, help_text='Designates whether this user has verified phone')
    key = models.CharField(max_length=100, unique=True, blank=True)
    USERNAME_FIELD = 'phone'


    objects = UserManager()  


    def __str__(self):
        return f'{self.phone} / {self.username}' 
    
    def authenticate(self, otp):
        """ This method authenticates the given otp"""
        provided_otp = 0
        try:
            provided_otp = int(otp)
        except:
            return False
        #Here we are using Time Based OTP. The interval is 60 seconds.
        #otp must be provided within this interval or it's invalid
        t = pyotp.TOTP(self.key, interval=300)
        return t.verify(provided_otp)
    
       

class  Permium(models.Model):
    Gold= 'G'
    Silver= 'S'
    Boronze= 'B'
    STATUS= [
        (Gold, 'G'),
        (Silver, 'S'),
        (Boronze, 'B')
    ]
    user = models.OneToOneField(CustomUser,on_delete=models.DO_NOTHING, related_name="permium")
    status = models.CharField("type of permium account", max_length=1, choices=STATUS)
    description = models.TextField(blank=True,null=True)
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateField("after active a permium account its end in 3 month", auto_now=False, auto_now_add=False)
    price = models.PositiveIntegerField(null=True, blank=True)
    

    def __str__(self):
        return f'{self.user.username} , {self.status}'