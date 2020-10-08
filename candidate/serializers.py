from rest_framework import serializers
from .models import Candidate, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=True, read_only=True)
    location = serializers.SerializerMethodField()

    def get_location(self, obj):
        return f'{obj.city}, {obj.province}'

    class Meta:
        model = Candidate
        fields = [
            'id',
            'company',
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
