from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path("view/<str:page>", views.page, name="page"),
    path("create", views.create , name="create")
]
