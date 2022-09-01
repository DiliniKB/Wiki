from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path("view/<str:page>", views.page, name="page"),
    path("create", views.create , name="create"),
    path("random", views.randomP , name="random"),
    path("edit/<str:page>", views.editP , name="edit")
]
