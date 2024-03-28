from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth import get_user_model



from django.db.models.signals import post_save
from django.dispatch import receiver


#User =  get_user_model()


# User Manager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        if not password:
            raise ValueError("User must have password")

        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_freeuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        
        user.free_user =True
        user.save(using=self._db)
        return user
    def create_customeuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        
        user.custome_user =True
        user.save(using=self._db)
        return user
    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.custome_user =True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.custome_user =True
        user.admin = True
        user.save(using=self._db)
        return user



# Custom user Module's 
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255,blank=True)
    last_name=models.CharField(max_length=255,blank=True)
    phone_number=models.CharField(max_length=255,blank=True)
    profile_imag= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login=  models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    free_user = models.BooleanField(default=False)
    custome_user = models.BooleanField(default=False)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.
    # add User Manager
    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
    @property
    def is_free_user(self):
        "Is the user a free user member?"
        return self.free_user
    @property
    def is_custome_user(self):
        "Is the user a custome user member?"
        return self.custome_user
    
    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if User.objects.filter(email = self.email):
            return True

        return False
    
    #to save the data
    def register(self):
        self.save()
    
    """def make_password(self,password):
        
        return self.PBKDF2PasswordHasher(password)"""
        
class FreeAccountUser(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    free_user = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255,blank=True)
    last_name=models.CharField(max_length=255,blank=True)
    phone_number=models.CharField(max_length=255,blank=True)
    password =models.CharField(max_length=255)
    
    """def make_password(self):
        
        return  PBKDF2PasswordHasher(self.password).encode()"""
    
    def isExists(self):
        if User.objects.filter(email = self.email):
            return True

        return False
    
    #to save the data
    def register(self):
        self.save()
    
    #to save the data
   
class CutomeAccountUser(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    custome_user = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255,blank=True)
    last_name=models.CharField(max_length=255,blank=True)
    phone_number=models.CharField(max_length=255,blank=True)
    password =models.CharField(max_length=255)
    
    """def make_password(self):
        
        return  PBKDF2PasswordHasher(self.password).encode()"""
    
    def isExists(self):
        if User.objects.filter(email = self.email):
            return True

        return False
    
    #to save the data
    def register(self):
        self.save()
    
    #to save the data
    
    
    
@receiver(post_save, sender=FreeAccountUser)
def create_free_account(sender, instance, created, **kwargs):
    if created:
        User.objects.create(
                            free_user=instance.free_user,
                            email=instance.email,
                            first_name=instance.first_name,
                            last_name=instance.last_name,
                            phone_number=instance.phone_number,
                            password =instance.password 
                             
                               ) 
        
@receiver(post_save, sender=CutomeAccountUser)
def create_custome_account(sender, instance, created, **kwargs):
    if created:
        User.objects.create(
                         custome_user=instance.custome_user,
                         email=instance.email,
                            first_name=instance.first_name,
                            last_name=instance.last_name,
                            phone_number=instance.phone_number,
                            password =instance.password 
                               ) 
    
