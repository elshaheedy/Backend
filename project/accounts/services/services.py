from accounts.models import Employee, Patient , Doctor
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response

User = get_user_model()



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
