# -*- coding:utf-8 -*-
from copy import deepcopy
from django.contrib.admin import helpers
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.conf import settings
#from core.models import INACTIVE
#from core.admin import activate, inactivate
from mezzanine.core.admin import DisplayableAdmin
from events.forms import EventForm, EventProgramationForm
from events.models import Event, EventProgramation



event_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
event_fieldsets[0][1]["fields"].extend([
    'event_title_menu','event_description_short',
    'event_logo', 'event_title', 'event_image_background', 'event_social_image',
    'information_active', 'information_title', 'information_text',
    'local_active', 'local_maps_name', 'local_title', 'local_text',
    'observation_active', 'observation_title', 'observation_text',
    'list_programations_active', 'list_programations_title',
    'list_events_active', 'list_events_title',
])

event_list_display = ["title", "status", "admin_link"]
#event_list_display.insert(0, "admin_thumb")


class EventAdmin(DisplayableAdmin):
    """
    Admin dos Eventos
    """
    form = EventProgramationForm
    fieldsets = event_fieldsets
    list_display = event_list_display
    #filter_horizontal = ("categories",)
    # inlines = [
    #     PersonLinkInline,
    # ]



class EventProgramationAdmin(admin.ModelAdmin):
    """
    Admin das Programacoes de Eventos
    """
    form = EventProgramationForm
    fieldsets = (
        (None, {
            "fields": ["name", "status", "image", "date_time", "content", "event" ],
        }),
    )
    list_display = ["name", "status", "get_event_url_edit"]
    list_display_links = ['name',]

admin.site.register(Event, EventAdmin)
admin.site.register(EventProgramation, EventProgramationAdmin)


# TODO: Antigos

# class EventProgramationInline(admin.TabularInline):
#     model = EventProgramation


# class EventAdmin(admin.ModelAdmin):
#     list_display = ('id', 'event_title_short', 'short_url', 'status', 'information_active', 'local_active', 'observation_active')
#     list_display_links = ('id', 'event_title_short', 'status',)
#     actions = ('duplicate_item',)
#
#     form = EventForm
#     # inlines = [EventProgramationInline, ]
#
#     def event_title_short(self, obj):
#         """
#         Retorna o titulo sem tags html para a exibição na listagem
#         """
#         return obj.__unicode__()
#     event_title_short.allow_tags = True
#     event_title_short.short_description = _(u"Título")
#
#     def duplicate_item(self, request, queryset):
#         if queryset.count() <> 1:
#             self.message_user(request, _(u"Selecione apenas 1 item para duplicar"), level=messages.ERROR)
#         else:
#             obj = queryset.get()
#             obj_new = obj.duplicate_save()
#             return HttpResponseRedirect(redirect_to=reverse('admin:events_event_change', args=(obj_new.id,)))
#     duplicate_item.short_description = _(u"Duplicar Item")
#
#
#     def link_url_event_preview(self, obj):
#         """
#         Cria link para pre-visualizar a pagina
#         """
#         return obj.get_link_preview()
#
#     link_url_event_preview.allow_tags = True
#     link_url_event_preview.short_description = _(u"Pré-visualização")


# class EventProgramationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'date_time', 'status', 'description_short', 'image_thumb')
#     # list_display_links = ('name',)
#     search_fields = ('name', 'description')
#     ordering = ('date_time', 'name', 'status', 'content')
#     list_filter = (
#         #('active', admin.ChoicesFieldListFilter),
#         'event',
#     )
#     #actions = [inactivate, activate, ]
#
#     def description_short(self, obj):
#         """
#         Corta o texto da Descrição para nao ficar exibir muito grande na listagem
#         """
#         text = strip_tags(obj.description)
#         if (len(text) > 80):
#             return "%s..." % text[0:80]
#         else:
#             return "%s" % text
#
#     def image_thumb(self, obj):
#         """
#         Exibe miniatura da imagem na listagem
#         """
#         return '<img src="%s%s" style="width:50px;">' % (settings.MEDIA_URL, obj.image)
#
#     image_thumb.allow_tags = True


#admin.site.register(Event, EventAdmin)
#admin.site.register(EventProgramation, EventProgramationAdmin)
