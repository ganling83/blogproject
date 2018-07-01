from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archives, name='archives'),
    path('category/<int:pk>/', views.category, name='category'),

]
#回头尝试将urlpatterns重新写一遍，
"""
    写成类似
       urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
 """
app_name='blog'
"""
    如果没有会出现
        NoReverseMatch at / 'blog' is not a registered namespace
"""