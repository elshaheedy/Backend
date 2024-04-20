from accounts.models import Employee, Patient , Phone, Address, Doctor
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response

from accounts.serializers import EmployeeSerializer, PatientSerializer, PhoneSerializer, AddressSerializer
User = get_user_model()

serializer_map = {
    'employee': EmployeeSerializer,
    'patient': PatientSerializer,
    'doctor': EmployeeSerializer,
    'phone': PhoneSerializer,
    'address': AddressSerializer
}
model_map = {
    'employee': Employee,
    'patient': Patient,
    'doctor': Doctor,
    'phone': Phone,
    'address': Address
}

def create_user(request_data):
    national_id = request_data['patient']['national_id']
    user = User.objects.create_user(username=national_id, password=national_id)
    return user

def create_model(data, user,SerializerClass):
    data['user'] = user.id
    serializer = SerializerClass(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    model_instance = serializer.save()
    return SerializerClass(model_instance).data

def create_data(data):
    user = create_user(data)
    response_data={}
    for field in data:
        serializer_class = serializer_map.get(field)
        if not serializer_class:   continue
        response_data[field]= create_model(data[field],user,serializer_class)
    return response_data
        





def update_model(model_instance, model_data,SerializerClass):
               
    serializer =  SerializerClass(model_instance, data=model_data, partial=True)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    updated_model = serializer.save()
    return SerializerClass(updated_model).data


def update_data(data):

    response_data={}
    for field in data:
        model_class = model_map.get(field)
        serializer_class = serializer_map.get(field)
        if not  model_class or not serializer_class:   continue
        instance = model_class.objects.get(id=data[field].pop('id'))
        response_data[field]= update_model(instance, data[field],serializer_class)
        
    return response_data

