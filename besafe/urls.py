"""
URL configuration for besafe project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from besafe import views
from inquiry.views import ConsultingFormView, PartnershipFormView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Index.as_view()),
    path("signin", views.Signin.as_view()),
    path("portfolio", views.Portfolio.as_view()),
    path("introduce", views.Introduce.as_view()),
    path("program", views.Program.as_view()),
    path("service", views.ServiceCenter.as_view()),
    path("subscription", views.Subscription.as_view()),
    path(
        "api/",
        include(
            [
                path("consulting", ConsultingFormView.as_view()),
                path("partnership", PartnershipFormView.as_view()),
            ]
        ),
    ),
    path("renew/", include("renew.urls")),
]
urlpatterns += staticfiles_urlpatterns()
