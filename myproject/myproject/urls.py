from django.urls import path
from myapp.views import CreateMainRecord, RetrieveMainRecord, RetrieveMainRecordDetails

urlpatterns = [
    path('api/main/create/', CreateMainRecord.as_view(), name='main-create'),
    path('api/main/<int:pk>/', RetrieveMainRecord.as_view(), name='main-retrieve'),
    path('api/main/<int:pk>/details/', RetrieveMainRecordDetails.as_view(), name='main-details'),
]
