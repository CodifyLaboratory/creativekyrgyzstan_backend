from django.contrib import admin


from .models import AboutUs, Reports, Supervisory

admin.site.register(AboutUs)

@admin.register(Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ('name', 'report_text', 'created_date', )
    save_on_top = True


admin.site.register(Supervisory)