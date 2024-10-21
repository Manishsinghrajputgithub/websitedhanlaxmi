from django.contrib import admin
from adminpanel.models import * 

# Register your models here.
admin.site.register(AdminUser)
admin.site.register(HowPlayGame)
admin.site.register(GameRates)
admin.site.register(Notice)