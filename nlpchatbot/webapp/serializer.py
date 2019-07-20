from rest_framework import serializers
from rest_framework import employees

class employeeSeralizer (seralizers.ModelSeralizer):

    class Meta:
        model=employees
        fields='__all__' 