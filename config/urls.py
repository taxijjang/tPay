from django.conf import settings
import debug_toolbar

from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('product.urls')),
]
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

# swagger 정보 설정, 관련 엔드포인트 추가
# swagger 엔드포인트는 DEBUG Mode에서만 노출
schema_view = get_schema_view(
    openapi.Info(
        title="config coding test API",
        default_version='v1',
        description="안녕하세요 김택윤 입니다. config coding test API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gw9122@naver.com"),
        license=openapi.License(name="BSD License"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

if settings.DEBUG:
    urlpatterns += [
        path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]