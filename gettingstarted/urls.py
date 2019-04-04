from django.urls import path, re_path, include

from django.contrib import admin

from django.conf.urls import url
from django.contrib.auth import views as auth_views


admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    #re_path(r'^login/$', auth_views.LoginView, {'template_name': 'login.html'}, name='login'),
    #re_path(r'^logout/$', auth_views.LogoutView, name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
