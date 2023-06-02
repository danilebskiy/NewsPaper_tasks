from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'content_header': ['exact'],
                  'author': ['exact'],
                  'data': ['date'],
                  }
