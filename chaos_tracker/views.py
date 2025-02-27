from django.shortcuts import render
from rest_framework import viewsets
from . models import Employee,Interaction
from . serializers import EmployeeSerializer,InteractionSerializer
from django.http import JsonResponse

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

def top_chaos_employee(request):
    top_employee = Employee.objects.order_by('-chaos_level').first()
    if top_employee:
        return JsonResponse({"name": top_employee.name, "chaos_level": top_employee.chaos_level})
    return JsonResponse({"message": "No employees found"}, status=404)