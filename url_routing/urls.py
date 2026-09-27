from django.urls import path

from . import views

app_name = 'url_routing'
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("articles/<int:year>/", views.article, name="article"),
    path("methods/", views.methods, name="methods"),
    path("form/", views.form, name="form-demo"),
]