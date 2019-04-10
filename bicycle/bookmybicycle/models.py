from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.
class UserOfApp(AbstractUser):
    #uid= models.AutoField(primary_key=True
    #uname= models.CharField(max_length=100)
    #upass= models.CharField(max_length=100)
    # email= models.EmailField(unique=True)
    # USERNAME_FIELD = 'email'
    uaddr= models.CharField(max_length=100)
    zip= models.CharField(max_length=6)
    state= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    phone= models.CharField(max_length=10)
    # udob= models.DateField()
    # uactive= models.BooleanField(default= False)
    #REQUIRED_FIELDS = ['uaddr']                #add other attributes in this list


    def __str__(self):
        # return f"uid={self.uid}, uname={self.uname}, upass={self.upass}"
        return self.username

# class LogOfApp(models.Model):
#     lid= models.AutoField(primary_key=True)
#     # ldate= models.DateTimeField()
#     uid= models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
#
#     def __str__(self):
#         return f"lid = {self.lid}, uid = {self.uid}"

class Stand(models.Model):
    sid= models.AutoField(primary_key=True)
    sstate= models.CharField(max_length=100,default=False)
    scity= models.CharField(max_length=100,default=False)
    sloc= models.CharField(max_length=100)

    def __str__(self):
        return f"{self.sid}"

class Cycle(models.Model):
    cid = models.AutoField(primary_key= True)
    cstate = models.BooleanField(default= False)
    sid= models.ForeignKey(Stand, on_delete= models.CASCADE, db_column='sid')
    rides= models.ManyToManyField(get_user_model(), blank=True)


    def __str__(self):
        return f"{self.cid}"

class Book(models.Model):
    bid= models.AutoField(primary_key=True)
    cid= models.ForeignKey(Cycle, on_delete= models.CASCADE, db_column='cid')
    sid_start= models.ForeignKey(Stand, on_delete= models.CASCADE, related_name="sid_start",default= -1, db_column='sid_start')
    sid_end= models.ForeignKey(Stand, on_delete= models.CASCADE, related_name="sid_end",default= -1, db_column='sid_end')
    uid= models.ForeignKey(UserOfApp, on_delete=models.CASCADE, db_column='uid')
#    from_date_time =
#    to_date_time =
    def __str__(self):
        return f"{self.bid}"
