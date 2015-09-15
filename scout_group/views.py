# -*- coding:utf-8 -*-

from django.shortcuts import get_object_or_404
from mezzanine.utils.views import render, paginate
from scout_group.models import ScoutGroup, District


def district(request, slug, template="mezzanine_people/person_detail.html"):
    """
    Custom templates are checked for using the name
    ``mezzanine_people/person_detail_XXX.html`` where ``XXX`` is the
    person's slug.
    """
    scout_group = get_object_or_404(District.objects.published(), slug=slug)
    context = {"scout_group": scout_group, "editable_obj": scout_group}
    templates = [u"mezzanine_people/person_detail_%s.html" % unicode(slug), template]
    return render(request, templates, context)


def scout_group(request, slug,
                  template="mezzanine_people/person_detail.html"):
    """
    Custom templates are checked for using the name
    ``mezzanine_people/person_detail_XXX.html`` where ``XXX`` is the
    person's slug.
    """
    scout_group = ScoutGroup.objects.published()
    person = get_object_or_404(scout_group, slug=slug)
    context = {"person": person, "editable_obj": person}
    templates = [u"mezzanine_people/person_detail_%s.html" % unicode(slug), template]
    return render(request, templates, context)
