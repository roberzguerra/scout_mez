# -*- coding:utf-8 -*-
from django.contrib.sites.models import Site
from django.shortcuts import get_object_or_404

from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import register_setting

register_setting(
    name="HOME_PAGE_SITE",
    label=_(u"Página Inicial do Site"),
    description=_(u"URL da Página, deve ser o que está no campo 'URL' no bloco 'Metadado' do Cadastro de Páginas."),
    editable=True,
    default='',

)
