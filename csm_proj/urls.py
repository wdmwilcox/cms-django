from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from csm_app.views import CompanyViewSet, PersonViewSet

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(f'person', PersonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
