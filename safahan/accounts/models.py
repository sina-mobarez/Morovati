from multiprocessing import Condition
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.core.validators import RegexValidator



import pyotp


class UserManager(BaseUserManager):
   
    def create_user(self, username, email, phone, password, **extra_fields):
        """
        Create and save a User with the given email, phone number and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        if not phone:
            raise ValueError('The Phone must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, phone, password, **extra_fields):
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

        return self.create_user(username, email, phone, password, **extra_fields)




class CustomUser(AbstractUser):
    phone_regex = RegexValidator( regex = '^9\d{9}$', message ="Phone number must be entered in the format 9999999999. Up to 10 digits allowed.")
    phone = models.CharField('Phone number',validators =[phone_regex], max_length=14, unique=True,null=True)
    is_verified = models.BooleanField('verified', default=False, help_text='Designates whether this user has verified phone')
    key = models.CharField(max_length=100, unique=True, blank=True)
    email = models.EmailField('email address', unique=True)
    mac_address = models.CharField("a unique address of every device", max_length=120, null=True, blank=True)
    last_name = models.CharField("family name", max_length=32, null=True, blank=True)
    REQUIRED_FIELDS = ['email', 'phone']


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
    
    
    
    
class Filter(models.Model):
    name = models.CharField("name of filter", max_length=50)
    description = models.TextField("a full description for filter")
    price = models.PositiveIntegerField("price of a filter")
    user = models.ForeignKey(CustomUser, verbose_name="user", on_delete=models.CASCADE)
    rank = models.CharField("rank of filter", max_length=3, null=True, blank=True)
    active = models.BooleanField("boolean field")
    
    
    def save(self, *args, **kwargs):
        if not self.rank:
            self.rank = Rank.objects.filter(filter= self)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.user.name} , {self.user}'
    
    


class Conditions(models.Model):
    type = models.IntegerField("")
    value = models.CharField("value of type", max_length=150)
    filter = models.ForeignKey(Filter, verbose_name="belong to a filter", on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.type} , {self.filter}'    
    
    
    
    
class Rank(models.Model):
    rate = models.PositiveIntegerField("its must from 0 to 5")
    user = models.ForeignKey(CustomUser, verbose_name="what user give this rate", on_delete=models.CASCADE)
    filter = models.ForeignKey(Filter, verbose_name="belong to a filter", on_delete=models.CASCADE, related_name='ranks')
    
    def __str__(self):
        return f'{self.user.rate} , {self.user}'    



    
class Alarm(models.Model):
    name = models.CharField("name of alarm", max_length=50)
    instanceCode = models.CharField("instance code", max_length=100)
    type = models.IntegerField("type of alarm")
    valueType = models.CharField("type for value", max_length=50)
    value = models.CharField("value", max_length=50)
    active = models.BooleanField("boolean field")
    user = models.ForeignKey(CustomUser, verbose_name="what user give this", on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.name} , {self.user}' 
    
    
    

class StockScout(models.Model):
    name = models.CharField("name of stock", max_length=50)
    instanceCode = models.CharField("code for instance", max_length=100)
    user = models.ForeignKey(CustomUser, verbose_name="what user give this", on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.user.name} , {self.user}' 
    
    
    
class CoinScout(models.Model):
    name = models.CharField("name", max_length=50)
    user = models.ForeignKey(CustomUser, verbose_name="what user give this", on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return f'{self.user.name} , {self.user}' 
    
    
    
    
