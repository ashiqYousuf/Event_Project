from myapp import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('<int:id>/' , views.liked_true,name="liked"),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
