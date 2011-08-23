from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.views.generic.simple import redirect_to

from django.utils.translation import ugettext, ugettext_lazy as _

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#-- Reverse lazy Hack
#-- reverse_lazy will be integrated into Django 1.4
#-- https://code.djangoproject.com/changeset/16121
from django.utils.functional import lazy
from django.core.urlresolvers import reverse
from django.utils.translation import activate
reverse_lazy = lazy(reverse, str)

urlpatterns = patterns('',
    (r'^i18n/', include('django.conf.urls.i18n')),
    #(r'^$', redirect_to, {'url': reverse_lazy('homepage')}),
)

urlpatterns += i18n_patterns('',
    #url(r'^$', TemplateView.as_view(template_name='homepage.html'), {'title':_("homepage"),}, name='homepage'),
    url(_(r'^one/'), TemplateView.as_view(template_name='one.html'), {'title':_("one"),}, name='one'),
    url(_(r'^two/'), TemplateView.as_view(template_name='two.html'), {'title':_("two"),}, name='two'),
    url(_(r'^three/'), TemplateView.as_view(template_name='three.html'), {'title':_("three"),}, name='three'),
    url(r'^', TemplateView.as_view(template_name='homepage.html'), {'title':_("homepage"),}, name='homepage'),
)
