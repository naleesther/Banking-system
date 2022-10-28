from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewSet
from .views import WalletViewSet
 

router = routers.DefaultRouter()
router.register(r"customers",CustomerViewSet)
router.register(r"wallets",WalletViewSet)


urlpatterns = [
    path("",include(router.urls)),
]

