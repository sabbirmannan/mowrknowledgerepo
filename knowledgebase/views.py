
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as logout_view
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import OuterRef, Q, Subquery
from django.shortcuts import redirect, render

from .forms import OrganizationForm
from .models import (Article, ArticleCategory, ArticlePublishCategory,
                     DataCategory, Document, Organization)

# Create your views here.


def home(request):
    count_organization = Organization.objects.count()
    count_categories = DataCategory.objects.filter(parent__isnull=True).count()

    pub_cat_ids = [5, 14]
    count_publication = Document.objects.filter(
        data_category__id__in=pub_cat_ids).count()
    count_reports = Document.objects.filter(
        Q(data_category__id=10) | Q(data_category__parent=10)).count()

    law_act_policy_cat_ids = [1, 7, 9, 11, 19]
    count_law_act_policy = Document.objects.filter(
        data_category__id__in=law_act_policy_cat_ids).count()

    plan_cat_ids = [33, 51]
    count_plan = Document.objects.filter(
        data_category__id__in=plan_cat_ids).count()

    context = {'organization': count_organization,
               'categories': count_categories, 'publication': count_publication, 'reports': count_reports, 'law_act_policy': count_law_act_policy, 'plan': count_plan}

    return render(request, 'home.html', context)


<<<<<<< HEAD
def home2(request):    
=======
def home2(request):

>>>>>>> 10df9e3d236791e4c6080b09db7fe837d1f76c55
    return render(request, 'home2.html')


def home3(request):
    return render(request, 'home3.html')


def test(request):    
    return render(request, 'test.html')

def dashboard(request):
    count_organization = Organization.objects.count()

    count_categories = DataCategory.objects.filter(parent__isnull=True).count()

    pub_cat_ids = [5, 14]
    count_publication = Document.objects.filter(
        data_category__id__in=pub_cat_ids).count()
    count_reports = Document.objects.filter(
        Q(data_category__id=10) | Q(data_category__parent=10)).count()

    law_act_policy_cat_ids = [1, 7, 9, 11, 19]
    count_law_act_policy = Document.objects.filter(
        data_category__id__in=law_act_policy_cat_ids).count()

    plan_cat_ids = [33, 51]
    count_plan = Document.objects.filter(
        data_category__id__in=plan_cat_ids).count()

    context = {'organization': count_organization,
               'categories': count_categories, 'publication': count_publication, 'reports': count_reports, 'law_act_policy': count_law_act_policy, 'plan': count_plan}

    return render(request, 'dashboard.html', context)


def orgsearch(request):
    return render(request, 'orgsearch.html')


def docsearch(request):
    return render(request, 'docsearch.html')


def national_international(request):
    return render(request, 'national-international-search.html')


def SearchResult1(request):
    return render(request, 'SearchResult1.html')


def article(request):
    #article_obj = Article.objects.get(pk=1)
    query_set = ArticlePublishCategory.objects.all()
    # query_set = Article.objects.select_related(
    #     'article_category', 'publish_category').order_by('id')

    # articles = Article.objects.filter(article_category=OuterRef('pk'))
    # ArticleCategory.objects.all().annotate(
    #     article_under_cat=Subquery(articles.values('article_category')))

    article_cat_queryset = ArticleCategory.objects.all()
    context = {'article_categories': article_cat_queryset,
               'atr_pub_cat': query_set}

    return render(request, 'article.html', context)


def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {'article': article}

    return render(request, 'article-detail.html', context)


def addOrganization(request):
    form = OrganizationForm()
    if request.method == 'POST':
        form = OrganizationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'Organization/add.html', context)
