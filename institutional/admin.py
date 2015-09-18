# -*- coding:utf-8 -*-
from copy import deepcopy

from django.contrib import admin

from mezzanine.conf import settings
from mezzanine.pages.admin import PageAdmin

from models import Team, ScoutGroupPage
from scout_core.admin import page_fieldsets

team_fields = deepcopy(page_fieldsets)
team_fields[0][1]["fields"].insert(5, u"categories")


class TeamAdmin(PageAdmin):
    """
    Admin para a Pagina de Equipes
    """

    fieldsets = team_fields

    #fieldsets = ((None, {"fields": ("title",)}),)

    # def in_menu(self):
    #     """
    #     Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
    #     """
    #     for (name, items) in settings.ADMIN_MENU_ORDER:
    #         if "people.PersonCategory" in items:
    #             return True
    #     return False

scout_core_page_fields = deepcopy(page_fieldsets)
scout_core_page_fields[0][1]["fields"].insert(5, u"type")

class ScoutGroupPageAdmin(PageAdmin):
    """
    Admin para a Pagina de Grupos e Distritos
    """
    fieldsets = scout_core_page_fields


admin.site.register(Team, TeamAdmin)
admin.site.register(ScoutGroupPage, ScoutGroupPageAdmin)
