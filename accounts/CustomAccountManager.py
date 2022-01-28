from multiprocessing.sharedctypes import Value
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import BaseUserManager

class CustomAccountManager(BaseUserManager):
    
    def create_user(self,email,username,firstname,lastname,password,**otherfields):
        
        if not email :
            raise ValueError(gettext_lazy('You must Provide email address'))
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            firstname=firstname,
            lastname=lastname,
            **otherfields
        )
        otherfields.setdefault('is_active',True)
        user.set_password(password)
        user.save()
        return user
        
    
    def create_superuser(self,email,username,firstname,lastname,password,**otherfields):
        
        otherfields.setdefault('is_staff',True)
        otherfields.setdefault('is_superuser',True)
        otherfields.setdefault('is_active',True)
        
        if otherfields.get('is_staff') is not True :
            raise ValueError(
                'Superuser must be assigned to is_staff=True.'
            )
        if otherfields.get('is_superuser') is not True :
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.'
            )
        
        return self.create_user(email,username,firstname,lastname,password,**otherfields)
        