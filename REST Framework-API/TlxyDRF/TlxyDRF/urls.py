from django.conf.urls import include, url
from django.contrib import admin
# 导入路由
from rest_framework import  routers
from case01 import views
router = routers.SimpleRouter()

router.register(r'student', views.StudentVS)
urlpatterns = [
    # Examples:
    # url(r'^$', 'TlxyDRF.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # 需要把drf路由当做子路由 配置好
    url(r'^api/', include(router.urls)),
]
