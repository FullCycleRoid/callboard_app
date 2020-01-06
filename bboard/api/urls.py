from django.urls import path
from .views import bbs, comments, BbsDetailView


app_name = 'api'

urlpatterns = [
    path('bbs/', bbs, name='bbs_api'),
    path('bbs/<int:pk>', BbsDetailView.as_view(), name='bbs_detail_api'),
    path('comments/<int:pk>', comments, name='bbs_comments_api'),
]