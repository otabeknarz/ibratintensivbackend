from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("stats/", views.stats),
    path("add/", views.add_people),
    path("add-tg-people/", views.add_tg_people),
    path("get-tg-people/<str:id>/", views.get_tg_people),
    path("invite-tg-friend/", views.invite_tg_people),
    path("get-people-ids/", views.get_people_ids),
    path("has-invited-people-ids/", views.has_invited_people_ids),
    path("set-true-10/", views.set_true_10),
]
