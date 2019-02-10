from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
                  path('@ad@m~in/', admin.site.urls),
                  path('', views.index, name='index'),
                  path('about/', views.About, name='about'),
                  re_path(r'^post/(?P<pk>[0-9]+)/$', views.PostView, name='post_detail'),
                  path('contact/', views.ContactUs, name='ContactUs'),
                  re_path(r'^languages/(?P<pk>[0-9]+)/$', views.Languages, name='languages'),
                  re_path(r'^alogorithms/(?P<pk>[0-9]+)/$', views.dataAL, name='alogorithms')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
