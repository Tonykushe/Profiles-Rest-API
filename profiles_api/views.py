from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from . models import employee
from . serializers import employeeSerializer

# Create your views here.
class employeeList(APIView):
  
  def get(self, request):
    """ Get the employee details """
    varemployee = employee.objects.all()
    serializer = employeeSerializer(varemployee, many=True)
    return Response(serializer.data)

  def post(self, request):
    """ Post new Employees """
    serializer = employeeSerializer(data=request.data)

    if serializer.is_valid():
      name = serializer.data.get('firstname')
      message = 'Hello {0}'.format(name)
      return Response({'message' : message})
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk=None):
    """ Handles updating an object """

    return Response({'method': 'put'})

  def patch(self, request, pk=None):
    """ Only updates fields provided in the request, Partial update """

    return Response({'method': 'patch'})

  def delete(self, request, pk=None):
    """Deletes an object """

    return Response({'method': 'delete'})

class EmployeeViewSet(viewsets.ViewSet):
  
  def list(self, request):
    """ Get the employee list """
    varemployee = employee.objects.all()
    serializer = employeeSerializer(varemployee, many=True)
    return Response(serializer.data)

  def create(self, request):
    """ Post new Employees """
    serializer = employeeSerializer(data=request.data)

    if serializer.is_valid():
      name = serializer.data.get('firstname')
      message = 'Hello {0}'.format(name)
      return Response({'message' : message})
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def retrieve(self, request, pk=None):
    """ Handles getting an object by it's ID """

    return Response({'http_method': 'GET'})

  def update(self, request, pk=None):
    """ Handles updating an object """

    return Response({'http_method': 'PUT'})

  def partial_update(self, request, pk=None):
    """ Handles updating part of an object """

    return Response({'http_method': 'PATCH'})

  def destroy(self, request, pk=None):
    """ Handles removing an object """

    return Response({'http_method': 'DELETE'})