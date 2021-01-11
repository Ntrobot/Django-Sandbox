## Snippet for One-to-One Relational Model
## Directory: In the individual app folder
## Date: 01/04/2021
## Variables to be changed: Profile

### signals.py ###
# This will give new User object a one-to-one relationship to the *Profile* classes automatically

# A signal is fired after a models object is created
from django.db.models.signals import post_save

# Sender is the User class
from django.contrib.auth.models import User

# Receiver is the function that performs tasks from the sender
from django.dispatch import receiver

# Importing the profile class
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    

### apps.py ###

from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'app_name'

    # LINES TO BE ADDED BELOW
    # for the automatic one-to-one relationshihp between Profile and User class
    def ready(self):
        import users.signals

        
