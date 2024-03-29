from rest_framework import serializers
from .models import DailyLog


class DailyLogSerializers(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'
