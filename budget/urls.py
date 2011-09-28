from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'budget.budgeting.views.home', name='home'),
    url(r'^transactions/recent$', 'budget.budgeting.views.view_transactions'),
    url(r'^accounts/', include('socialauth.urls')),
    url(r'^signin_complete$', 'socialauth.views.signin_complete'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
