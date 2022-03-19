from rest_framework import serializers

from api_app.models import Molecule, Activity


class MoleculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Molecule
        fields = [
            'id',
            'name',
            'max_phase',
            'structure',
            'inchi_key'
        ]


class ActivitySerializer(serializers.ModelSerializer):
    target_name = serializers.ReadOnlyField(source='target.name')
    target_organism = serializers.ReadOnlyField(source='target.organism')

    class Meta:
        model = Activity
        fields = [
            'type',
            'units',
            'value',
            'relation',
            'target_name',
            'target_organism'
        ]
