"""kuku URL Configuration
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
from my_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^function_view/', views.function_view),
    url(r'^class_based_view/', views.ExampleClassBased.as_view()),
    url(r'^Example/', views.Example_template, name='example_url'),
    url(r'^variable/', views.Example_template_Variable, name='variable_url'),
    url(r'^groups/', views.GroupsView.as_view(), name='groups'),
    url(r'^group/(?P<id>\d+)', views.GroupView.as_view(), name='group'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
