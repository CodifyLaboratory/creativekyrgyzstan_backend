from django.contrib import admin
from django.forms import inlineformset_factory

# Register your models here.

from .models import Event, EventImages

# admin.site.register(Event)
# admin.site.register(EventImages)

class EventImagesAdmin(admin.StackedInline):    
    model = EventImages

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_filter = ('event_date',)
    search_fields = ('name',) 
    list_display = ('name', 'event_date',)
    inlines = [EventImagesAdmin]
    save_on_top = True 
    ordering = ('-event_date',)
    actions = ['publish', 'unpublish']



    def unpublish(self, request, queryset):
        """ снять с публикации """
        row_update = queryset.update(draft=True)
        if row_update == 1:
                message_bit = '1 запись была обновлена '
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')    


    def publish(self, request, queryset):
        """ опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
             message_bit = '1 запись была обновлена '
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')      

    publish.short_description = "опубликовать" 
    publish.allowed_permissions = ('change', )   

    unpublish.short_description = "снять с публикации" 
    unpublish.allowed_permissions = ('change', )   