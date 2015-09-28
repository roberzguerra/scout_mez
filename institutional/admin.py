# -*- coding:utf-8 -*-
from copy import deepcopy

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django import forms

from mezzanine.conf import settings
from mezzanine.blog.models import BlogPost
from mezzanine.forms.admin import FormAdmin
from mezzanine.galleries.admin import GalleryAdmin
from mezzanine.pages.models import Page
from mezzanine.core.admin import DisplayableAdminForm, DisplayableAdmin, TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from mezzanine.blog.admin import BlogPostAdmin

from models import Team, ScoutGroupPage, HomePage, Slide, SocialLinks
from scout_core.admin import page_fieldsets


class BlogPostAdminForm(DisplayableAdminForm):
    """
    Form customizado para o BlogPost

    Seta o atributo "Exibir no sitemap" como False e não obrigatorio
    """
    in_sitemap = forms.BooleanField(label=_(u"Show in sitemap"), required=False, initial=False)

BlogPostAdmin.form = BlogPostAdminForm
admin.site.unregister(BlogPost)
admin.site.register(BlogPost, BlogPostAdmin)


class PageAdminForm(DisplayableAdminForm):
    """
    Form customizado para Paginas do Site

    Seta o atributo "Exibir no sitemap" como False e não obrigatorio
    """
    in_sitemap = forms.BooleanField(label=_(u"Show in sitemap"), required=False, initial=False)


PageAdmin.form = PageAdminForm
admin.site.unregister(Page)
admin.site.register(Page, PageAdmin)

class SocialLinkInline(TabularDynamicInlineAdmin):
    model = SocialLinks


class SlideInline(TabularDynamicInlineAdmin):
    model = Slide


class HomePageAdmin(PageAdmin):
    """
    Admin para a HomePage
     """
    filter_horizontal = ("blog_posts", "teams", )
    inlines = [SlideInline, SocialLinkInline, ]

admin.site.register(HomePage, HomePageAdmin)
# admin_classes_with_slides = [HomePageAdmin, ] #FormAdmin, GalleryAdmin]
# for admin_class in admin_classes_with_slides:
#     setattr(admin_class, 'inlines', list(admin_class.inlines) + [SlideInline])



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
