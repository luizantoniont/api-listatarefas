
from django.contrib import admin
from django.urls import include, path
from listadetarefas.views import TarefasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tarefas', TarefasViewSet, basename='Tarefas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
