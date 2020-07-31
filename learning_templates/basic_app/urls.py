from django.conf.urls import url
from basic_app import views
# URL MAPPING between proj amd app: LEC 141 11:00 min
# TEMPLATE TAGGING
app_name = 'basic_app'  #this needs to be set up for relative
                        # url tagging. Reference this within
                        # href statement

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
