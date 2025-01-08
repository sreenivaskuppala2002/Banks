from django.shortcuts import render
from django.http import HttpResponse
from . serializers import BankSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Banks

# Create your views here.
def endpoints(request):
    return HttpResponse("use '/banklist' endpoint to get bank list")

#view to get all bank details with specific branch details
@api_view(['GET'])
def banklist(reqeust):
    banks=Banks.objects.all()
    banklist=BankSerializer(banks,many=True)
    return Response(banklist.data)


    
