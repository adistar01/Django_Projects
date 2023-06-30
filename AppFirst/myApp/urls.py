from django.urls import path
from . import views

urlpatterns = [
    path('', views.myfunctioncall, name='index'),
    path('about', views.myfunctionabout, name='about'),
    path('add/<int:a>/<int:b>', views.myfunctionadd, name='add'),
    path('page', views.myhtmpage, name='htmlpage'),
    path('secpage', views.secpage, name='sechtm'),
    path('thirdpage', views.thirdpage, name='thirdhtm'),
    path('imgpg', views.imgpg, name='imagepage'),
    path('myform', views.myform, name='myform')
]