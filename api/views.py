from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import company
from .serializer import CompanySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def getData(request):
    lis=company.objects.all()
    serializer=CompanySerializer(lis,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def postData(request):
    serializer=CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
def companies(request):
    app=company.objects.all()
    return render(request,{'app':app})
