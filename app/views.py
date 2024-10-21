from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from datetime import datetime,date,time
from app.models import *
from adminpanel.models import *
from django.core.mail import send_mail
import random
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.

# register page
def index(request):
    md=ApplicationMode.objects.get(id=1)
    if(md.mode == "on"):
        if request.session.has_key('username'):
            mobile = request.session['username']
            Password = request.session['password']
            user=authenticate(username=mobile+"@gmail.com",password=Password)
            login(request,user)
            return redirect(games)
        else:
            return render(request,"index.html")
    else:
        return render(request,"calculator.html")

# loginpg page
def loginpg(request):
    return render(request,"login.html")

def forgetpassword(request):
    return render(request,"forgot.html")

def games(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    if client.status == "yes":
        gm=Games.objects.all().values()
        sp=AdminInfo.objects.get(id=1)
        notice=Notice.objects.get(id=1)
        return render(request,"game.html",{"client":client,"gm":gm,"sp":sp,"notice":notice})
    else:
        gm=Games.objects.all().values()
        sp=AdminInfo.objects.get(id=1)
        notice=Notice.objects.get(id=1)
        return render(request,"inactive.html",{"client":client,"gm":gm,"sp":sp,"notice":notice})

def addfunds(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    sp=AdminInfo.objects.get(id=1)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"addfunds.html",{"client":client,"sp":sp})

def withdrawal(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    sp=AdminInfo.objects.get(id=1)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"withdrawal.html",{"client":client,"sp":sp})

def starlines(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    gm=StarlineGames.objects.all().values()
    return render(request,"starlines.html",{"client":client,"gm":gm})

def GaliDesawarPage(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    gm=GaliDesawarGame.objects.all().values()
    return render(request,"GaliDesawar.html",{"client":client,"gm":gm})



def myprofile(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"myprofile.html",locals())

def privacypolicy(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    return render(request,"privacypolicy.html")

def howtoplay(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    return render(request,"howtoplay.html")

def gameprice(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    rt=GameRates.objects.get(id=1)
    return render(request,"gameprice.html",{"client":client,"rt":rt})

def payment(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    dt=PaymentDetails.objects.get(user=user)
    client=customer.objects.get(user=user)
    return render(request,"payment.html",locals())

def history(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"history.html",locals())

def DepositHistory(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    dt=DepositRequest.objects.filter(mobile=client.mobile)
    return render(request,"DepositHistory.html",{"client":client,"dt":dt})

def BidHistory(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    dt=Beting.objects.filter(mobile=client.mobile)
    return render(request,"BidHistory.html",{"client":client,"dt":dt})

def bidwinhistory(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    dt=Beting.objects.filter(mobile=client.mobile,status="Success")
    return render(request,"BidWinHistory.html",{"client":client,"dt":dt})

def passbook(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    dt=Withdrawal.objects.filter(mobile=client.mobile)
    return render(request,"passbook.html",{"client":client,"dt":dt})

def StarlineBidHistory(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    dt=StarlineBeting.objects.filter(mobile=client.mobile)

    return render(request,"StarlineBidHistory.html",{"client":client,"dt":dt})

def StarlineWinHistory(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    dt=StarlineBeting.objects.filter(mobile=client.mobile,status="Success")

    return render(request,"StarlineWinHistory.html",{"client":client,"dt":dt})

def GaliBidHistory(request):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    dt=GaliDesawarBeting.objects.filter(mobile=client.mobile)

    return render(request,"DesawarHistory.html",{"client":client,"dt":dt})

def CloseGame(request,pid):
    gm=Games.objects.get(name=pid)
    gm.status="close"
    gm.save()
    return redirect(games)

def CloseGameStarline(request,pid):
    gm=StarlineGames.objects.get(name=pid)
    gm.status="close"
    gm.save()
    return redirect(games)

def OpenGame(request):
    gm=Games.objects.all().values()
    for i in gm:
        i.status="open"
        i.save()
    return redirect(games)

# create account
@csrf_exempt
def createAc(request):
    if request.method=="POST":
        name=request.POST.get('usernm')
        mobile=request.POST.get('contact_no')
        Password=request.POST.get('password')
        cpsw=request.POST.get("password_confirmation")
        bt=AdminInfo.objects.get(id=1)

        if(len(customer.objects.filter(mobile=mobile))>=1):
            message={'message':'number is alerady use !!!'}
            return render(request,'index.html',message)
        elif(Password!=cpsw):
            message={'message':'Password dont match !!!'}
            return render(request,'index.html',message)
        
        else:
            user=User.objects.create_user(first_name=name,username=mobile+"@gmail.com",password=Password)
            Employees=customer(mobile=mobile,user=user,name=name,password=Password,join=datetime.today(),wallet=bt.bonus)
            Employees.save()
            pm=PaymentDetails(user=user,mobile=mobile)
            pm.save()
            request.session['username'] = mobile+"@gmail.com"
            request.session['password'] = Password
            userr=authenticate(username=mobile+"@gmail.com",password=Password)
            login(request,user)
            message={'message':'Your Account Successfully Create,Please Login'}
            # return render(request,'index.html',message)
            return redirect(games)
    return redirect(index)
        

# login 
@csrf_exempt
def loginuser(request):
     if request.method == "POST":
        mobile=request.POST.get('contact_no')
        Password=request.POST.get('password')
        user=authenticate(username=mobile+"@gmail.com",password=Password)
        if user:
         login(request,user)
         request.session['username'] = mobile+"@gmail.com"
         request.session['password'] = Password
         return redirect(games)
        else:
            message={'message':'Invalid details !!!'}
            return render(request,'login.html',message)
        
     return redirect(loginpg)

# logout
def Elogout(request):
    logout(request)
    return redirect(loginpg)


# updateprofile
@csrf_exempt
def updateprofile(request):
    if request.method == "POST":
        mobile=request.POST.get('contact_no')
        email=request.POST.get('email')
        name=request.POST.get('name')
        
        dt=customer.objects.get(mobile=mobile)
        dt.name=name
        dt.email=email
        dt.save()

        message={'message':'Profile Update !!!'}
        return render(request,"myprofile.html",message)
        
        
    return redirect()

# updatepaymentInfo
@csrf_exempt
def updatepaymentInfo(request):
    if request.method == "POST":
        paytm=request.POST.get('paytm')
        phonepay=request.POST.get('phonepe')
        gpay=request.POST.get('googlepay')
        ac=request.POST.get('ac_number')
        ifsc=request.POST.get('ifsc')
        bankname=request.POST.get('bank_name')
        holder=request.POST.get('ac_holder_name')

        user=request.user
        dt=PaymentDetails.objects.get(user=user)
        dt.paytm=paytm
        dt.phonepay=phonepay
        dt.gpay=gpay
        dt.ac=ac
        dt.ifsc=ifsc
        dt.bankname=bankname
        dt.holder=holder
        dt.save()
        
        return redirect(payment)
        
        
    return redirect()

# withdrawal
@csrf_exempt
def withdrawalammount(request):
    if request.method == "POST":
        amt=request.POST.get("amount")
        b_id=Withdrawal.objects.all().last()
        if(b_id.txid == "" or b_id.txid == " "):
            txid=1000
        else:
            txid=int(b_id.txid)+1
        user=request.user
        us=customer.objects.get(user=user)

        if(int(amt)>us.wallet):
            message={'message':'Invalid Ammount !!!'}
            return render(request,"withdrawal.html",message)
        
        else:
            us.wallet=us.wallet-int(amt)
            rq=Withdrawal(mobile=us.mobile,txid=txid,amount=amt,status="Processing")
            rq.save()
            us.save()
            message={'message':'Withdrawal Request Sent Success'}
            return render(request,"withdrawal.html",message)
    return redirect(withdrawal)

# Deposit
@csrf_exempt
def UserDeposit(request):
    if request.method == "POST":
        utr=request.POST.get("utr")
        amt=request.POST.get("amount")
        user=request.user
        us=customer.objects.get(user=user)

        if(len(DepositRequest.objects.filter(utr=utr))>=1):
            message='Invalid UTR No. !!!'
            return render(request,"addfunds.html",{"message":message,"client":us})
        
        else:
            dt=DepositRequest(mobile=us.mobile,amount=amt,utr=utr,status="Pending")
            dt.save()
            message="Recharge Request Sent Success,Please Wait For Admin Confirmation"
            return render(request,"addfunds.html",{"message":message,"client":us})
    return redirect(addfunds)


# gametype page
def gametype(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    return render(request,"gametype.html",{"name":pid})
        

# game type pages

def SingleAnk(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"singleank.html",{"name":pid,"client":client,"td":datetime.today()}) 

def jodi(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"jodi.html",{"name":pid,"client":client,"td":datetime.today()}) 

def SinglePatti(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"singlepatti.html",{"name":pid,"client":client,"td":datetime.today()}) 

def DoublePatti(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"doublepatti.html",{"name":pid,"client":client,"td":datetime.today()}) 

def TripplePatti(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"tripplepatti.html",{"name":pid,"client":client,"td":datetime.today()}) 

def HalfSangam(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"hafsanagm.html",{"name":pid,"client":client,"td":datetime.today()}) 

def FullSangam(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"fullsangam.html",{"name":pid,"client":client,"td":datetime.today()}) 

def SpMotor(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"spmotar.html",{"name":pid,"client":client,"td":datetime.today()}) 

def DpMotor(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"dpmotar.html",{"name":pid,"client":client,"td":datetime.today()}) 


# Beting
@csrf_exempt
def singlebet(request):
    if request.method == "POST":
        pt=""
        dt=""
        dts=[]
        pts=[]
        session=request.POST.get("session")
        digits=request.POST.get("digit1")
        point=request.POST.get("points1")
        tm=request.POST.get("total")
        gamenm=request.POST.get("game_name")
        pananm=request.POST.get("pana_name")
        page=request.POST.get("page")
        
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        user=request.user
        client=customer.objects.get(user=user)
        digitss=str(digits) + ","
        pointss=str(point) + ","
        
        for x in digitss:
                if x not in punctuations:
                    dt=dt+x
                else:
                    
                    dts.append(dt)
                    dt=""
        [print(x) for x in dts]
        print(dts)

        for z in pointss:
                if z not in punctuations:
                    pt=pt+z
                else:
                    pts.append(pt)
                    pt=""
        [print(z) for z in pts]
    
        if(client.wallet < int(tm)):
            return render(request,page,{"name":gamenm,"client":client,"td":datetime.today(),"message":"Invalid Amount"})
        else:
            for i in range(len(dts)):
               b_id=Beting.objects.all().last()
               txid=int(b_id.bettingid) + 1
            
               dt=Beting(name=gamenm,bettingid=txid,pana_name=pananm,status="Processing",gametype=session,mobile=client.mobile,points=pts[i],digit=dts[i],join=date.today())
               dt.save()
            
            client.wallet=client.wallet-int(tm)
            client.save()
            return render(request,"history.html",{"message":"Bet Add Successful,Chek Beting History","client":client})
    return redirect(games)

@csrf_exempt
def fullsangam(request):
    if request.method == "POST":
        try:
            # Initialize variables
            dts = []
            pts = []
            
            # Get data from the form POST request
            session = request.POST.get("session")
            open_digits = request.POST.get("digits")  # Open Panna
            close_digits = request.POST.get("closedigits")  # Close Panna
            points = request.POST.get("points")  # Points entered
            
            game_name = request.POST.get("game_name")
            pana_name = request.POST.get("pana_name")
            page = request.POST.get("page")
            
            # Combine open and close digits to form the 'Sangam'
            combined_digits = f"{open_digits}-{close_digits}"
            
            # Retrieve the current user and client details
            user = request.user
            client = customer.objects.get(user=user)
            print("--->>>", points, open_digits, close_digits)
            # Validate input data
            if not points or not open_digits or not close_digits:
                raise ValueError("All fields are required.")
            
            # Check if the client has enough balance in the wallet
            if client.wallet < int(points):
                return render(request, page, {
                    "name": game_name,
                    "client": client,
                    "td": datetime.today(),
                    "message": "Invalid Amount"
                })
            
            # Save each bet into the database
            for digit in combined_digits.split(','):
                if digit.strip():
                    dts.append(digit.strip())
            for point in points.split(','):
                if point.strip():
                    pts.append(point.strip())
            
            for i in range(len(dts)):
                b_id = Beting.objects.all().last()
                txid = int(b_id.bettingid) + 1 if b_id else 1  # Increment betting ID for uniqueness
                
                dt = Beting(
                    name=game_name,
                    bettingid=txid,
                    pana_name=pana_name,
                    status="Processing",
                    gametype=session,
                    mobile=client.mobile,
                    points=pts[i],
                    digit=dts[i],
                    join=date.today()
                )
                dt.save()
            
            # Deduct the total points from the client's wallet
            client.wallet -= int(points)
            client.save()
            
            # Redirect to the history page or a success message
            return render(request, "history.html", {
                "message": "Bet Add Successful, Check Betting History",
                "client": client
            })

        except Exception as e:
            # Handle exceptions and log them
            return render(request, page, {
                "name": game_name,
                "client": client,
                "td": datetime.today(),
                "message": f"An error occurred: {str(e)}"
            })
    
    return redirect(history)



@csrf_exempt
def GaliJodiBet(request):
    if request.method == "POST":
        pt=""
        dt=""
        dts=[]
        pts=[]
        session=request.POST.get("session")
        digits=request.POST.get("digit1")
        point=request.POST.get("points1")
        tm=request.POST.get("total")
        gamenm=request.POST.get("game_name")
        pananm=request.POST.get("pana_name")
        digitss=digits+","
        pointss=point+","
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        user=request.user
        client=customer.objects.get(user=user)

        for x in digitss:
                if x not in punctuations:
                    dt=dt+x
                else:
                    dts.append(dt)
                    dt=""
        [print(x) for x in dts]

        for z in pointss:
                if z not in punctuations:
                    pt=pt+z
                else:
                    pts.append(pt)
                    pt=""
        [print(z) for z in pts]
    
        if(client.wallet < int(tm)):
            return render(request,"GaliDesawar/Jodi.html",{"name":gamenm,"client":client,"td":datetime.today(),"message":"Invalid Amount"})
        else:
            for i in range(len(dts)):
                 b_id=GaliDesawarBeting.objects.all().last()
                 txid=int(b_id.bettingid) + 1
                 dt=GaliDesawarBeting(name=gamenm,bettingid=txid+i,pana=pananm,status="Processing",gametype=session,mobile=client.mobile,points=pts[i],digit=dts[i],join=date.today())
                 dt.save()
            
            client.wallet=client.wallet-int(tm)
            client.save()
            return render(request,"GaliDesawar/Jodi.html",{"message":"Bet Add Successful,Chek Beting History","client":client})

     

    return HttpResponse("err")

@csrf_exempt
def spmotarbet(request):
    if request.method == "POST":
        session=request.POST.get("session")
        digits=request.POST.get("digits")
        point=request.POST.get("points")
        gamenm=request.POST.get("game_name")
        pananm=request.POST.get("pana_name")
        b_id=Beting.objects.all().last()
        if(b_id.bettingid == "" or b_id.bettingid == " "):
            txid=1000
        else:
            txid=int(b_id.bettingid)+1
        user=request.user
        client=customer.objects.get(user=user)
        if(client.wallet < int(point)):
            return render(request,"spmotar.html",{"name":gamenm,"client":client,"td":datetime.today(),"message":"Invalid Amount"})
        else:
            
            dt=Beting(name=gamenm,bettingid=txid,pana_name=pananm,status="Processing",gametype=session,mobile=client.mobile,points=point,digit=digits,join=datetime.today())
            dt.save()
            client.wallet=client.wallet-int(point)
            client.save()
            return render(request,"history.html",{"message":"Bet Add Successful,Chek Beting History","client":client})

    return redirect(SpMotor)

@csrf_exempt
def sangambet(request):
    if request.method == "POST":
        session=request.POST.get("closedigits")
        digits=request.POST.get("digits")
        point=request.POST.get("points")
        gamenm=request.POST.get("game_name")
        pananm=request.POST.get("pana_name")
        page=request.POST.get("page")
        b_id=Beting.objects.all().last()
        if(b_id.bettingid == "" or b_id.bettingid == " "):
            txid=1000
        else:
            txid=int(b_id.bettingid)+1
        user=request.user
        client=customer.objects.get(user=user)
        if(client.wallet < int(point)):
            return render(request,page,{"name":gamenm,"client":client,"td":datetime.today(),"message":"Invalid Amount"})
        else:
            dt=Beting(name=gamenm,bettingid=txid,pana_name=pananm,status="Processing",gametype=session,mobile=client.mobile,points=point,digit=digits,join=datetime.today())
            dt.save()
            client.wallet=client.wallet-int(point)
            client.save()
            return render(request,"history.html",{"message":"Bet Add Successful,Chek Beting History","client":client})
    return redirect(HalfSangam)



# Starline Games

def starlinegametype(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    return render(request,"StarlineGameType.html",{"name":pid})



def StarlineSingleAnk(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"starline/SingleDigit.html",{"name":pid,"client":client,"td":datetime.today()}) 



def StarlineSinglePatti(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"starline/SinglePatti.html",{"name":pid,"client":client,"td":datetime.today()}) 

def StarlineDoublePatti(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"starline/DoublePanna.html",{"name":pid,"client":client,"td":datetime.today()}) 

def StarlineTripplePatti(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"starline/TripplePatti.html",{"name":pid,"client":client,"td":datetime.today()}) 

def GaliJodi(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    user=request.user
    client=customer.objects.get(user=user)
    return render(request,"GaliDesawar/Jodi.html",{"name":pid,"client":client,"td":datetime.today()}) 



# Beting
@csrf_exempt
def StarlineSinglebet(request):
    if request.method == "POST":
        pt=""
        dt=""
        dts=[]
        pts=[]
        session=request.POST.get("session")
        digits=request.POST.get("digit1")
        point=request.POST.get("points1")
        tm=request.POST.get("total")
        gamenm=request.POST.get("game_name")
        pananm=request.POST.get("pana_name")
        digitss=digits+","
        pointss=point+","
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        user=request.user
        client=customer.objects.get(user=user)

        for x in digitss:
                if x not in punctuations:
                    dt=dt+x
                else:
                    dts.append(dt)
                    dt=""
        [print(x) for x in dts]

        for z in pointss:
                if z not in punctuations:
                    pt=pt+z
                else:
                    pts.append(pt)
                    pt=""
        [print(z) for z in pts]
    
        if(client.wallet < int(tm)):
            return render(request,"starline/SingleDigit.html",{"name":gamenm,"client":client,"td":datetime.today(),"message":"Invalid Amount"})
        else:
            for i in range(len(dts)):
                 b_id=StarlineBeting.objects.all().last()
                 txid=int(b_id.bettingid) + 1
                 dt=StarlineBeting(name=gamenm,bettingid=txid,pana=pananm,status="Processing",gametype=session,mobile=client.mobile,points=pts[i],digit=dts[i],join=datetime.today())
                 dt.save()
            
            client.wallet=client.wallet-int(tm)
            client.save()
            return render(request,"StarlineBidHistory.html",{"message":"Bet Add Successful,Chek Beting History","client":client})

     

    return HttpResponse("err")




# GaliDesawar Games

def GaliGameType(request,pid):
    if not request.user.is_authenticated:
        return redirect(loginpg)
    return render(request,"GaliDesawar/GaliGameType.html",{"name":pid})



# page not found
def not400(request,exception):
    return render(request,'404notfound.html')