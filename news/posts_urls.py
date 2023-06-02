
from django.urls import path

from .views import Posts, PostCreate, PostUpdate, PostDetail, PostDelete, upgrade_me,\
    CategoryListView, subscribe

urlpatterns = [
    path('', Posts.as_view(), name='posts'),
    # path('search', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_details'),
    path('add/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('upgrade', upgrade_me, name='upgrade'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
]
