from .models import CustomUser
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import pyotp




        
def is_unique(key):
    try:
        CustomUser.objects.get(key=key)
    except CustomUser.DoesNotExist:
        return True
    return False        
        
def generate_key():
    """ User otp key generator """
    key = pyotp.random_base32()
    if is_unique(key):
        return key
    generate_key()
    
    





@receiver(pre_save, sender=CustomUser)
def create_key(sender, instance, **kwargs):

    if not instance.key:
        instance.key = generate_key()