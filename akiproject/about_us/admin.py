from django.contrib import admin
from .models import AboutUs, Founders, Reports, Supervisory, Advantages


class AdvantagesInline(admin.StackedInline):
    model = Advantages

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AdvantagesInline]


@admin.register(Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ('name', 'report_text', 'created_date', )
    save_on_top = True


admin.site.register(Supervisory)
admin.site.register(Founders)