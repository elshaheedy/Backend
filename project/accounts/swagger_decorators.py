# swagger_decorators.py
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
def home_create_schema():
    return swagger_auto_schema(
        operation_description="Create home data",
        responses={status.HTTP_201_CREATED: "Created data"},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            # required=['patient'],  # Add required fields here
            
            properties={
                'postion': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'full_name': openapi.Schema(type=openapi.TYPE_STRING),
                        'nationality': openapi.Schema(type=openapi.TYPE_STRING),
                        'national_id': openapi.Schema(type=openapi.TYPE_STRING),
                        'date_of_birth': openapi.Schema(type=openapi.FORMAT_DATE),
                        'gender': openapi.Schema(type=openapi.TYPE_STRING, enum=['M', 'F']),  
                    },
                ),
                'address': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'street': openapi.Schema(type=openapi.TYPE_STRING),
                        'city': openapi.Schema(type=openapi.TYPE_STRING),
                        'governorate': openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
                'phone': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'mobile': openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            },
        ),
    )


# swagger_decorators.py
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
def home_update_schema():
    return swagger_auto_schema(
        operation_description="Update home data",
        responses={status.HTTP_200_OK: "Updated data"},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            # required=['patient', 'address', 'phone'],  # Add required fields here
            properties={
                'postion': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'nationality': openapi.Schema(type=openapi.TYPE_STRING),
                        'full_name': openapi.Schema(type=openapi.TYPE_STRING),
                        'national_id': openapi.Schema(type=openapi.TYPE_STRING),
                        'date_of_birth': openapi.Schema(type=openapi.FORMAT_DATE),
                        'gender': openapi.Schema(type=openapi.TYPE_STRING, enum=['M', 'F']),  # Assuming 'M' and 'F' are the only options
                    },
                ),
                'address': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'street': openapi.Schema(type=openapi.TYPE_STRING),
                        'city': openapi.Schema(type=openapi.TYPE_STRING),
                        'governorate': openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
                'phone': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'mobile': openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            },
        ),
    )
