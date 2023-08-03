from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_all/", views.get_all, name="get_all"),
    path("create/", views.create, name="create"),
    path("query/", views.query, name="query"),
    path("get_history/", views.get_history, name="get_history"),
    path("clear_history/", views.clear_history, name="clear_history"),
    path("change/", views.change, name="change")
]
