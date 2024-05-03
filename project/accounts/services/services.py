from accounts.models import Employee, Patient , Phone, Address, Doctor
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response

from accounts.serializers import EmployeeSerializer, PatientSerializer, PhoneSerializer, AddressSerializer
User = get_user_model()

serializer_map = {
    # 'employee': EmployeeSerializer,
    # 'patient': PatientSerializer,
    # 'doctor': EmployeeSerializer,
    'phone': PhoneSerializer,
    'address': AddressSerializer
}
model_map = {
    # 'employee': Employee,
    # 'patient': Patient,
    # 'doctor': Doctor,
    'phone': Phone,
    'address': Address
}

def create_user(request_data):
    try:
        national_id = request_data['national_id']
    except:
        return "national_id is required", None
    try:
        user = User.objects.create_user(username=national_id, password=national_id)
        return "created" ,user 
    except :
        return "national_id already exists", None



def create_model(model_data, user,SerializerClass):
    model_data['user'] = user.id
    serializer = SerializerClass(data=model_data)
    if not serializer.is_valid():
        return serializer.errors, "not valid"
    model_instance = serializer.save()
    return SerializerClass(model_instance).data,"created"

def postion_create(request_data,SerializerClass):
    massage, user = create_user(request_data)
    if massage!="created":   return Response(massage, status=status.HTTP_400_BAD_REQUEST)
    request_data['user'] = user.id
    serializer  = SerializerClass(data=request_data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    serializer.save()
  
    for field in request_data:
        if field not in  serializer_map :   continue
        serializer_class = serializer_map.get(field)
        sub_instance,massage  = create_model(request_data[field],user,serializer_class)
        if massage!="created":   return Response(sub_instance, status=status.HTTP_400_BAD_REQUEST)

    return Response(SerializerClass(serializer.instance).data, status=status.HTTP_201_CREATED)
        





def update_model(modelClass, model_data,SerializerClass):
    instance = modelClass.objects.get(id=model_data['id'])
    serializer =  SerializerClass( instance=instance, data=model_data, partial=True)
    if not serializer.is_valid():
        return serializer.errors , "not valid"
    serializer.save()
    return SerializerClass(instance).data ,"updated"


def postion_update(instance,request_data,SerializerClass):

   
    serializer  =SerializerClass(instance= instance,data=request_data, partial=True)
    if not serializer .is_valid():
        return Response(serializer .errors, status=status.HTTP_400_BAD_REQUEST)
    serializer .save()

   
    for field in request_data:
        if field not in  serializer_map :   continue
        serializer_class = serializer_map.get(field)

        model_instance = model_map.get(field)
        update_data,massage = update_model(model_instance, request_data[field],serializer_class)
        if massage!="updated":   return Response( update_data, status=status.HTTP_400_BAD_REQUEST)
       
    return Response(SerializerClass(serializer.instance).data, status=status.HTTP_200_OK)
