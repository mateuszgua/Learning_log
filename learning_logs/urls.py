"""Define URL adress for learning_log"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Main page
    path('', views.index, name='index'),
    # Show all topics
    path('topics/', views.topics, name='topics'),
    # Page with simple topic
    path('topics/(<int:topic_id>)/', views.topic, name='topic'),
    # Page for add new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for add new entry
    path('new_entry/(<int:topic_id>)/', views.new_entry, name='new_entry'),
    # Page for edit entry
    path('edit_entry/(<int:entry_id>)/', views.edit_entry, name='edit_entry'),
    
]