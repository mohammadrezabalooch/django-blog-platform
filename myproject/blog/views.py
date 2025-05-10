from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from account.models import User
from account.mixins import AuthorAccessMixin
from django.http import HttpResponse
from .models import Article, Category
from django.db.models import Q
# Create your views here.

def home(request):
    articles_list= Article.objects.all()
    paginator = Paginator(articles_list,4)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {"articles" : articles
    }
    return render(request, "blog/home.html", context)

def detail(request, slug):
    context = {
        "article" : Article.objects.get(slug=slug)
    }
    return render(request,'blog/detail.html', context)

# def index(request, page=1):
#     articles_list = Article.objects.all()
#     paginator = Paginator(articles_list, 2)
#     articles = paginator.get_page(page)
#     context = {"articles": articles
#     }
#     return render(request, "blog/article_list.html", context)

class ArticleList(ListView):
    # model = Article
    # template_name = "blog/article_list.html"
    # context_object_name = "articles"
    queryset = Article.objects.published()
    paginate_by = 2



# def post(request, slug):
#     context = {
#         "article" : get_object_or_404(Article.objects.published(), slug=slug, status = "p")
#     }
#     return render(request,'blog/article_detail.html', context)

class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)
        
        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)
        return article

class ArticlePreview(AuthorAccessMixin, DetailView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)

# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     articles_list= category.articles.published()
#     paginator = Paginator(articles_list, 1)
#     articles = paginator.get_page(page)
#     context = {
#         "category": category,
#         "articles": articles,
#     }
#     return render(request, "blog/category.html", context)

class CategoryList(ListView):
    paginate_by = 1
    template_name = "blog/category.html"
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
    
class AuthorList(ListView):
    paginate_by = 1
    template_name = "blog/author.html"
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context


class SearchList(ListView):
    paginate_by = 1
    template_name = "blog/search_list.html"
    def get_queryset(self):
        search = self.request.GET.get('q')
        return Article.objects.filter(Q(description__icontains=search) | Q(title__icontains=search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context



