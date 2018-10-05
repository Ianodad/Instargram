from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


# import welcome from views
from .views import home


urlpatterns = [
    url(r'^$', home),

]
