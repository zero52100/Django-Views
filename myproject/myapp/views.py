from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ForeignKeyModel, MainModel
from .serializers import ForeignKeyModelSerializer, MainModelSerializer
from rest_framework import status
class CreateMainRecord(CreateAPIView):
    serializer_class = MainModelSerializer

    def create(self, request, *args, **kwargs):
     
        foreign_key_id = request.data.get('foreign_key_field')
        try:
            foreign_key_instance = ForeignKeyModel.objects.get(pk=foreign_key_id)
        except ForeignKeyModel.DoesNotExist:
            
            foreign_key_instance = ForeignKeyModel.objects.create(id=foreign_key_id)  
       
        request.data['foreign_key_field'] = foreign_key_instance.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RetrieveMainRecord(RetrieveAPIView):
    queryset = MainModel.objects.all()
    serializer_class = MainModelSerializer

class RetrieveMainRecordDetails(APIView):
    def get(self, request, pk):
        main_record = MainModel.objects.get(pk=pk)
        serializer = MainModelSerializer(main_record)
        return Response(serializer.data)
