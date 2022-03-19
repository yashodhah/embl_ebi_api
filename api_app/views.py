from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from api_app.models import Molecule, Activity
from api_app.serializers import MoleculeSerializer, ActivitySerializer


class MoleculeViews(APIView):
    def get(self, request, molecule_id):
        item = Molecule.objects.get(id=molecule_id)
        serializer = MoleculeSerializer(item)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def get(self, request):
        item = Molecule.objects.all()

        paginator = PageNumberPagination()
        paginator.page_size = 10

        result_page = paginator.paginate_queryset(item, request)
        serializer = MoleculeSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)


class ActivityView(APIView):
    def get(self, request, molecule_id):
        item = Activity.objects.filter(molecule_id=molecule_id)

        paginator = PageNumberPagination()
        paginator.page_size = 10

        result_page = paginator.paginate_queryset(item, request)
        serializer = ActivitySerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)
