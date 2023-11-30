"""
URL configuration for myFuckingP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.conf import settings

admin_urls = [
    path('admin/user/',
         include(('user.urls.admin', 'muFuckingP.user'), namespace='users-admin')),
    path('admin/media/',
         include(('media.urls.admin', 'muFuckingP.media'), namespace='media-admin')),
    path('admin/services/',
         include(('service.urls.admin', 'muFuckingP.service'), namespace='service-admin')),
    path('admin/article/',
         include(('article.urls.admin', 'muFuckingP.article'), namespace='article-admin')),
    path('admin/order/',
         include(('order.urls.admin', 'muFuckingP.order'), namespace='order-admin')),

]

front_urls = [
    path('front/user/',
         include(('user.urls.front', 'muFuckingP.user'), namespace='users-front')),
    path('front/media/',
         include(('media.urls.front', 'muFuckingP.media'), namespace='media-front')),
    path('front/service/',
         include(('service.urls.front', 'muFuckingP.service'), namespace='service-front')),
    path('front/article/',
         include(('article.urls.front', 'muFuckingP.article'), namespace='article-front')),
    path('front/order/',
         include(('order.urls.front', 'muFuckingP.order'), namespace='order-front')),

]

doc_patterns = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = [
                  path("akm/", admin.site.urls),
              ] + front_urls + admin_urls + doc_patterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
