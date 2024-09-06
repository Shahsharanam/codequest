from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexview,name="indexview"),
    path('home', views.home, name='home'),
    path('student_login', views.student_login, name='student_login'),
    path('student_login1', views.student_login1, name='student_login1'),
    path('language_selection', views.language_selection, name='language_selection'),
    path('start_level', views.start_level, name='start_level'),
    path('quiz_view', views.quiz_view, name='quiz_view'),
    path('Logintrans', views.Logintrans, name='Logintrans'),
    path('Logintrans1', views.Logintrans1, name='Logintrans1'),
    path('user', views.user, name='user'),
    path('topic', views.topic, name='topic'),
    path('strings', views.strings, name='strings'),
    path('strings2', views.strings2, name='strings2'),
    path('strings3', views.strings3, name='strings3'),
    path('strings4', views.strings4, name='strings4'),
    path('strings5', views.strings5, name='strings5'),
    path('strings6', views.strings6, name='strings6'),
    path('quiz1', views.quiz1, name='quiz1'),
    path('quiz2', views.quiz2, name='quiz2'),
    path('quiz3', views.quiz3, name='quiz3'),
    path('quiz4', views.quiz4, name='quiz4'),
    path('quiz5', views.quiz5, name='quiz5')

]