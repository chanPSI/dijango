from django.urls import path
from . import views
from .views import base_views, question_views, answer_views

app_name = 'pybo'

urlpatterns = [
    
    #path
    
    # base_views.py
    path('question/list/', base_views.index, name='index'),
    path('question/list/<str:category_name>/', base_views.index, name='index'),
    path('question/detail/<int:question_id>/', base_views.detail, name='detail'),

    # question
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),
    path('question/create/<str:category_name>/', question_views.question_create, name='question_create_category'),
    path('question/list/<str:category_name>/', base_views.index, name='question_list'),

    # answer
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
]