from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from . import models
from .serializers import PersonSerializer
from rest_framework import permissions
from rest_framework.viewsets import ViewSet


@api_view(['GET', 'POST'])
def one(request):
    data = {
        'Message': 'Hello world',
    }
    if request.method == 'POST':
        name = request.data['name']
        return Response(data=name, status=status.HTTP_200_OK)
    else:
        return Response(data['Message'], status=status.HTTP_200_OK)


@api_view(['GET'])
def all_person(request):
    obj = models.Person.objects.all()
    ser = PersonSerializer(obj, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def new_person(request, ):
    if request.method == 'POST':
        form = request.data
        data = {
            'name': form['name'],
            'age': form['age'],
            'email': form['email']
        }
        ser = PersonSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def new_user(request):
    ser = PersonSerializer(data=request.data)
    if ser.is_valid():
        models.Person(name=ser.validated_data['name'], age=ser.validated_data['age'],
                      email=ser.validated_data['email']).save()
        return Response({'message': 'Ok'})
    else:
        return Response(ser.errors)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def retrieve_person(request, r_id):
    try:
        obj = models.Person.objects.get(pk=r_id)
        ser = PersonSerializer(obj)
        return Response(ser.data, status=status.HTTP_200_OK)
    except:
        return Response({"Message": "Error"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def search_person(request):
    try:
        obj = models.Person.objects.filter(name__icontains=request.query_params['name'])
        ser = PersonSerializer(obj, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    except:
        return Response({"Message": "Error"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", 'DELETE'])
def del_person(request, d_id):
    try:
        obj = models.Person.objects.get(id=d_id)
    except:
        return Response({'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)
    obj.delete()
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def up_person(request, u_id):
    obj = models.Person.objects.get(id=u_id)
    if request.method == 'PUT':
        ser = PersonSerializer(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)



