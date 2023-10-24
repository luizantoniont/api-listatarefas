
from django.contrib import admin
from django.urls import include, path
from listadetarefas.views import TarefasViewSet
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = routers.DefaultRouter()
router.register('tarefas', TarefasViewSet, basename='Tarefas')


urlpatterns = [
    
    path('controle/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
