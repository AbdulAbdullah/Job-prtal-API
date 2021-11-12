from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from library.views import JobList, ApplicationList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('jobs', JobList)
router.register('applications', ApplicationList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
]
