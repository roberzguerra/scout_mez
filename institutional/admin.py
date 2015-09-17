# -*- coding:utf-8 -*-

from django.contrib import admin

from mezzanine.conf import settings
from mezzanine.pages.admin import PageAdmin

from models import Team, ScoutGroupPage


class TeamAdmin(PageAdmin):
    """
    Admin para a Pagina de Equipes
    """

    #fieldsets = ((None, {"fields": ("title",)}),)

    # def in_menu(self):
    #     """
    #     Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
    #     """
    #     for (name, items) in settings.ADMIN_MENU_ORDER:
    #         if "people.PersonCategory" in items:
    #             return True
    #     return False

class ScoutGroupPageAdmin(PageAdmin):
    """
    Admin para a Pagina de Grupos e Distritos
    """

admin.site.register(Team, TeamAdmin)
admin.site.register(ScoutGroupPage, ScoutGroupPageAdmin)
