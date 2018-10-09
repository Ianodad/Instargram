from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

# from . import views
# import welcome from views
from .views import home, profile


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^profile$', profile, name='profile')
]
