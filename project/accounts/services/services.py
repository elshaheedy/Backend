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
    try:
        national_id = request_data['patient']['national_id']
    except:
        return "national_id is required", None
    try:
        user = User.objects.create_user(username=national_id, password=national_id)
        return "created" ,user 
    except :
        return "national_id already exists", None



def create_model(data, user,SerializerClass):
    data['user'] = user.id
    serializer = SerializerClass(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    model_instance = serializer.save()
    return SerializerClass(model_instance).data

def postion_create(data):
    massage, user = create_user(data)
    if massage!="created":   return Response(massage, status=status.HTTP_400_BAD_REQUEST)
    
    response_data={}
    for field in data:
        serializer_class = serializer_map.get(field)
        if field not in model_map:   continue
        response_data[field]= create_model(data[field],user,serializer_class)

        for sub_field in data[field]:
            if  sub_field not in serializer_map:   continue
            serializer_class = serializer_map.get(sub_field)
            response_data[field][sub_field]= create_model(data[field][sub_field],user,serializer_class)
    return response_data
        




def update_model(model_instance, model_data,SerializerClass):
               
    serializer =  SerializerClass(model_instance, data=model_data, partial=True)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    updated_model = serializer.save()
    return SerializerClass(updated_model).data


def postion_update(data):

    response_data={}
    for field in data:
        if   field not in model_map  or field not in serializer_map:   continue
        model_class = model_map.get(field)
        serializer_class = serializer_map.get(field)
        instance = model_class.objects.get(id=data[field].pop('id'))
        response_data[field]= update_model(instance, data[field],serializer_class)
        for sub_field in data[field]:
            if  sub_field not in serializer_map or sub_field not in model_map:   continue
            model_class = model_map.get(sub_field)
            serializer_class = serializer_map.get(sub_field)
            instance = model_class.objects.get(id=data[field][sub_field].pop('id'))
            response_data[field][sub_field]= update_model(instance, data[field][sub_field],serializer_class)
            
    return response_data

