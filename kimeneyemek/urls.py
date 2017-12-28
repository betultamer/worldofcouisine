"""kimeneyemek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^tarif/', views.tarif_page, name='tarif'),
    url(r'^category/(?P<cat>.+)', views.cat_page, name='category'),
    url(r'^cuisine/(?P<name>.+)/(?P<cuisine_id>[0-9]+)', views.cuisine_page, name='cuisine'),
    url(r'^(?P<title>.+)/(?P<food_id>[0-9]+)', views.food_page, name='food'),
    url(r'^test_forms/', views.test_forms),
]
urlpatterns += [
url(r'^home/$', views.index, name='index'),

]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
