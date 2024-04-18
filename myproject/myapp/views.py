from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ForeignKeyModel, MainModel
from .serializers import ForeignKeyModelSerializer, MainModelSerializer

class CreateMainRecord(CreateAPIView):
    queryset = MainModel.objects.all()
    serializer_class = MainModelSerializer

class RetrieveMainRecord(RetrieveAPIView):
    queryset = MainModel.objects.all()
    serializer_class = MainModelSerializer

class RetrieveMainRecordDetails(APIView):
    def get(self, request, pk):
        main_record = MainModel.objects.get(pk=pk)
        serializer = MainModelSerializer(main_record)
        return Response(serializer.data)
