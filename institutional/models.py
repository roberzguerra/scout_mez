# -*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
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


# class Homepage(Page):
#     """
#
#     """
#     class Meta:
#         verbose_name = _(u"Homepage")
#         verbose_name_plural = _(u"Homepages")