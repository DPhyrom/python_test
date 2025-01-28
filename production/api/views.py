from django.shortcuts import render
from rest_framework import generics
from api.models import Product, Category
from api.serializers import ProductSerializer, CategorySerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.views import View
from django.http import HttpResponse



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import tempfile
from .models import Product
from .utils import extract_features  # Import the utility function
from .utils import extract_features, precompute_features, calculate_similarity

class ImageSearchAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        # Get the uploaded image
        uploaded_image = request.FILES.get('image')
        if not uploaded_image:
            return Response({"error": "No image uploaded"}, status=400)

        # Save the uploaded image to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            for chunk in uploaded_image.chunks():
                temp_file.write(chunk)
            temp_file_path = temp_file.name

        # Extract features from the uploaded image
        input_features = extract_features(temp_file_path)  # Use the utility function
        if input_features is None:
            return Response({"error": "Invalid image"}, status=400)

        # Precompute features for all products (or load from storage)
        product_features = precompute_features()

        # Calculate similarity
        similarities = calculate_similarity(input_features, product_features)

        # Sort products by similarity score
        sorted_products = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

        # Get the top 10 most similar products
        top_10_products = sorted_products[:10]

        # Fetch product details from the database
        results = []
        for product_id, similarity_score in top_10_products:
            product = Product.objects.get(id=product_id)
            results.append({
                "id": product.id,
                "name": product.name,
                "image": request.build_absolute_uri(product.image.url),
                "price": str(product.price),
                "similarity_score": similarity_score
            })

        return Response(results)













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
