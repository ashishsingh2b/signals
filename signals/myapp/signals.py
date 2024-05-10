# myapp/signals.py

from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import pre_init,pre_save,pre_delete,post_save,post_init,post_delete
from django.core.signals import request_started,request_finished,got_request_exception

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("----------------------------")
    print("Log in signals.. Run Intro..")
    print("Sender:", sender)
    print("Request:", request)
    print("User:", user)
    print(f'Kwargs: {kwargs}')

@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print("----------------------------")
    print("Log Out signals..")
    print("Sender:", sender)
    print("Request:", request)
    print("User:", user)
    print(f'Kwargs: {kwargs}')

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("----------------------------")
    print("Login failed signal ")
    print("Sender:", sender)
    print("Credentials:", credentials)
    print("Request:", request)
    print(f'Kwargs: {kwargs}')

@receiver(pre_save,sender=User)
def at_begining_save(sender,instance, **kwargs):
    print("----------------------------")
    print("Pre save signal ")
    print("new record")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'Kwargs: {kwargs}')

@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created, **kwargs):
  if created:
    print("----------------------------")
    print("Post save signal ")
    print("new record")
    print("Sender:", sender)
    print("Instance:", instance)
    print("Created:",created)
    print(f'Kwargs: {kwargs}')
  else:
    print("----------------------------")
    print("Post save signal ")
    print("Update")
    print("Sender:", sender)
    print("Instance:", instance)
    print("Created:",created)
    print(f'Kwargs: {kwargs}')

@receiver(pre_delete,sender=User)
def at_begining_delete(sender,instance, **kwargs):
    print("----------------------------")
    print("Pre delete signal ")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'Kwargs: {kwargs}')

@receiver(post_delete,sender=User)
def at_begining_init(sender,instance, **kwargs):
    print("----------------------------")
    print("Post delete signal ")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'Kwargs: {kwargs}')

@receiver(pre_init,sender=User)
def at_ending_init(sender,*args, **kwargs):
    print("----------------------------")
    print("pre init signal ")
    print("Sender:", sender)
    print(f'Args:{args}')
    print(f'Kwargs: {kwargs}')

@receiver(post_init,sender=User)
def at_ending_init(sender,*args, **kwargs):
    print("----------------------------")
    print("Post init signal ")
    print("Sender:", sender)
    print(f'Args:{args}')
    print(f'Kwargs: {kwargs}')

@receiver(request_started)
def at_begining_request(sender,environ, **kwargs):
    print("----------------------------")
    print("at begining request signal ")
    print("Sender:", sender)
    print('Environ:', environ)
    print(f'Kwargs: {kwargs}')

@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print("----------------------------")
    print("at ending request signal ")
    print("Sender:", sender)
    print(f'Kwargs: {kwargs}')

@receiver(got_request_exception)
def log_out(sender, request, **kwargs):
    print("----------------------------")
    print("At Request Exception..")
    print("Sender:", sender)
    print("Request:", request)
    print(f'Kwargs: {kwargs}')
