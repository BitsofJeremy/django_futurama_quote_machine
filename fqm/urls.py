from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
# from api import views as api_views
from frontend import views as fe_views

router = routers.DefaultRouter()
# router.register(r'users', api_views.UserViewSet)
# router.register(r'groups', api_views.GroupViewSet)
router.register(r'characters', fe_views.CharacterViewSet)
router.register(r'quotes', fe_views.QuoteViewSet)

urlpatterns = [
    # Set the main route to frontend
    path('', include('frontend.urls')),
    # Set the admin route
    path('admin/', admin.site.urls),
    # API stuff
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
