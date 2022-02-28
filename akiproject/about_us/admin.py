from django.contrib import admin
from .models import AboutUs, Founders, Reports, Supervisory, Advantages, Purpose, Documents


admin.site.register(AboutUs)
@admin.register(Advantages)
class AdvantagesAdmin(admin.ModelAdmin):
    list_display = ('subtitle', )


@admin.register(Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ('name', 'report_text', 'created_date', )
    save_on_top = True


admin.site.register(Supervisory)
admin.site.register(Founders)
admin.site.register(Purpose)
admin.site.register(Documents)