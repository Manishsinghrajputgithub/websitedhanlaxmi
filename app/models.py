from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# customer Profile
class customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    mobile=models.CharField(max_length=225)
    password=models.CharField(max_length=125)
    email=models.CharField(max_length=225,null="",blank=True)
    wallet=models.IntegerField(default=0)
    status=models.CharField(max_length=225,default="no",blank=True)
    join=models.DateTimeField(auto_now_add=True, blank=True)
   
   
    def __str__(self):
     return self.user.first_name
    
# customer payment details
class PaymentDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=225,null="",blank=True)
    paytm=models.CharField(max_length=225,null="",blank=True)
    phonepay=models.CharField(max_length=225,null="",blank=True)
    gpay=models.CharField(max_length=225,null="",blank=True)
    ac=models.CharField(max_length=255,null="",blank=True)
    ifsc=models.CharField(max_length=225,null="",blank=True)
    bankname=models.CharField(max_length=255,null="",blank=True)
    holder=models.CharField(max_length=255,null="",blank=True)

    def __str__(self):
     return self.mobile
   

# admin contact info
class AdminInfo(models.Model):
   whatsapp=models.CharField(max_length=225,null="",blank=True)
   telegram=models.CharField(max_length=225,null="",blank=True)
   support=models.CharField(max_length=225,null="",blank=True)
   bonus=models.CharField(max_length=225,null="",blank=True)
   MinimumDeposit=models.CharField(max_length=225,null="",blank=True)
   MinimumWithdraw=models.CharField(max_length=225,null="",blank=True)
   WithdrawOpenTime=models.CharField(max_length=225,null="",blank=True)
   WithdrawCloseTime=models.CharField(max_length=225,null="",blank=True)
   upi=models.CharField(max_length=225,null="",blank=True)
   barcode=models.ImageField()

   def __str__(self):
     return self.whatsapp
   
  # game
class Games(models.Model):
   name=models.CharField(max_length=225,null="",blank=True)
   open=models.CharField(max_length=225,null="",blank=True)
   close=models.CharField(max_length=225,null="",blank=True)
   holiday=models.CharField(max_length=225,null="",blank=True)
   chart=models.CharField(max_length=225,null="",blank=True)
   OpenPanna=models.CharField(max_length=225,null="",blank=True)
   ClosePanna=models.CharField(max_length=225,null="",blank=True)
   SinglePanna=models.CharField(max_length=225,null="",blank=True)
   JodiPanna=models.CharField(max_length=225,null="",blank=True)
   status=models.CharField(max_length=225,null="",blank=True ,default="close")

   def __str__(self):
     return self.name
   
    #milan game
class StarlineGames(models.Model):
   name=models.CharField(max_length=225,null="",blank=True)
   chart=models.CharField(max_length=225,null="",blank=True)
   holiday=models.CharField(max_length=225,null="",blank=True)
   pana=models.CharField(max_length=225,null="",blank=True)
   digit=models.CharField(max_length=225,null="",blank=True)
   jodi=models.CharField(max_length=225,null="",blank=True)
   status=models.CharField(max_length=225,null="",blank=True,default="close")

   def __str__(self):
     return self.name
   
    #Gali game
class GaliDesawarGame(models.Model):
  name=models.CharField(max_length=225,null="",blank=True)
  open=models.CharField(max_length=225,null="",blank=True)
  close=models.CharField(max_length=225,null="",blank=True)
  chart=models.CharField(max_length=225,null="",blank=True)
  Result=models.CharField(max_length=225,null="",blank=True)
  holiday=models.CharField(max_length=225,null="",blank=True)
  status=models.CharField(max_length=225,null="",blank=True ,default="close")


  def __str__(self):
     return self.name
   

# beting
class Beting(models.Model):
   bettingid=models.CharField(max_length=225,default="0",blank=True)
   mobile=models.CharField(max_length=225,null="",blank=True)
   name=models.CharField(max_length=225,null="",blank=True)
   pana_name=models.CharField(max_length=225,null="",blank=True)
   digit=models.CharField(max_length=225,null="",blank=True)
   points=models.CharField(max_length=225,null="",blank=True)
   gametype=models.CharField(max_length=225,null="",blank=True)
   WinAmount=models.CharField(max_length=225,null="",blank=True)
   status=models.CharField(max_length=225,null="",blank=True)
   join=models.DateField(blank=True)

   def __str__(self):
     return self.status
   
# Starline beting
class StarlineBeting(models.Model):
   bettingid=models.CharField(max_length=225,null="",blank=True)
   mobile=models.CharField(max_length=225,null="",blank=True)
   name=models.CharField(max_length=225,null="",blank=True)
   pana=models.CharField(max_length=225,null="",blank=True)
   digit=models.CharField(max_length=225,null="",blank=True)
   points=models.CharField(max_length=225,null="",blank=True)
   gametype=models.CharField(max_length=225,null="",blank=True)
   WinAmount=models.CharField(max_length=225,null="",blank=True)
   status=models.CharField(max_length=225,null="",blank=True)
   join=models.DateField(blank=True)

   def __str__(self):
     return self.status
   
# GaliDesawar beting
class GaliDesawarBeting(models.Model):
   bettingid=models.CharField(max_length=225,null="",blank=True)
   mobile=models.CharField(max_length=225,null="",blank=True)
   name=models.CharField(max_length=225,null="",blank=True)
   pana=models.CharField(max_length=225,null="",blank=True)
   digit=models.CharField(max_length=225,null="",blank=True)
   points=models.CharField(max_length=225,null="",blank=True)
   gametype=models.CharField(max_length=225,null="",blank=True)
   WinAmount=models.CharField(max_length=225,null="",blank=True)
   status=models.CharField(max_length=225,null="",blank=True)
   join=models.DateField(blank=True)

   def __str__(self):
     return self.status


# withdrawl

class Withdrawal(models.Model):
   mobile=models.CharField(max_length=225,null="",blank=True)
   txid=models.IntegerField(null="",blank=True)
   amount=models.IntegerField(null="",blank=True)
   status=models.CharField(max_length=225,null="",blank=True)
   join=models.DateTimeField(auto_now_add=True,blank=True)
   
   def __str__(self):
     return self.mobile
   
class DepositRequest(models.Model):
   mobile=models.CharField(max_length=225,null="",blank=True)
   amount=models.IntegerField(null="",blank=True)
   utr=models.CharField(max_length=225,null="",blank=True)
   status=models.CharField(max_length=225,null="",blank=True)
   join=models.DateTimeField(auto_now_add=True,blank=True)
   
   def __str__(self):
     return self.mobile


# Application Mode
class ApplicationMode(models.Model):
   mode=models.CharField(max_length=50,default='on')

   def __str__(self):
     return self.mode