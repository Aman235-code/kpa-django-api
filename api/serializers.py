from rest_framework import serializers
from .models import BasicInfo
from .models import WheelSpecification, BogieChecksheet

class BasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInfo
        fields = '__all__'

class WheelSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'

class BogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheet
        fields = '__all__'