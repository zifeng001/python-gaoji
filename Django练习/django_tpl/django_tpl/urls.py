from django.conf.urls import include, url
from django.contrib import admin

from mytpl import views as v
urlpatterns = [
    # Examples:
    # url(r'^$', 'django_tpl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^oneve/', v.one,),
    url(r'^twowo/', v.two),
    url(r'^three/', v.three),
    url(r'^four/', v.four),
    url(r'^five_get/', v.five_get),
    url(r'^five_post/', v.five_post),

]
