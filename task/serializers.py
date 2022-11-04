from rest_framework import serializers
from .models import ArithmeticModel



class ArithmeticSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArithmeticModel
        fields = ('a','b','operation_type',)