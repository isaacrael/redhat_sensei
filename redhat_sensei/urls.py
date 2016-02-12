from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'redhat_sensei.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^account/', include('registration.backends.default.urls')),
    url(r'^$', 'redhat_sensei_quiz.views.index', name='index'),
    url(r'^quiz_selection/', 'redhat_sensei_quiz.views.quiz_selection', name='quiz_selection'),
    url(r'^quiz_selection/', include('redhat_sensei_quiz.urls', namespace="redhat_sensei_quiz")),
    url(r'^quiz/', include('redhat_sensei_quiz.urls', namespace="redhat_sensei_quiz")),
#    url(r'^quiz/', 'redhat_sensei_quiz.views.git_quiz', name='git_quiz'),
    url(r'^admin/', include(admin.site.urls)),



#    url(r'^results/', 'giturdone_quiz.views.results', name='results'),
# Left line below in prod version for now just in case it is needed
#    url(r'^quiz/', 'giturdone_quiz.views.git_quiz', name='git_quiz'),
#    url(r'^account/', include('registration.backends.default.urls')),
#    url(r'^admin/', include(admin.site.urls)),
]
