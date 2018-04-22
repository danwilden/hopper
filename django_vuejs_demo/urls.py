"""django_vuejs_demo URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.authtoken import views as rest_framework_views

from demoapp import views

urlpatterns = [
    url(r'^$', view=TemplateView.as_view(template_name='home.html')),
    url(r'^financials/$', view=TemplateView.as_view(template_name='financials.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^test/$', views.test),
    url(r'^business/$', views.business_list.as_view()),
    url(r'^business/(?P<pk>[0-9]+)$', views.business_detail.as_view()),
    url(r'^user/$', views.user_list.as_view()),
    url(r'^user/(?P<pk>[0-9]+)$', views.user_detail.as_view()),
    url(r'^contact/$', views.contact_list.as_view()),
    url(r'^contact/(?P<pk>[0-9]+)$', views.contact_detail.as_view()),
    url(r'^viewer/$', views.viewer_list.as_view()),
    url(r'^viewer/(?P<pk>[0-9]+)$', views.viewer_detail.as_view()),
    url(r'^listing/$', views.listing_list.as_view()),
    url(r'^listing/(?P<pk>[0-9]+)$', views.listing_detail.as_view()),
    url(r'^financial/$', views.financial_list.as_view()),
    url(r'^financial/(?P<pk>[0-9]+)$', views.financial_detail.as_view()),
    url(r'^datatype/$', views.datatype_list.as_view()),
    url(r'^datatype/(?P<pk>[0-9]+)$', views.datatype_detail.as_view()),
    url(r'^api-token-auth/', rest_framework_views.obtain_auth_token),
    url(r'^valuation/$', views.valuation_list.as_view()),
    # url(r'^families/(?P<pk>[0-9]+)$', views.family_detail.as_view()),
    # url(r'^locations/$', views.location_list.as_view()),
    # url(r'^locations/(?P<pk>[0-9]+)$', views.location_detail.as_view()),
    # url(r'^transactions/$', views.transaction_list.as_view()),
    # url(r'^transactions/(?P<pk>[0-9]+)$', views.transaction_detail.as_view()),
]
