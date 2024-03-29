from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', 'myapp.views.index', name='index'),
    url(r'^registration/', 'myapp.views.registration', name='registration' ),
    url(r'^management/', 'myapp.views.management', name='management'),
    url(r'^bigdata/', 'myapp.views.bigdata', name='bigdata'),
    url(r'^index/', 'myapp.views.index', name='index'),
    url(r'^login/', 'myapp.views.login', name='login'),
    url(r'^pageLocations/', 'myapp.views.pageLocations', name='pageLocations'),
    url(r'^pageIoT/', 'myapp.views.pageIoT', name='pageIoT')
)
