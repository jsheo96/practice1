from .models import Aquainfo
from rest_framework import serializers

class AquainfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aquainfo
        fields = ['date','days','num','average_weight','total_weight',
                  'biomass','survival_rate','feed','weekly_growth_rate',
                  'total_weight_increase','feed_conversion_rate','remarks']

