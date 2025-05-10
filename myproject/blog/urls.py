from django.urls import path
from .views import home, detail, ArticleDetail, CategoryList, ArticleList, AuthorList, ArticlePreview, SearchList

app_name = 'blog'
urlpatterns = [
    #path('', home, name = 'home'),
    #path('article/<slug:slug>', detail, name = 'detail'),
    path('', ArticleList.as_view(), name = 'index'),
    path('page/<int:page>', ArticleList.as_view(), name = 'index'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name = 'post'),
    path('preview/<int:pk>', ArticlePreview.as_view(), name = 'preview'),
    path('category/<slug:slug>', CategoryList.as_view(), name = 'category'),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name = 'category'),
    path('author/<slug:username>', AuthorList.as_view(), name = 'author'),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name = 'author'),
    path('search/', SearchList.as_view(), name = 'search'),
    path('search/page/<int:page>', SearchList.as_view(), name = 'search'),
]
