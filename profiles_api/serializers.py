from rest_framework import serializers
from rest_framework import employee

class employeeSerializer(serializers.ModelSerializer):
  

  class Meta:
    model = employee
    # fields = ('firstname', 'lastname')
    fields = '__all__'