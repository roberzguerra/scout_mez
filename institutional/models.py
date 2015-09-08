# -*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models

from mezzanine.pages.models import Page, RichText
from mezzanine.blog.models import BlogPost


class BlogPostExtend:
    """
    Alteracoes no model BlogPost
    """
    def publish_date_post(self):
        return self.publish_date.strftime("Publicado em %d/%m/%Y às %H:%M")

    def publish_date_post_list(self):
        return self.publish_date.strftime("%d/%m/%Y às %H:%M")

BlogPost.__bases__ += (BlogPostExtend,)


class Team(Page, RichText):
    """
    Pagina de Equipes
    """
    categories = models.ManyToManyField("mezzanine_people.PersonCategory", verbose_name=_(u"Equipes"), blank=True,
        related_name="people_category", help_text=_(u"Selecione as equipes para exibir na página."))

    class Meta:
        verbose_name = _(u"Equipe")
        verbose_name_plural = _(u"Equipes")



# class Homepage(Page):
#     """
#
#     """
#     class Meta:
#         verbose_name = _(u"Homepage")
#         verbose_name_plural = _(u"Homepages")