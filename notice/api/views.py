from rest_framework import viewsets
from notice.models import Notice
from .serializer import NoticeSerializer


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
