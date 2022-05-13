from django.conf import settings
from django.conf.urls.static import static
from send.views import ListCreateClientAPIView, RUDClientAPIView, DistributionListCreateAPIView
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from sms_send.yasg import swaggerurlpatterns as doc_urls


router = routers.DefaultRouter()
router.register(r'clients', ListCreateClientAPIView)
router.register(r'messages', RUDClientAPIView)
router.register(r'distribution', DistributionListCreateAPIView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include("rest_framework.urls", namespace="rest_framework")),

]

urlpatterns += doc_urls

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)