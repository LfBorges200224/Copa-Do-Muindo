from django.urls import path
from .views import TeamView
from .views import TeamParamsView

urlpatterns = [
    path('teams/', TeamView.as_view()),
    path("teams/<int:team_id>/", TeamParamsView.as_view()),
]