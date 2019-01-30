from rest_framework import serializers

from stockapp.models import Stock
from django.contrib.auth import get_user_model


class StockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'stock_name', 'stock_price', 'stock_gain', 'stock_markets')


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
