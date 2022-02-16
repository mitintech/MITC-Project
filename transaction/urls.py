from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from .views import *
from master.views import *
from django.conf.urls.static import static

urlpatterns = [

    path('streaminsert/',streaminsert),
    path('streamsearch/', streamsearch),
    path('streamupdate/<int:id>', streamupdate),
    path('streamdelete/<int:id>', streamdelete),

    path('classinsert/',classinsert),
    path('classsearch/', classsearch),
    path('classupdate/<int:id>', classupdate),
    path('classdelete/<int:id>', classdelete),

    path('subjectinsert/', subjectinsert),
    path('subjectsearch/', subjectsearch),
    path('subjectupdate/<int:id>', subjectupdate),
    path('subjectdelete/<int:id>', subjectdelete),

    path('chapterinsert/', chapterinsert),
    path('chaptersearch/', chaptersearch),
    path('chapterupdate/<int:id>', chapterupdate),
    path('chapterdelete/<int:id>', chapterdelete),

    path('typesofquestioninsert/', typesofquestioninsert),
    path('typesofquestionsearch/', typesofquestionsearch),
    path('typesofquestionupdate/<int:id>', typesofquestionupdate),
    path('typesofquestiondelete/<int:id>', typesofquestiondelete),

    path('examinsert/', examinsert),
    path('examsearch/', examsearch),
    path('examupdate/<int:id>', examupdate),
    path('examdelete/<int:id>', examdelete),





    path('studentinsert/', studentinsert),
    path('studentsearch/', studentsearch),
    path('studentupdate/<int:id>', studentupdate),
    path('studentdelete/<int:id>',studentdelete),

    path('teacherinsert/',teacherinsert),
    path('teachersearch/',teachersearch),
    path('teacherupdate/<int:id>', teacherupdate),
    path('teacherdelete/<int:id>',teacherdelete),

    path('questioninsert/',questioninsert),
    path('questionsearch/',questionsearch),
    path('questionupdate/<int:id>',questionupdate),
    path('questiondelete/<int:id>',questiondelete),

    path('resultinsert/',resultinsert),
    path('resultsearch/', resultsearch),
    path('resultupdate/<int:id>', resultupdate),
    path('resultdelete/<int:id>',resultdelete),

#################################################################################################################################



    # path('streaminsert/',streaminsert),
    # path('streamsearch/', streamsearch),
    # path('streamupdate/<int:id>', streamupdate),
    # path('streamdelete/<int:id>', streamdelete),
    #
    # path('classinsert/',classinsert),
    # path('classsearch/', classsearch),
    # path('classupdate/<int:id>', classupdate),
    # path('classdelete/<int:id>', classdelete),
    #
    # path('subjectinsert/', subjectinsert),
    # path('subjectsearch/', subjectsearch),
    # path('subjectupdate/<int:id>', subjectupdate),
    # path('subjectdelete/<int:id>', subjectdelete),
    #
    # path('chapterinsert/', chapterinsert),
    # path('chaptersearch/', chaptersearch),
    # path('chapterupdate/<int:id>', chapterupdate),
    # path('chapterdelete/<int:id>', chapterdelete),
    #
    # path('typesofquestioninsert/', typesofquestioninsert),
    # path('typesofquestionsearch/', typesofquestionsearch),
    # path('typesofquestionupdate/<int:id>', typesofquestionupdate),
    # path('typesofquestiondelete/<int:id>', typesofquestiondelete),
    #
    # path('examinsert/', examinsert),
    # path('examsearch/', examsearch),
    # path('examupdate/<int:id>', examupdate),
    # path('examdelete/<int:id>', examdelete),



    path('groupinsert/',groupinsert),
    path('groupview/', groupview),
    path('groupupdate/<int:id>', groupupdate),
    path('groupdelete/<int:id>', groupdelete),



    path('sopinsert/', sopinsert),
    path('sopview/', sopview),
    path('sopupdate/<int:id>', sopupdate),
    path('sopdelete/<int:id>', sopdelete),


    path('practicalquestionsinsert/', practicalquestionsinsert),
    path('practicalquestionsview/', practicalquestionsview),
    path('practicalquestionsupdate/<int:id>', practicalquestionsupdate),
    path('practicalquestionsdelete/<int:id>', practicalquestionsdelete),


    path('', index),
    path('ebookinsert/', fnebook , name='ebookinsert'),

    path('questionpaper/', questionpaper, name='questionpaper'),

    path('load-courses/', load_courses, name='ajax_load_courses'),


    path('group/',gcfilterview,name='group'),

    path('practical/', practical , name='practical'),
]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)