from django.urls import path
from api.views import ProductListCreateAPIView, CategoryListCreateAPIView, getStart, CategoryDetailAPIView, ProductDetailAPIView


urlpatterns = [
    path('', getStart.as_view()),
    path('product/', ProductListCreateAPIView.as_view()),
    path('product/<int:pk>/', ProductDetailAPIView.as_view()),
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),
]
