from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BasicInfo, WheelSpecification, BogieChecksheet
from .serializers import BasicInfoSerializer, WheelSpecificationSerializer, BogieChecksheetSerializer
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def get_wheel_specification(request):
    form_number = request.GET.get('formNumber')
    if not form_number:
        return Response({'error': 'Missing formNumber parameter'}, status=status.HTTP_400_BAD_REQUEST) 
    try:
        spec = WheelSpecification.objects.get(form_number=form_number)
        serializer = WheelSpecificationSerializer(spec)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except WheelSpecification.DoesNotExist:
        return Response({'error': 'No data found for this formNumber'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_basic_info(request):
    serializer = BasicInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_basic_info_by_phone(request, phone):
    try:
        info = BasicInfo.objects.get(phone=phone)
        serializer = BasicInfoSerializer(info)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except BasicInfo.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_wheel_spec(request):
    serializer = WheelSpecificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Wheel specification submitted successfully.",
            "data": {
                "formNumber": serializer.data["form_number"],
                "submittedBy": serializer.data["submitted_by"],
                "submittedDate": serializer.data["submitted_date"],
                "status": "Saved"
            }
        }, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_bogie_checksheet(request):
    serializer = BogieChecksheetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Bogie checksheet submitted successfully.",
            "data": {
                "formNumber": serializer.data["form_number"],
                "inspectionBy": serializer.data["inspection_by"],
                "inspectionDate": serializer.data["inspection_date"],
                "status": "Saved"
            }
        }, status=201)
    return Response(serializer.errors, status=400)

