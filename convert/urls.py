
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import UserViewSet
from converts.views import ConvertViewSet, ClearViewSet

router_user = DefaultRouter()
router_user.register('', UserViewSet, basename='user')
router_convert = DefaultRouter()
router_convert.register('', ConvertViewSet, basename='convert')
router_clear = DefaultRouter()
router_clear.register('', ClearViewSet, basename='clear')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(router_user.urls)),
    path('converts/', include(router_convert.urls)),
    path('clear/', include(router_clear.urls)),
    
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

