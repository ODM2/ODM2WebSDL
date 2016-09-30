"""WebSDL URL Configuration

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
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView

from dataloader.models import Organization
from dataloaderinterface.forms import UserRegistrationForm
from dataloaderinterface.views import OrganizationAutocomplete

BASE_URL = settings.SITE_URL[1:]

login_configuration = {
    'redirect_field_name': 'next'
}

logout_configuration = {
    'next_page': reverse_lazy('home')
}

urlpatterns = [
    url(r'^' + BASE_URL + 'admin/', admin.site.urls),
    url(r'^' + BASE_URL + 'login/$', auth_views.login, login_configuration, name='login'),
    url(r'^' + BASE_URL + 'logout/$', auth_views.logout, logout_configuration, name='logout'),
    url(r'^' + BASE_URL + 'register/$', CreateView.as_view(template_name='registration/register.html', form_class=UserRegistrationForm, success_url=reverse_lazy('home')), name='user_registration'),
    url(r'^' + BASE_URL + 'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(BASE_URL, include('dataloaderinterface.urls')),
    url(BASE_URL, include('dataloaderservices.urls')),
    url(r'^organization-autocomplete/$', OrganizationAutocomplete.as_view(model=Organization, create_field='organization_name'), name='organization-autocomplete')
]
