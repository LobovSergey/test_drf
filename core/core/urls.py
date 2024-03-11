from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from organiztion.views import *
from events.views import *
from user.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(prefix="events", viewset=EventViewSet, basename='events')
router.register(prefix="organization", viewset=OrganizationCreateAPI)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", UserRegisterAPIView.as_view()),
    path("user/<int:pk>", UserRetrieveOptionsAPIViewSet.as_view(
        {"get": "retrieve", "put": "update", "delete": "destroy"})),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),


]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
