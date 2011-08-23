from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'', include('django_project_i18n_demo.i18ndemo.urls')),
)