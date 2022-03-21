from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api_app.models import Molecule, Activity
from api_app.serializers import MoleculeSerializer, ActivitySerializer


@api_view(('GET',))
def molecule_view(request, molecule_id):
    try:
        molecule = Molecule.objects.get(id=molecule_id)
        serializer = MoleculeSerializer(molecule)

        return Response(serializer.data)
    except Molecule.DoesNotExist:
        return Response({"res": "Molecule does not exists"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
def molecule_all_view(request):
    item = Molecule.objects.all()

    page_size = request.query_params.get('page_size')
    paginator = get_paginator(page_size)
    result_page = paginator.paginate_queryset(item, request)
    serializer = MoleculeSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(('GET',))
def activity_view(request, molecule_id):
    item = Activity.objects.filter(molecule_id=molecule_id)

    page_size = request.query_params.get('page_size')
    paginator = get_paginator(page_size)
    result_page = paginator.paginate_queryset(item, request)
    serializer = ActivitySerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


# TODO: enhance this logic
def get_paginator(page_size):
    default_page_size = '10'
    max_page_size = 100

    page_size = page_size or default_page_size

    if str.isdigit(page_size):
        page_size = int(page_size)

        if page_size > max_page_size:
            page_size = max_page_size
    else:
        page_size = default_page_size

    paginator = PageNumberPagination()
    paginator.page_size = page_size

    return paginator
