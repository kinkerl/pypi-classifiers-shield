# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls
from core.views import image_redirect
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView


urlpatterns = [
    
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^image/(?P<project_name>[\w-]+)/(?P<classifier>[\w-]+)', image_redirect),
#     url(r'^.*$', RedirectView.as_view(url='https://heise.de', permanent=False), name='index')
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
