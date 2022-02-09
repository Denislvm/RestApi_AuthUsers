from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class AuthUsers(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    username = models.CharField(verbose_name='Username', max_length=128)
    email = models.EmailField(verbose_name='email', max_length=254)
    password = models.CharField(verbose_name='password', max_length=64)
    register_date = models.DateField(auto_now=False, auto_now_add=False)
