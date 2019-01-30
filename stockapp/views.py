from django.contrib.auth import get_user_model
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

from .serializers import StockSerializers, UserSerializers
from .models import Stock
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated,AllowAny
# Create your views here.

class StockViewSets(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Stock.objects.all()
    serializer_class = StockSerializers

    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ('stock_markets',)
    seach_fields = ('stock_name',)
    odering = ('stock_gain',)



class CreateUserViews(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializers



