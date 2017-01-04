from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/', views.login_photogram, name='login'),
    url(r'register/', views.register_pre, name='register'),
    url(r'register_post/', views.register_post, name='register_post'),
    url(r'logout/', views.logout_view, name='logout'),
    url(r'delete/', views.delete, name='delete'),
    url(r'edit/', views.edit, name='edit'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)