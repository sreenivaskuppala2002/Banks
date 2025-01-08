from rest_framework.serializers import ModelSerializer
from . models import Banks,Branch

class BranchSerializer(ModelSerializer):
    class Meta:
        model=Branch
        fields=['branch','IFSC']


class BankSerializer(ModelSerializer):
    branches=BranchSerializer(many=True)
    class Meta:
        model=Banks
        fields=['bank_name','branches']

