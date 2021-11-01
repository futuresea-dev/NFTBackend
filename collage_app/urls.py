from django.urls import path, include
from collage_app import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'serie', views.SeriedToken)
urlpatterns = router.urls

urlpatterns += [
    path('main-page/', views.TokenList.as_view(), name='home')
]