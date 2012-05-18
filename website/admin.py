from django.contrib import admin
from website.models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'nome', 'company', 'location','projetos','linguagens', 'link', 'contactado', 'iniciado', 'aprovado')
    list_filter = ['location','company']
    search_fields = ['username', 'nome', 'location','linguagens']


class AccountAdmin(admin.ModelAdmin):
    search_fields = ['username',]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Account, AccountAdmin)