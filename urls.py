from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^', include('i18ndemo.urls')),
)