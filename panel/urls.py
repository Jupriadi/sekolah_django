from django.urls import path
from . import views
from . import siswaviews

urlpatterns = [
    path('',views.index),
    path('profsek/',views.profsek),
    path('editprofsek/',views.editprofsek),
    path('guru/',views.guru),
    path('tambahguru/',views.tambahguru),
    path('editguru/<int:id>',views.editguru),
    path('hapusguru/<int:id>',views.hapusguru),
    path('siswa/', siswaviews.index)
] 