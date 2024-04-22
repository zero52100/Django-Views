from rest_framework.generics import CreateAPIView, RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ForeignKeyModel, MainModel
from .serializers import ForeignKeyModelSerializer, MainModelSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from .models import MainModel
from .serializers import MainModelSerializer
from django.db.models import Q  
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

class ListMainRecords(ListAPIView):
    serializer_class = MainModelSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = MainModel.objects.all()
        
        
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query))
        
       
        created_after = self.request.query_params.get('created_after', None)
        created_before = self.request.query_params.get('created_before', None)
        updated_after = self.request.query_params.get('updated_after', None)
        updated_before = self.request.query_params.get('updated_before', None)
        
        if created_after:
            queryset = queryset.filter(created_at__gte=created_after)
        if created_before:
            queryset = queryset.filter(created_at__lte=created_before)
        if updated_after:
            queryset = queryset.filter(updated_at__gte=updated_after)
        if updated_before:
            queryset = queryset.filter(updated_at__lte=updated_before)
        
        sort_by = self.request.query_params.get('sort_by', None)
        if sort_by:
            queryset = queryset.order_by(sort_by)
        
        return queryset