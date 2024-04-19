from rest_framework.generics import CreateAPIView, RetrieveAPIView,UpdateAPIView,DestroyAPIView
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

class RetrieveMainRecordDetails(UpdateAPIView):
    def get(self, request, pk):
        main_record = MainModel.objects.get(pk=pk)
        serializer = MainModelSerializer(main_record)
        return Response(serializer.data)


class UpdateMainRecord(APIView):
    def put(self, request, pk):
        main_record = MainModel.objects.get(pk=pk)
        serializer = MainModelSerializer(main_record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Record updated successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        main_record = MainModel.objects.get(pk=pk)
        serializer = MainModelSerializer(main_record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Record updated successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DeleteMainRecord(DestroyAPIView):
    queryset = MainModel.objects.all()
    serializer_class = MainModelSerializer
    lookup_url_kwarg = 'pk'
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
            return Response({"message": "Record deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": f"Failed to delete record: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class BulkDeleteMainRecords(APIView):
    def post(self, request):
        ids = request.data.get('ids', [])
        MainModel.objects.filter(pk__in=ids).delete()
        return Response({"message": "Records deleted successfully."})

