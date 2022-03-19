from django.urls import include, path

from api_app.views import MoleculeViews, ActivityView

urlpatterns = [
    path('molecules', MoleculeViews.as_view()),
    path('molecules/<int:molecule_id>', MoleculeViews.as_view()),
    path('activity/<int:molecule_id>', ActivityView.as_view())
]
