from rest_framework import serializers
from notice.models import Notice


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('title', 'start_date', 'end_date')
