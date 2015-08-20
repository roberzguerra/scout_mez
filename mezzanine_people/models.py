# -*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.core.models import Displayable, RichText, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import AdminThumbMixin


class Person(Displayable, RichText, AdminThumbMixin):
    """
    A person.
    """

    categories = models.ManyToManyField("PersonCategory", verbose_name=_(u"Equipes"), blank=True,
        related_name="people")
    first_name = models.CharField(_(u"Primeiro Nome"), blank=True, max_length=100)
    last_name = models.CharField(_(u"Último Nome"), blank=True, max_length=100)
    mugshot = FileField(verbose_name=_(u"Imagem de Perfil"), upload_to="people", format="Image", max_length=255,
        null=True, blank=True)
    mugshot_credit = models.CharField(_(u"Imagem de Perfil (credit)"), blank=True, max_length=200)
    email = models.EmailField(_(u"E-mail"), blank=True)
    bio = RichTextField(_(u"Biografia"), help_text=_(u"Breve biografia da pessoa e/ou cargo."), default="", blank=True)
    job_title = models.CharField(_(u"Título do Cargo"), max_length=60, blank=True, help_text=_(u"Exemplo: Diretor Presidente"))
    order = models.PositiveSmallIntegerField(verbose_name=_(u"Ordem"), default=0)

    admin_thumb_field = "mugshot"
    search_fields = {"first_name", "last_name", "bio", "job_title",}

    class Meta:
        verbose_name = _(u"Pessoa")
        verbose_name_plural = _(u"Pessoas")
        ordering = ("order", "last_name", "first_name",)

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    @models.permalink
    def get_absolute_url(self):
        return ("person_detail", (), {"slug": self.slug})

class PersonLink(models.Model):
    """
    A link to a person's interesting URLs, such as Twitter or Facebook
    """
    name = models.CharField(_(u"Nome do Link"), max_length=50, help_text=_(u"Nome do link, ex: Twitter, Facebook..."))
    url = models.URLField(_(u"URL"))
    person = models.ForeignKey(Person)

    class Meta:
        verbose_name = _(u"Link da Pessoa")
        verbose_name_plural = _(u"Links da Pessoa")
        ordering = ('name',)

class PersonCategory(Slugged):
    """
    A category for grouping people.
    """

    class Meta:
        verbose_name = _(u"Equipe")
        verbose_name_plural = _(u"Equipes")

    @models.permalink
    def get_absolute_url(self):
        return ("person_list_category", (), {"slug": self.slug})
