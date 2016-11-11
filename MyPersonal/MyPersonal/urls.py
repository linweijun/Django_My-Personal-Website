"""MyPersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView, ShowPostsViews, ContactViews



urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^contact/',ContactViews.as_view(), name='contact'),
    url(r'^posts/(?P<slug>\w+)$', ShowPostsViews.as_view(), name='show'),
    url(r'^admin/', include('Admin.urls')),
    url(r'^uploads/',include('upload.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'MyPersonal.views.page_not_found_view'
handler403 = 'MyPersonal.views.permission_denied_view'
handler500 = 'MyPersonal.views.error_view'


