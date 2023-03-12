from django.contrib import admin
from django.urls import path, include

from engine.views import CustomLoginView, SchemaAddView, SchemaListView, SchemaUpdateView, SchemaDeleteView, \
    SchemaDetailView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('schema_create/', SchemaAddView.as_view(), name='schema_create'),
    path('schema_list/', SchemaListView.as_view(), name='schema_list'),
    path('schema_update/<int:pk>', SchemaUpdateView.as_view(), name='schema_update'),
    path('schema_delete/<int:pk>', SchemaDeleteView.as_view(), name='schema_delete'),
    path('schema_detail/<int:pk>', SchemaDetailView.as_view(), name='schema_detail'),
]