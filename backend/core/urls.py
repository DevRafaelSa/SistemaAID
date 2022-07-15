from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib import admin
from drf_yasg import openapi


# Schema view para Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# Rotas para Django Admin, API e AuthToken
urlpatterns = [
    path("admin/", admin.site.urls), # Django Admin
    path("api/v1/", include("api.urls", namespace="api")), # API
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")), # API Auth
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # AuthToken
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # TokenRefresh
]

# Rotas para Swagger 
urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
