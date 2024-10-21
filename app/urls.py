
from django.contrib import admin
from django.urls import path
from app import views
from adminpanel import views as adminpnl

urlpatterns = [
   path('',views.index,name="register page"),
   path('loginpg',views.loginpg,name="loginpg page"),
   path('forgetpassword',views.forgetpassword,name="forget-password page"),
   path('createAc',views.createAc,name="create account"),
   path('loginuser',views.loginuser,name="login account"),
   path('games',views.games,name="games page"),
   path('addfunds',views.addfunds,name="addfunds page"),
   path('withdrawal',views.withdrawal,name="withdrawal page"),
   path('starlines',views.starlines,name="starlines page"),
   path('myprofile',views.myprofile,name="myprofile page"),
   path('Elogout',views.Elogout,name="Elogout page"),
   path('privacypolicy',views.privacypolicy,name="privacypolicy page"),
   path('howtoplay',views.howtoplay,name="howtoplay page"),
   path('gameprice',views.gameprice,name="gameprice page"),
   path('payment',views.payment,name="payment page"),
   path('history',views.history,name="history page"),
   path('bid-history',views.BidHistory,name="BidHistory page"),
   path('bidwinhistory',views.bidwinhistory,name="bidwinhistory page"),
   path('passbook',views.passbook,name="passbook page"),
   path('DepositHistory',views.DepositHistory,name="DepositHistory page"),
   path('starline-bid-history',views.StarlineBidHistory,name="StarlineBidHistory page"),
   path('StarlineWinHistory',views.StarlineWinHistory,name="StarlineWinHistory page"),
   path('gali-bid-history',views.GaliBidHistory,name="gali-bid-history page"),
   path('update_profile',views.updateprofile,name="updateprofile page"),
   path('update_paymentInfo',views.updatepaymentInfo,name="updatepaymentInfo page"),
   path('withdrawal_ammount',views.withdrawalammount,name="withdrawalammount page"),
   path('UserDeposit',views.UserDeposit,name="UserDeposit page"),
   path('gametype<str:pid>',views.gametype,name="gametype page"),
   path('CloseGame<str:pid>',views.CloseGame,name="CloseGame url"),
   path('CloseGameStarline<str:pid>',views.CloseGameStarline,name="CloseGameStarline url"),
   path('OpenGame',views.OpenGame,name="OpenGame "),
   path('GaliDesawarPage',views.GaliDesawarPage,name="GaliDesawarPage "),

   path('SingleAnk<str:pid>',views.SingleAnk,name="SingleAnk page"),
   path('jodi<str:pid>',views.jodi,name="jodi page"),
   path('SinglePatti<str:pid>',views.SinglePatti,name="SinglePatti page"),
   path('DoublePatti<str:pid>',views.DoublePatti,name="DoublePatti page"),
   path('TripplePatti<str:pid>',views.TripplePatti,name="TripplePatti page"),
   path('HalfSangam<str:pid>',views.HalfSangam,name="HalfSangam page"),
   path('FullSangam<str:pid>',views.FullSangam,name="FullSangam page"),
   path('SpMotor<str:pid>',views.SpMotor,name="SpMotor page"),
   path('DpMotor<str:pid>',views.DpMotor,name="DpMotor page"),

   path('singlebet',views.singlebet,name="singlebet data"),
   path('spmotarbet',views.spmotarbet,name="spmotarbet data"),
   path('sangambet',views.sangambet,name="sangambet data"),
   path('fullsangam', views.fullsangam, name='full sangam'),

   path('starlinegametype<str:pid>',views.starlinegametype,name="starlinegametype page"),
   path('StarlineSingleAnk<str:pid>',views.StarlineSingleAnk,name="SingleAnk page"),
   path('StarlineSinglePatti<str:pid>',views.StarlineSinglePatti,name="SinglePatti page"),
   path('StarlineDoublePatti<str:pid>',views.StarlineDoublePatti,name="Double page"),
   path('StarlineTripplePatti<str:pid>',views.StarlineTripplePatti,name="Triple page"),

   path('StarlineSinglebet',views.StarlineSinglebet,name="StarlineSinglebet data"),

   
   path('GaliGameType<str:pid>',views.GaliGameType,name="GaliGameType page"),
   path('GaliJodi<str:pid>',views.GaliJodi,name="GaliJodi page"),
   path('GaliJodiBet',views.GaliJodiBet,name="GaliJodiBet data"),










   # adminpanel section start
    path('adminloginpage',adminpnl.adminloginpage,name="adminlogin page"),
    path('adminlogin',adminpnl.adminlogin,name="adminlogin"),
    path('adminhome',adminpnl.adminhome,name="adminhome page"),
    path('UserMngPage',adminpnl.UserMngPage,name="UserMngPage page"),
    path('marketgames',adminpnl.marketgames,name="marketgames page"),
    path('UpdateGameRates',adminpnl.UpdateGameRates,name="UpdateGameRates page"),
    path('AdminStarlineGames',adminpnl.AdminStarlineGames,name="AdminStarlineGames page"),
    path('AdminUsers',adminpnl.AdminUsers,name="AdminUsers page"),
    path('Support',adminpnl.Support,name="Support page"),
    path('Mode',adminpnl.Mode,name="Mode page"),
    path('UserProfile<str:pid>',adminpnl.UserProfile,name="UserProfile page"),
    path('UpdateSupport',adminpnl.UpdateSupport,name="UpdateSupport page"),
    path('AdminHowPlay',adminpnl.AdminHowPlay,name="AdminHowPlay page"),
    path('AdminPswCng',adminpnl.AdminPswChange,name="AdminPswChange post"),
    path('AdminPswChange',adminpnl.AdminPswCng,name="AdminPswCng page"),
    path('changemode<str:pid>',adminpnl.changemode,name="changemode page"),
    path('Userdelete<str:pid>',adminpnl.Userdelete,name="Userdelete page"),
    path('UserDeactive<str:pid>',adminpnl.UserDeactive,name="UserDeactive page"),
    path('Admindelete<str:pid>',adminpnl.Admindelete,name="Admindelete page"),
    path('AdminMarketBids',adminpnl.AdminMarketBids,name="AdminMarketBids page"),
    path('AdminStarlineBids',adminpnl.AdminStarlineBids,name="AdminStarlineBids page"),
    path('UpdateGamePlay',adminpnl.UpdateGamePlay,name="UpdateGamePlay page"),
    path('AdminGameRates',adminpnl.AdminGameRates,name="AdminGameRates page"),
    path('AdminWithdraw',adminpnl.AdminWithdraw,name="AdminWithdraw page"),
    path('NotificationMng',adminpnl.NotificationMng,name="NotificationMng page"),
    path('UpdateNotification',adminpnl.UpdateNotification,name="UpdateNotification page"),
    path('EmailNotification',adminpnl.EmailNotification,name="EmailNotification page"),
    path('AdminAddGame',adminpnl.AdminAddGame,name="AdminAddGame page"),
    path('DeclareResPg',adminpnl.DeclareResPg,name="DeclareResPg page"),
    path('DeclareResult',adminpnl.DeclareResult,name="DeclareResult Post"),
    path('DepositRequestPg',adminpnl.DepositRequestPg,name="DepositRequest Post"),
    path('add-points-user-wallet',adminpnl.AppPointPage,name="AppPointPage Post"),
    path('AdminAddPoint',adminpnl.AdminAddPoint,name="AdminAddPoint Post"),
    path('AdminWithdrawalPoint',adminpnl.AdminWithdrawalPoint,name="AdminWithdrawalPoint Post"),
    path('starline-declare-result',adminpnl.StarlineDeclareResult,name="StarlineDeclareResult Post"),
    path('galidisawar-market-list',adminpnl.GaliDesawarMarket,name="GaliDesawarMarket Post"),
    path('galidisawer_bid_history',adminpnl.GaliDesawarBids,name="GaliDesawarBids Post"),
    path('galidisawer-declare-result',adminpnl.GaliDesawarResult,name="GaliDesawarResult Post"),
    path('winning-details',adminpnl.WiningDetails,name="WiningDetails Page"),
    path('GameDelete<str:pid>',adminpnl.GameDelete,name="GameDelete page"),
    path('MarketGameStatus<str:pid>',adminpnl.MarketGameStatus,name="MarketGameStatus page"),
    path('ViewWithdrawal',adminpnl.ViewWithdrawal,name="ViewWithdrawal page"),
    path('WithdrawStatusApprove<str:pid>',adminpnl.WithdrawStatusApprove,name="WithdrawStatusApprove page"),
    path('WithdrawStatusReject<str:pid>',adminpnl.WithdrawStatusReject,name="WithdrawStatusReject page"),


    path('BidUpdate',adminpnl.BidUpdate,name="BidUpdate page"),
    path('MarketResultDelete',adminpnl.MarketResultDelete,name="MarketResultDelete page"),
    path('StarlineResultDelete',adminpnl.StarlineResultDelete,name="StarlineResultDelete page"),
    path('GaliResultDelete',adminpnl.GaliResultDelete,name="GaliResultDelete page"),

    path('DepositReject/<str:pid>/<str:utr>',adminpnl.DepositReject,name="DepositReject Url"),
    path('DepositApprove/<str:pid>/<str:utr>',adminpnl.DepositApprove,name="DepositApprove Url"),

   #  starline
    path('StarlineBidUpdate',adminpnl.StarlineBidUpdate,name="StarlineBidUpdate page"),
    path('StarlineGameDelete<str:pid>',adminpnl.StarlineGameDelete,name="StarlineGameDelete page"),
    path('StarlineGameAdd',adminpnl.StarlineGameAdd,name="StarlineGameAdd page"),
    path('StarlineGameStatus<str:pid>',adminpnl.StarlineGameStatus,name="StarlineGameStatus page"),
    path('DeclareStarlineResult',adminpnl.DeclareStarlineResult,name="DeclareStarlineResult "),

   #  Gali Desawar
    path('GaliGameDelete<str:pid>',adminpnl.GaliGameDelete,name="GaliGameDelete page"),
    path('GaliGameAdd',adminpnl.GaliGameAdd,name="GaliGameAdd page"),
    path('DeclareGaliResult',adminpnl.DeclareGaliResult,name="DeclareGaliResult "),
    path('GaliGameStatus<str:pid>',adminpnl.GaliGameStatus,name="GaliGameStatus page"),

   #  holiday
    path('MarketHoliday<str:pid>',adminpnl.MarketHoliday,name="MarketHoliday page"),
    path('StarlineHoliday<str:pid>',adminpnl.StarlineHoliday,name="StarlineHoliday page"),
    path('GaliHoliday<str:pid>',adminpnl.GaliHoliday,name="GaliHoliday page"),

   #  declare result show winner
    path('ShowWinnerTable',adminpnl.ShowWinnerTable,name="ShowWinnerTable "),

   # adminpanel section end
]
