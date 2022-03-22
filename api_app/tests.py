from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from api_app.models import Molecule
from api_app.serializers import MoleculeSerializer

client = Client()


class ApiAppTest(TestCase):
    def setUp(self):
        self.molecule1 = Molecule.objects.create(
            name='molecule1', max_phase=3, structure='structure1', inchi_key='key1')
        self.molecule2 = Molecule.objects.create(
            name='molecule2', max_phase=1, structure='structure2', inchi_key='key2')
        self.molecule3 = Molecule.objects.create(
            name='molecule3', max_phase=2, structure='structure3', inchi_key='key3')
        self.molecule4 = Molecule.objects.create(
            name='molecule4', max_phase=6, structure='structure4', inchi_key='key4')

    def test_should_get_valid_single_molecule_by_id(self):
        response = client.get(reverse('get_molecule_by_id', kwargs={'molecule_id': self.molecule1.pk}))

        molecule = Molecule.objects.get(id=self.molecule1.pk)
        serializer = MoleculeSerializer(molecule)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_should_not_get_single_molecule_for_invalid_id(self):
        response = client.get(
            reverse('get_molecule_by_id', kwargs={'molecule_id': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_should_get_all_molecules_paginated(self):
        response = client.get(reverse('get_all_molecules'), {'page_size': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['count'] == 4)
        self.assertTrue(len(response.data['results']) == 2)
