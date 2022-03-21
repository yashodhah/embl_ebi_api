from django.urls import path

from api_app.views import molecule_view, molecule_all_view, activity_view

urlpatterns = [
    path('molecules', molecule_all_view),
    path('molecules/<int:molecule_id>', molecule_view),
    path('activity/<int:molecule_id>', activity_view)
]
