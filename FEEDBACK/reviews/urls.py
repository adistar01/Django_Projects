from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path("thank_you", views.Thanks.as_view()),
    path("re", views.ReviewsListView.as_view()),
    path("re/favourite", views.AddFavView.as_view()),
    path("re/<int:pk>", views.ReviewDetail.as_view())
]