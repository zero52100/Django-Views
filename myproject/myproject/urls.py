from django.urls import path
from myapp.views import CreateMainRecord, RetrieveMainRecord, RetrieveMainRecordDetails,UpdateMainRecord,DeleteMainRecord,BulkDeleteMainRecords

urlpatterns = [
    path('api/main/create/', CreateMainRecord.as_view(), name='main-create'),
    path('api/main/<int:pk>/', RetrieveMainRecord.as_view(), name='main-retrieve'),
    path('api/main/<int:pk>/details/', RetrieveMainRecordDetails.as_view(), name='main-details'),
    path('api/main/<int:pk>/update/', UpdateMainRecord.as_view(), name='main-update'),
    path('api/main/<int:pk>/delete/', DeleteMainRecord.as_view(), name='main-delete'),
    path('api/main/bulk-delete/', BulkDeleteMainRecords.as_view(), name='main-bulk-delete'),
    
]
