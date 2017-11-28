"""engrProbSolving URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from collection import views

urlpatterns = [
    url(r'^$', views.index_engr1102, name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about_engr1102.html'),
        name='about'),
    url(r'^contact/$',
        TemplateView.as_view(template_name='contact_engr1102.html'),
        name='contact'),
    url(r'^projects/$',
        TemplateView.as_view(template_name='our_projects.html'),
        name='projects'),
    url(r'^projects/$',
        TemplateView.as_view(template_name = 'for_loops.html'),
        name = 'forloops'), 
    url(r'^projects/(?P<slug>[-\w]+)/$', views.project_detail,
        name='project_detail'),
    url(r'^projects/(?P<slug>[-\w]+)/edit/$',
        views.edit_project, name='edit_project'),
    url(r'^admin/', admin.site.urls),
]
