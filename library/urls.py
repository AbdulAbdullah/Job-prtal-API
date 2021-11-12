from library.views import ApplicationDetails, ApplicationList
from django.urls import path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'people', ApplicationDetails)
router.register(r'species', ApplicationList)


urlpatterns = [
    path('api/inventory/<int:pk>', ApplicationList.as_view()),
    path('api/inventory/<int:pk>', ApplicationDetails.as_view()),
    
]
