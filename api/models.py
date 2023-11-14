from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

## ================== SECCIÓN MODELO USUARIO ==================

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Tienes que proveer un email')

        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user
    
    def create_user(self, email = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
## MODELO OFICIAL DEL USUARIO PARA UCM SPORTS
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank = True, default='', unique=True)
    membresia = models.BooleanField(default = True)
    reservas_alta_demanda = models.IntegerField()

    ## DJANGO
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank = True, null = True)

    rol = models.CharField(max_length=10)

    # Esto apunta al CustomUserManager que configuramos
    objects = CustomUserManager()

    # Definimos los campos de username y de email del modelo
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if self.is_staff:
            self.rol = 'ADMIN'
        else:
            self.rol = 'USUARIO'
        super().save(*args, **kwargs)
    
## ==================  FIN SECCIÓN MODELO USUARIO ==================