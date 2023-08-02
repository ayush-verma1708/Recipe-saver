from django.contrib import admin
from django.urls import include ,path 
from home.views import *
from vege.views import *

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('recipe/', recipes , name = "recipe"),

    path('delete-recipe/<id>/',delete_recipe,name="delete-recipe"),
    path('update-recipe/<id>/',update_recipe,name="update-recipe"),

    path('', home, name ="home"),
    path('contact/', contact, name ="contact"),
    path('about/', about, name ="about"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)