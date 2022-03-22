from django.urls import path

from api_app.views import molecule_view, molecule_all_view, activity_view

urlpatterns = [
    path('molecules', molecule_all_view, name='get_all_molecules'),
    path('molecules/<int:molecule_id>', molecule_view, name='get_molecule_by_id'),
    path('activity/<int:molecule_id>', activity_view, name='get_activity_by_molecule_id')
]
