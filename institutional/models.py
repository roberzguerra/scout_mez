# -*- coding:utf-8 -*-
from django.shortcuts import get_object_or_404

from django.utils.translation import ugettext_lazy as _
from django.db import models

from mezzanine.pages.models import Page, RichText
from mezzanine.blog.models import BlogPost
from scout_group.models import ScoutGroup, District


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
        db_table = "institutional_team"
        verbose_name = _(u"Equipe")
        verbose_name_plural = _(u"Equipes")


class ScoutGroupPage(Page, RichText):
    """
    Pagina de Grupos Escoteiros
    """

    TYPE_GROUP_ALPHA = 1
    TYPE_GROUP_NUMBER = 2
    TYPE_GROUP_DISTRICT = 3
    TYPE_GROUP_ONLY_DISTRICT = 4

    TYPE_PAGE = (
        (TYPE_GROUP_ALPHA, _(u"Grupos em ordem Alfabética")),
        (TYPE_GROUP_NUMBER, _(u"Grupos por Númeral")),
        (TYPE_GROUP_DISTRICT, _(u"Grupos por Distritos")),
        (TYPE_GROUP_ONLY_DISTRICT, _(u"Somente Distritos")),
    )

    type = models.IntegerField(verbose_name=_(u"Tipo de Exibição"), choices=TYPE_PAGE, max_length=2,
        help_text=_(u"Tipo de exibição dos itens da página"))

    class Meta:
        db_table = "institutional_scout_group_page"
        verbose_name = _(u"Grupo | Distrito")
        verbose_name_plural = _(u"Grupos | Distritos")

    def get_scout_groups_type_alpha(self):
        """
        Retorna uma lista de Grupos escoteiros ordenados pelo nome
        """
        return ScoutGroup.objects.published().order_by('name')

    def get_scout_groups_type_number(self):
        """
        Retorna uma lista de Grupos escoteiros ordenados pelo Numeral
        """
        return ScoutGroup.objects.published().order_by('number')

    def get_scout_groups_type_district(self):
        """
        Retorna uma lista de Distritos
        """
        return District.objects.published().order_by('number')


# class Homepage(Page):
#     """
#
#     """
#     class Meta:
#         verbose_name = _(u"Homepage")
#         verbose_name_plural = _(u"Homepages")