from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime,date,time
from adminpanel.models import *
from app.models import *
from django.core.mail import send_mail
import random
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, csrf_protect



# Create your views here.

def adminloginpage(request):
    return render(request,"adminpanel/adminlogin.html")


def adminlogin(request):
    if request.method == "POST":
        mobile=request.POST.get('contact_no')
        Password=request.POST.get('password')
        if(len(AdminUser.objects.filter(mobile=mobile))>=1):
            ds=AdminUser.objects.get(mobile=mobile)
            if(ds.mobile==mobile and ds.password==Password): 
                return redirect(adminhome)
                
            else:
                 message={'message':"Password dont match !!!!"}
                 return render(request,'adminpanel/adminlogin.html',message)
            
        
        else:
            message={'message':'Invalid details !!!'}
            return render(request,'adminpanel/adminlogin.html',message)
        
     
    return redirect(adminloginpage)


def adminhome(request):
    dt=customer.objects.all().values().count()
    td=customer.objects.filter(join=date.today()).count()
    ad=AdminUser.objects.all().values()
    gameplay=HowPlayGame.objects.get(id=1)
    return render(request,'adminpanel/adminDashboard.html',{"total":dt,"today":td,"admin":ad,"HowPlayGame":gameplay})

def UserMngPage(request):
    dt=customer.objects.all().values()
    return render(request,'adminpanel/UserManagement.html',{"dt":dt})

def marketgames(request):
    dt=Games.objects.all().values()
    return render(request,'adminpanel/MarketGames.html',{"gm":dt})

def AdminStarlineGames(request):
    dt=StarlineGames.objects.all().values()
    return render(request,'adminpanel/AdminStarlineGames.html',{"gm":dt})

def AdminUsers(request):
    dt=AdminUser.objects.all().values()
    return render(request,'adminpanel/AdminUsers.html',{"dt":dt})

def Support(request):
    dt=AdminInfo.objects.all().values()
    data=AdminInfo.objects.get(id=1)
    return render(request,'adminpanel/Support.html',{"dt":dt,"data":data})

def Mode(request):
    dt=ApplicationMode.objects.get(id=1)
    return render(request,'adminpanel/Mode.html',{"dt":dt})

def AdminHowPlay(request):
    dt=HowPlayGame.objects.get(id=1)
    return render(request,'adminpanel/HowPlay.html',{"dt":dt})

def AdminPswCng(request):
    return render(request,'adminpanel/change_password.html')

def DepositRequestPg(request):
    dt=DepositRequest.objects.all().values()
    return render(request,'adminpanel/DepositRequest.html',{"dt":dt})

def StarlineDeclareResult(request):
    dt=StarlineGames.objects.all().values()
    return render(request,'adminpanel/StarlineResult.html',{"dt":dt})

def AppPointPage(request):
    dt=customer.objects.all().values()
    return render(request,'adminpanel/AppPointPage.html',{"dt":dt})

@csrf_exempt
def AdminAddPoint(request):
    if request.method=="POST":
        ph=request.POST.get("user_id")
        point=request.POST.get("points")
        dt=customer.objects.get(mobile=ph)
        dt.wallet=dt.wallet+int(point)
        dt.save()
    return redirect(AppPointPage)

@csrf_exempt
def AdminWithdrawalPoint(request):
    if request.method=="POST":
        ph=request.POST.get("user_id")
        point=request.POST.get("pointsWithdwaw")
        dt=customer.objects.get(mobile=ph)
        dt.wallet=dt.wallet-int(point)
        dt.save()
    return redirect(UserMngPage)

@csrf_exempt
def UpdateSupport(request):
    if request.method=="POST":
        whatsapp=request.POST.get("whatsapp")
        telegram=request.POST.get("telegram")
        support=request.POST.get("contact")
        bonus=request.POST.get("bonus")
        MinimumDeposit=request.POST.get("MinimumDeposit")
        MinimumWithdraw=request.POST.get("MinimumWithdraw")
        WithdrawOpenTime=request.POST.get("WithdrawOpenTime")
        WithdrawCloseTime=request.POST.get("WithdrawCloseTime")
        upi=request.POST.get("upi")

        data=AdminInfo.objects.get(id=1)
        data.whatsapp=whatsapp
        data.telegram=telegram
        data.support=support
        data.upi=upi
        data.bonus=bonus
        data.MinimumDeposit=MinimumDeposit
        data.MinimumWithdraw=MinimumWithdraw
        data.WithdrawOpenTime=WithdrawOpenTime
        data.WithdrawCloseTime=WithdrawCloseTime
        data.save()

        return redirect(Support)
    
    return redirect(Support)

@csrf_exempt
def changemode(request,pid):
    dt=ApplicationMode.objects.get(id=1)
    if(pid == "on"):
        dt.mode="on"
        msg="Application Mode On, Please refresh page"
        
    else:
        dt.mode="off"
        msg="Calculator Mode On,Please refresh page"

    dt.save() 
    return render(request,'adminpanel/Mode.html',{"message":msg}) 

@csrf_exempt
def Userdelete(request,pid):
    dt=customer.objects.get(mobile=pid)
    user=User.objects.get(username=pid+"@gmail.com")
    user.delete()
    dt.delete()
    return redirect(UserMngPage)

@csrf_exempt
def UserDeactive(request,pid):
    dt=customer.objects.get(mobile=pid)
    if(dt.status == "yes"):
        dt.status="no"
        dt.save()
    else:
        dt.status="yes"
        dt.save()
    return redirect(UserMngPage)

@csrf_exempt
def Admindelete(request,pid):
    dt=AdminUser.objects.get(mobile=pid)
    dt.delete()
    return redirect(AdminUsers)

@csrf_exempt
def GameDelete(request,pid):
    dt=Games.objects.get(name=pid)
    dt.delete()
    return redirect(marketgames)

def AdminMarketBids(request):
    dt=Beting.objects.all().values()
    return render(request,'adminpanel/MarketBids.html',{"dt":dt}) 

def WiningDetails(request):
    dt=Beting.objects.filter(status="Success")
    return render(request,'adminpanel/WiningDitails.html',{"dt":dt}) 

def GaliDesawarMarket(request):
    dt=GaliDesawarGame.objects.all().values()
    return render(request,'adminpanel/GaliMarkets.html',{"gm":dt}) 

def GaliDesawarBids(request):
    dt=GaliDesawarGame.objects.all().values()
    ht=GaliDesawarBeting.objects.all().values()
    return render(request,'adminpanel/GaliBids.html',{"dt":dt,"history":ht}) 

def GaliDesawarResult(request):
    dt=GaliDesawarGame.objects.all().values()
    return render(request,'adminpanel/GaliResult.html',{"dt":dt}) 

def DeclareResPg(request):
    dt=Games.objects.all().values()
    bt=Beting.objects.filter(join=date.today(),status="Processing")
    return render(request,'adminpanel/DeclareResult.html',{"dt":dt,"bt":bt}) 

@csrf_exempt
def ShowWinnerTable(request):
    if request.method == "POST":
        gamenm=request.POST.get("market")
        digit=request.POST.get("digit")
        panna=request.POST.get("panna")
        session=request.POST.get("session")
        bt=Beting.objects.filter(join=date.today(),status="Processing",name=gamenm,gametype=session,digit=panna)
    return render(request,'adminpanel/DeclareResult.html',{"bt":bt}) 

def AdminStarlineBids(request):
    dt=StarlineGames.objects.all().values()
    ht=StarlineBeting.objects.all().values()
    return render(request,'adminpanel/StarlineBids.html',{"dt":dt,"history":ht}) 

def AdminGameRates(request):
    dt=GameRates.objects.get(id=1)
    return render(request,'adminpanel/GameRates.html',{"data":dt}) 

def AdminWithdraw(request):
    dt=Withdrawal.objects.all().values()
    return render(request,'adminpanel/WithdrawRequest.html',{"dt":dt}) 

def SingleResultGame(request,pid):
    dt=Games.objects.get(name=pid)
    return render(request,'adminpanel/SingleResultGame.html',{"dt":dt}) 


@csrf_exempt
def UserProfile(request,pid):
    dt=customer.objects.get(mobile=pid)
    ht=Beting.objects.filter(mobile=pid)
    wt=Withdrawal.objects.filter(mobile=pid)
    payment=PaymentDetails.objects.get(mobile=pid)
    return render(request,'adminpanel/UserProfile.html',{"dt":dt,"ht":ht,"wt":wt,"pd":payment}) 

def NotificationMng(request):
    notice=Notice.objects.get(id=1)
    return render(request,'adminpanel/notification.html',{"notice":notice}) 


@csrf_exempt
def UpdateNotification(request):
     if request.method=="POST":
         msg=request.POST.get("message")
         notice=Notice.objects.get(id=1)
         notice.notice=msg
         notice.save()

     return redirect(NotificationMng)

@csrf_exempt
def UpdateGamePlay(request):
    if request.method=="POST":
        msg=request.POST.get('HowToPlay')
        gameplay=HowPlayGame.objects.get(id=1)
        gameplay.howplay=msg
        gameplay.save()

    return redirect(adminhome)

@csrf_exempt
def AdminAddGame(request):
    if request.method=="POST":
        name=request.POST.get('name')
        open=request.POST.get('open')
        close=request.POST.get('close')
        chart=request.POST.get('chart')
        gm=Games(name=name,open=open,close=close,chart=chart)
        gm.save()
       

    return redirect(marketgames)

@csrf_exempt
def DeclareResult(request):
    if request.method=="POST":
        name=request.POST.get('market')
        panna=request.POST.get('panna')
        digit=request.POST.get('digit')
        session=request.POST.get('session')
        dt=Games.objects.get(name=name)

        if(session == "open"):
            dt.OpenPanna=panna
            dt.SinglePanna=digit
            dt.save()

            bt=Beting.objects.filter(join=date.today(),status="Processing",name=name,gametype="open")
            for i in bt:
                cl=customer.objects.get(mobile=i.mobile)
                if(i.digit == digit):
                     cl.wallet=cl.wallet+int(i.points)*9
                     i.WinAmount=int(i.points)*9
                     i.status="Success"
                     i.save()
                     cl.save()
                elif(i.digit == panna):
                    cl.wallet=cl.wallet+int(i.points)*140
                    i.WinAmount=int(i.points)*140
                    i.status="Success"
                    i.save()
                    cl.save()
             
                else:
                    i.status="Failed"
                    i.save()    

            
        else:
            dt.ClosePanna=panna
            dt.JodiPanna=dt.SinglePanna + digit
            dt.save()

            bt=Beting.objects.filter(join=date.today(),status="Processing",name=name,gametype="close")
            for i in bt:
                cl=customer.objects.get(mobile=i.mobile)
                if(i.digit == panna ):
                    cl.wallet=cl.wallet+int(i.points)*140
                    i.WinAmount=int(i.points)*140
                    i.status="Success"
                    i.save()
                    cl.save()
                
                elif(i.digit == dt.JodiPanna ):
                    cl.wallet=cl.wallet+int(i.points)*90
                    i.WinAmount=int(i.points)*90
                    i.status="Success"
                    i.save()
                    cl.save()
                else:
                    i.status="Failed"
                    i.WinAmount="0"

                    i.save()    
      

    return redirect(DeclareResPg)

@csrf_exempt
def DepositReject(request,pid,utr):
    dt=DepositRequest.objects.get(utr=utr)
    dt.status="Rejected"
    dt.save()
    return redirect(DepositRequestPg)

@csrf_exempt
def DepositApprove(request,pid,utr):
    dt=DepositRequest.objects.get(utr=utr)
    cs=customer.objects.get(mobile=pid)
    cs.wallet=cs.wallet+int(dt.amount)
    dt.status="Success"
    dt.save()
    cs.save()
    return redirect(DepositRequestPg)

@csrf_exempt
def BidUpdate(request):
    if request.method=="POST":
        txid=request.POST.get("bettingid")
        bid=request.POST.get("bid")
        point=request.POST.get("point")
        dt=Beting.objects.get(bettingid=txid)
        dt.digit=bid
        dt.points=point
        dt.save()
                    
    return redirect(AdminMarketBids)

@csrf_exempt
def StarlineBidUpdate(request):
    if request.method=="POST":
        txid=request.POST.get("bettingid")
        bid=request.POST.get("bid")
        point=request.POST.get("point")
        dt=StarlineBeting.objects.get(bettingid=txid)
        dt.digit=bid
        dt.points=point
        dt.save()
                    
    return redirect(AdminStarlineGames)

@csrf_exempt
def GaliBidUpdate(request):
    if request.method=="POST":
        txid=request.POST.get("bettingid")
        bid=request.POST.get("bid")
        point=request.POST.get("point")
        dt=GaliDesawarBeting.objects.get(bettingid=txid)
        dt.digit=bid
        dt.points=point
        dt.save()
                    
    return redirect(GaliDesawarMarket)

@csrf_exempt
def MarketResultDelete(request):
    if request.method=="POST":
        game=request.POST.get("gameID")
        dt=Games.objects.get(name=game)
        dt.OpenPanna=""
        dt.ClosePanna=""
        dt.SinglePanna=""
        dt.JodiPanna=""
        dt.save()
                    
    return redirect(DeclareResPg)

@csrf_exempt
def StarlineResultDelete(request):
    if request.method=="POST":
        game=request.POST.get("gameID")
        dt=StarlineGames.objects.get(name=game)
        dt.pana=""
        dt.digit=""
        dt.jodi=""
       
        dt.save()
                    
    return redirect(StarlineDeclareResult)

def GaliResultDelete(request):
    if request.method=="POST":
        game=request.POST.get("gameID")
        dt=GaliDesawarGame.objects.get(name=game)
        dt.Result=""
       
        dt.save()
                    
    return redirect(DeclareGaliResult)

@csrf_exempt
def UpdateGameRates(request):
    if request.method=="POST":
        SingleDigit=request.POST.get("SingleDigit")
        Jodi=request.POST.get("Jodi")
        SinglePanna=request.POST.get("SinglePanna")
        DoublePanna=request.POST.get("DoublePanna")
        TripplePanna=request.POST.get("TripplePanna")
        HalfSangam=request.POST.get("HalfSangam")
        FullSangam=request.POST.get("FullSangam")

        dt=GameRates.objects.get(id=1)
        dt.SingleDigit=SingleDigit
        dt.Jodi=Jodi
        dt.SinglePanna=SinglePanna
        dt.DoublePanna=DoublePanna
        dt.TripplePanna=TripplePanna
        dt.HalfSangam=HalfSangam
        dt.FullSangam=FullSangam
        dt.save()
                    
    return redirect(AdminGameRates)
    


def MarketGameStatus(request,pid):
    dt=Games.objects.get(name=pid)
    if(dt.status == "open"):
        dt.status="close"
    else:
        dt.status="open"
    dt.save()
    return redirect(marketgames)

def AdminPswChange(request):
    if request.method=="POST":
        old=request.POST.get("Oldpassword")
        new=request.POST.get("Newpassword")
        dt=AdminUser.objects.get(name="Ajay")
        if(dt.password == old):
            dt.password=new
            return render(request,"adminpanel/change_password.html",{"message":"Password Changed"})
        else:
            return render(request,"adminpanel/change_password.html",{"message":"Password Dont Match"})
        
    return redirect(AdminPswCng)


def ViewWithdrawal(request):
    return render(request,"adminpanel/ViewWithdrawal.html")



# starline games
def StarlineGameDelete(request,pid):
    dt=StarlineGames.objects.get(name=pid)
    dt.delete()
    return redirect(AdminStarlineGames)

@csrf_exempt
def StarlineGameAdd(request):
    if request.method=="POST":
        chart=request.POST.get("gameName")
        close=request.POST.get("closeTime")
        if(len(StarlineGames.objects.filter(name=close))>=1):
            return redirect(AdminStarlineGames)
        
        else:
            dt=StarlineGames(name=close,chart=chart)
            dt.save()
            return redirect(AdminStarlineGames)
    
    return redirect(AdminStarlineGames)

def StarlineGameStatus(request,pid):
    dt=StarlineGames.objects.get(name=pid)
    if(dt.status == "open"):
        dt.status="close"
    else:
        dt.status="open"
    dt.save()
    return redirect(AdminStarlineGames)

# GaliDesawar games
def GaliGameDelete(request,pid):
    dt=GaliDesawarGame.objects.get(name=pid)
    dt.delete()
    return redirect(AdminStarlineGames)

@csrf_exempt
def GaliGameAdd(request):
    if request.method=="POST":
        chart=request.POST.get("chart")
        open=request.POST.get("openTime")
        close=request.POST.get("closeTime")
        name=request.POST.get("gameName")
        if(len(GaliDesawarGame.objects.filter(name=close))>=1):
            return redirect(GaliDesawarMarket)
        
        else:
            dt=GaliDesawarGame(name=name,chart=chart,open=open,close=close)
            dt.save()
            return redirect(GaliDesawarMarket)
    
    return redirect(GaliDesawarMarket)

@csrf_exempt
def DeclareGaliResult(request):
    if request.method=="POST":
        gameid=request.POST.get("gameId")
        result=request.POST.get("panna")
        dt=GaliDesawarGame.objects.get(name=gameid)
        dt.Result=result
        dt.save()

        bt=GaliDesawarBeting.objects.filter(date=date.today())
        for i in bt:
            cl=customer.objects.get(mobile=i.mobile)
            if(i.digit == result and i.status == "Processing" and i.name == gameid):
                cl.wallet=cl.wallet+int(i.points)*9
                i.WinAmount=int(i.points)*9
                i.status="Success"
                i.save()
                cl.save()
            else:
                i.status="Failed"
                i.WinAmount="0"
                i.save()    

    return redirect(GaliDesawarResult)

@csrf_exempt
def DeclareStarlineResult(request):
    if request.method=="POST":
        gameid=request.POST.get("gameId")
        pana=request.POST.get("panna")
        single=request.POST.get("digit")
        jodi=request.POST.get("jodi")
        dt=StarlineGames.objects.get(name=gameid)
        dt.pana=pana
        dt.digit=single
        dt.jodi=jodi
        dt.save()

        bt=StarlineBeting.objects.filter(join=date.today())
        for i in bt:
            cl=customer.objects.get(mobile=i.mobile)
            if(i.digit == single and i.status == "Processing" and i.name == gameid):
                cl.wallet=cl.wallet+int(i.points)*9
                i.WinAmount=int(i.points)*9
                i.status="Success"
                i.save()
                cl.save()
            elif(i.digit == pana and i.status == "Processing" and i.name == gameid):
                cl.wallet=cl.wallet+int(i.points)*140
                i.WinAmount=int(i.points)*140
                i.status="Success"
                i.save()
                cl.save()
            elif(i.digit == jodi and i.status == "Processing" and i.name == gameid):
                cl.wallet=cl.wallet+int(i.points)*90
                i.WinAmount=int(i.points)*90
                i.status="Success"
                i.save()
                cl.save()
            else:
                i.status="Failed"
                i.WinAmount="0"
                i.save()    

    return redirect(StarlineDeclareResult)

def GaliGameStatus(request,pid):
    dt=GaliDesawarGame.objects.get(name=pid)
    if(dt.status == "open"):
        dt.status="close"
    else:
        dt.status="open"
    dt.save()
    return redirect(GaliDesawarMarket)

def WithdrawStatusApprove(request,pid):
    dt=Withdrawal.objects.get(txid=pid)
    dt.status="Success"
    dt.save()
    return redirect(UserMngPage)

def WithdrawStatusReject(request,pid):
    dt=Withdrawal.objects.get(txid=pid)
    dt.status="Reject"
    dt.save()
    return redirect(UserMngPage)


# holiday
def MarketHoliday(request,pid):
    dt=Games.objects.get(name=pid)
    dt.status="Today Holiday"
    dt.save()
    return redirect(marketgames)

def StarlineHoliday(request,pid):
    dt=StarlineGames.objects.get(name=pid)
    dt.status="Today Holiday"
    dt.save()
    return redirect(AdminStarlineGames)

def GaliHoliday(request,pid):
    dt=GaliDesawarGame.objects.get(name=pid)
    dt.status="Today Holiday"
    dt.save()
    return redirect(GaliDesawarMarket)


def EmailNotification(request):
    if request.method=="POST":
        Emailtitle=request.POST.get("Emailtitle")
        Emailmessage=request.POST.get("Emailmessage")

        cl=customer.objects.all().values()
        

    return redirect(NotificationMng)