from django.contrib import admin
from .models import RulesAndPolitics, Members


admin.site.register(RulesAndPolitics)
class MembersAdmin(admin.ModelAdmin):
    search_fields = ('submit__full_name',)


    


admin.site.register(Members, MembersAdmin)
