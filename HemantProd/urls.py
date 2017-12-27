"""HemantProd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
#from django.contrib import admin

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#]

#Copied
#from django.conf.urls import patterns, include, url


#from django.conf.urls.defaults import *
from django.conf.urls import url, include
from django.contrib import admin
#from django.conf.urls import patterns, url, include
#from yavatmal.views import *

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from spardhamitra import settings

from django.contrib import admin
from django.contrib.auth import views as auth_views
from yavatmal import views as ytlViews
from yavatmal.models import *
from pioneer import views as pioViews
from pioneer.models import *
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings



urlpatterns = [
    # Examples:
    # url(r'^$', 'spardhamitra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

    # Examples:
    #url(r'^$', home),
    #url(r'^$', 'django.contrib.auth.views.login'),
    #url(r'^admintools/', include('admin_tools.urls')),
    #(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^$', ytlViews.root),
    # url(r'^blog/', include('blog.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^index$', ytlViews.index, name='index'),
	url(r'^login/$', ytlViews.login),
	url(r'^signin/$', ytlViews.signin),
    url(r'^logout/$', ytlViews.logout_page),
    url(r'^Applogout/$', ytlViews.Applogout_page),
    url(r'^accounts/login/$', auth_views.login), # If user is not login it will redirect to login page
    url(r'^register/$', ytlViews.register),
    url(r'^register/success/$', ytlViews.register_success),
    url(r'^accounts/profile/$', ytlViews.home),
	url(r'^myprofile/$', ytlViews.myprofile),
    url(r'^Dashboard/$', ytlViews.dashboard),
    url(r'^AppDashboard/$', ytlViews.Appdashboard),
    #url(r'^appear_exam/(?P<id>\d+)/$', views.appear_exam),
    url(r'^appear_exam/(?P<T_Exam_ExamID_url>\w+)/$', ytlViews.appear_exam),
    url(r'^Appappear_exam/(?P<T_Exam_ExamID_url>\w+)/$', ytlViews.Appappear_exam),
    url(r'^start_exam/(?P<T_Exam_ExamID_url>\w+)/$', ytlViews.start_exam),
    url(r'^Appstart_exam/(?P<T_Exam_ExamID_url>\w+)/$', ytlViews.Appstart_exam),
    url(r'^print/admin/yavatmal/t_exam/(?P<T_Exam_ExamID_url>\w+)/history/$', ytlViews.print_paper),
    url(r'^exam_answers/(?P<T_Exam_ExamID_url>\w+)/$', ytlViews.exam_answers),
    url(r'^Appexam_answers/(?P<T_Exam_ExamID_url>\w+)/$', ytlViews.Appexam_answers),
	url(r'^Admissions/$', ytlViews.Admissions),
	url(r'^Contacts/$', ytlViews.Contacts),
	url(r'^Courses/$', ytlViews.Courses),
	url(r'^Programs/$', ytlViews.Programs),
	url(r'^AppPrograms/$', ytlViews.AppPrograms),
	url(r'^Teachers/$', ytlViews.Teachers),
	url(r'^submit_paper$', ytlViews.SubmitPaper),
	url(r'^Programs/(?P<T_Exam_ExamID_url>\w+)/$', ytlViews.articles),
	#url(r'^ckeditor/', include('ckeditor.urls')),
	url(r'^ques/', ytlViews.QuestionList.as_view()),
	url(r'^quesreq/(?P<pk>[0-9]+)/$', ytlViews.QuestionList.questionsset_detail),
	url(r'^generate/', pioViews.generate_pdf, name='generate_pdf'),
	url(r'^ckeditor/', include('ckeditor_uploader.urls')),


]

urlpatterns = format_suffix_patterns(urlpatterns)

admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.site_header = settings.ADMIN_SITE_HEADER