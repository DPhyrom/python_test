from django.shortcuts import render
from rest_framework import generics
from api.models import Product, Category
from api.serializers import ProductSerializer, CategorySerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.views import View
from django.http import HttpResponse


#create and view product
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'id']

#delete update retrive Product
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer






#create and view category
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#delete update retrive Category
class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class getStart(View):

    def get(self, request, *args, **kwargs):
        # HTML with inline styles
        html_content = """
        <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    color: #333;
                    margin: 0;
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                .box {
                    background-color: #ffffff;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    max-width: 600px;
                    width: 100%;
                    text-align: center;
                }
                h1 {
                    color: #4CAF50;
                    margin-bottom: 20px;
                }
                p {
                    font-size: 18px;
                    line-height: 1.6;
                    margin-bottom: 20px;
                }
                a {
                    color: #2196F3;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
                ul {
                    list-style-type: none;
                    padding: 0;
                }
                ul li {
                    margin: 10px 0;
                }
            </style>
        </head>
        <body>
            <div class="box">
                <h1>Hello!</h1>
                <p>I hope you are doing well.</p>
                <p>Please go to the following routes to see the API:</p>
                <ul>
                    <li><a href="/product">/product</a> & <a href="/product/1">/product/1</a></li>
                    <li><a href="/category">/category</a> & <a href="/category/1">/category/1</a></li>
                </ul>
                <p>Thank you for spending your valuable time to review my project ^_^</p>
            </div>
        </body>
        </html>
        """
        return HttpResponse(html_content)
