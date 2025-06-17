from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
    
from django.utils import timezone

class ManejardorCuenta(BaseUserManager):
    # Crear un usuario normal
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError("El usuario debe tener una dirección de correo electrónico")
                    
        # Crear un objeto de usuario
        user = self.model(
            # normalize_email Convierte la email a minusculas y elimina espacios
            email=self.normalize_email(email),            
            name=name,            
        )

        # Establecer la contraseña y guardar el usuario en la base de datos
        user.set_password(password)
        user.is_active = True         
        return user

    # Método para crear un superusuario, el administrador
    def create_superuser(self, name, email, password):
        # Utilizar el método create_user para crear un superusuario
        user = self.create_user(
            email=self.normalize_email(email),            
            name=name,
            password=password,            
        )

        # Establecer permisos y características especiales para el superusuario
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# Creamos el modelo de usuario personalizado que hereda de AbstractBaseUser
class Cuenta(AbstractBaseUser):
    name = models.CharField(max_length=50)       
    email = models.EmailField(max_length=50, unique=True)    
    # Permisos campos requeridos
    date_joined = models.DateTimeField(default=timezone.now)    
    last_login = models.DateTimeField(blank=True, null=True)    
    is_staff = models.BooleanField(default=False, verbose_name="usuario")
    is_admin = models.BooleanField(default=False, verbose_name="Administrador")
    is_active = models.BooleanField(default=True, verbose_name="Actvio")
    # Campos password 

    USERNAME_FIELD = "email" # Campo para iniciar sesión en el admin
    REQUIRED_FIELDS = ["name"] # Los demas campos tiene validación por defecto
    
    # Manejador de usuarios personalizado
    objects = ManejardorCuenta()

    def __str__(self):
        return self.email

