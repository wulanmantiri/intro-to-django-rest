from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()

    def get_location(self, obj):
        return f'{obj.city}, {obj.province}'

    class Meta:
        model = Candidate
        fields = [
            'id',
            'name',
            'job',
            'picture',
            'city',
            'province',
            'days_notice',
            'description',
            'updated_at',
            'location',
        ]
