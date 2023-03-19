from rest_framework import pagination, viewsets
from rest_framework.generics import ListAPIView

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 10


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination


class AdListView(ListAPIView):
    queryset = Ad.objects.all() # Список всех записей модели
    serializer_class = AdSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

