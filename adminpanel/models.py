from django.db import models

# Create your models here.
# admin  info
class AdminUser(models.Model):
   name=models.CharField(max_length=225,null="",blank=True)
   mobile=models.CharField(max_length=225,null="",blank=True)
   password=models.CharField(max_length=225,null="",blank=True)
   whatsapp=models.CharField(max_length=225,null="",blank=True)
   join=models.DateField(auto_now_add=True,blank=True)

   def __str__(self):
     return self.mobile
   

class HowPlayGame(models.Model):
   howplay=models.TextField()
   def __str__(self):
     return self.howplay
   
class Notice(models.Model):
   notice=models.TextField()
   def __str__(self):
     return self.notice
 
class GameRates(models.Model):
   SingleDigit=models.CharField(max_length=225,null="",blank=True)
   Jodi=models.CharField(max_length=225,null="",blank=True)
   SinglePanna=models.CharField(max_length=225,null="",blank=True)
   DoublePanna=models.CharField(max_length=225,null="",blank=True)
   TripplePanna=models.CharField(max_length=225,null="",blank=True)
   HalfSangam=models.CharField(max_length=225,null="",blank=True)
   FullSangam=models.CharField(max_length=225,null="",blank=True)