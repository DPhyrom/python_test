import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .models import Product

def extract_features(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        return None

    # Resize the image to a fixed size (e.g., 128x128)
    image = cv2.resize(image, (128, 128))

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the histogram
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # Normalize the histogram
    hist = cv2.normalize(hist, hist).flatten()

    return hist

def precompute_features():
    products = Product.objects.all()
    features = {}

    for product in products:
        if product.image:
            image_path = product.image.path
            hist = extract_features(image_path)
            if hist is not None:
                features[product.id] = hist

    return features

def calculate_similarity(input_features, product_features):
    similarities = {}

    for product_id, product_hist in product_features.items():
        # Reshape the histograms for cosine similarity
        input_hist = input_features.reshape(1, -1)
        product_hist = product_hist.reshape(1, -1)

        # Calculate cosine similarity
        similarity = cosine_similarity(input_hist, product_hist)[0][0]
        similarities[product_id] = similarity

    return similarities