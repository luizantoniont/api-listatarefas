
from django.contrib import admin
from django.urls import include, path
from listadetarefas.views import TarefasViewSet
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

schema_view = get_schema_view(
   openapi.Info(
      title="Gerenciador de Tarefas",
      default_version='v1',
      description="API Lista de Tarefas",
      terms_of_service="#",
      contact=openapi.Contact(email="admin@admin.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('tarefas', TarefasViewSet, basename='Tarefas')


urlpatterns = [

    path('controle/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
