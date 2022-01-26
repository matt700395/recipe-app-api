from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fileds):
        """Creates and saves a new user"""
        user = self.model(email=email, **extra_fileds) #user라고하는 변수로 email을 modelf에 받아 오겠다는 뜻
        user.set_password(password) #set_password() 함수는 매개변수로 들어온걸 비밀번호 저장을 위해 암호화함 | BaseUserManager 나 AbstractBaseUser 둘 다에 들어있는 함수임
        user.save(using=self._db) #using=self._db를 넣으면 다양한 db에 모델의 내용을 저장할 수 있음

        return user

class User(AbstractBaseUser, PermissionsMixin): #장고 사용자 모델을 사용하지만, 그 위에 빌드하고 사용자정으를 할 수 있다
    #이메일을 사용자 아이디로 받기 위한 작업을 진행할 예정
    """Custom user model that supports using email instead of username"""
    """Field of data base model"""
    email = models.EmailField(max_length=255, unique=True) #unique=Ture면 한명당 email 하나만 만들고 사용가능
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    