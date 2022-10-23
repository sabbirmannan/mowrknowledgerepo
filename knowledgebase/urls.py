from django.urls import path


from . import views

# URLConf
urlpatterns = [
    path('', views.home, name="home"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('orgsearch/', views.orgsearch, name="orgsearch"),
    path('docsearch/', views.docsearch, name="docsearch"),
    path('national_international/', views.national_international,
         name="national_international"),
    path('SearchResult1/', views.SearchResult1, name="SearchResult1"),
    path('home2/', views.home2, name="home2"),
    path('home3/', views.home3, name="home3"),

    path('article/', views.article, name="article"),
    path('article/<int:pk>/', views.article_detail, name="article_detail"),

    path('organization/add', views.addOrganization, name="add_organization"),
    path('document/add', views.addDocument, name="add_document"),
    path('article/add', views.addArticleDetail, name="add_article"),
]
