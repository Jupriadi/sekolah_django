
from django.contrib import admin
from django.urls import path, include

from . import views
from blog import views as blogViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('blog/', blogViews.index),
    path('panel/', include('panel.urls'))
]
