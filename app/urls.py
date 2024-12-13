from django.urls import path,include
from .views import PostBucket,GetBucket

urlpatterns = [
    path('postbucket',PostBucket.as_view()),
    path('getbucket/<str:url_id>/',GetBucket.as_view())
]