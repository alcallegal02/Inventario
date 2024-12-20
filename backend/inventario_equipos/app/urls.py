from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import NaveViewSet, DepartamentoViewSet, TrabajadorViewSet, EquipoViewSet, ImpresoraViewSet

# Configuración del router para las vistas basadas en ViewSets
router = DefaultRouter()
router.register(r'naves', NaveViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'trabajadores', TrabajadorViewSet)
router.register(r'equipos', EquipoViewSet)
router.register(r'impresoras', ImpresoraViewSet)

# Configuración de las rutas
urlpatterns = [
    # Rutas para autenticación JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Añadir las rutas del router a las rutas principales
urlpatterns += router.urls
