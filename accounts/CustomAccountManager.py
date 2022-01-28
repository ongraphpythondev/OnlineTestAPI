from django.utils.translation import gettext_lazy
from django.contrib.auth.models import BaseUserManager

# making some changes in default django User database.
class CustomAccountManager(BaseUserManager):
    
    # Method for creating normal user
    def create_user(self,email,username,firstname,lastname,password,**otherfields):
        # In case email not given or is None
        if not email :
            raise ValueError(gettext_lazy('You must Provide email address'))
        
        # Normalizing email
        email = self.normalize_email(email)
        # assigning all fields their respective parameter.
        user = self.model(
            email=email,
            username=username,
            firstname=firstname,
            lastname=lastname,
            **otherfields
        )
        # setting normal user as active user by setting is_active=True
        otherfields.setdefault('is_active',True)
        # setting up password , this way saved password will be hashed instead of normal string
        user.set_password(password)
        # saving all provided data till now in user variable
        user.save()
        # returing user varaible
        return user
        
    # Method for creating superuser
    def create_superuser(self,email,username,firstname,lastname,password,**otherfields):
        
        """ 
        A superuser in django have active, staff and superuser all set to True
        """ 
        # is_active set to True
        otherfields.setdefault('is_active',True)
        # is_staff set to True
        otherfields.setdefault('is_staff',True)
        # is_superuser set to True
        otherfields.setdefault('is_superuser',True)
        
        # In case is_staff is not True below ValueError will be shown
        if otherfields.get('is_staff') is not True :
            raise ValueError(
                'Superuser must be assigned to is_staff=True.'
            )
        # In case is_super is not True below ValueError will be shown
        if otherfields.get('is_superuser') is not True :
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.'
            )
        # after setting all required setting for superuser data is sent to create_user method.
        return self.create_user(email,username,firstname,lastname,password,**otherfields)
        