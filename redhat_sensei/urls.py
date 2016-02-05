from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'redhat_sensei.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'redhat_sensei_quiz.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),


#    url(r'^quiz/', include('giturdone_quiz.urls', namespace="giturdone_quiz")),
#    url(r'^$', 'giturdone_quiz.views.index', name='index'),
#    url(r'^results/', 'giturdone_quiz.views.results', name='results'),
# Left line below in prod version for now just in case it is needed
#    url(r'^quiz/', 'giturdone_quiz.views.git_quiz', name='git_quiz'),
#    url(r'^account/', include('registration.backends.default.urls')),
#    url(r'^admin/', include(admin.site.urls)),
]
