Hello and welcome! Thank you for taking the time to review my project. I truly appreciate your interest and would love to hear your feedback. 😊

## Getting Started

Follow these steps to set up and run the project on your local machine:

1. **Clone the repository**

   ```bash
   git clone https://github.com/DPhyrom/python_test.git

2. **Create a virtual environment** To ensure all dependencies are isolated, create a virtual environment:

   ```bash
   python -m venv myenv

3. **Activate the virtual environment** If you are using Windows:

   ```bash
   .\myenv\Scripts\activate

4. **Install required dependencies** Use pip to install all the modules listed in requirements.txt:

   ```bash
   pip install -r .\requirements.txt


5. **Jump into product folder**

   ```bash
   cd .\production\

6. **Run the server** Start the development server with the following command:

   ```bash
   python .\manage.py runserver

## Demo
Once the server is running, you can access the application in your web browser at http://127.0.0.1:8000/.

![image alt](https://github.com/DPhyrom/python_test/blob/bf6e43b7be96d3dbc34fef9da9c72d3e59737cde/Screenshot%202025-01-28%20102941.png)

- Once you click on /product, it will take you to the next page, which lists all products and allows you to create and filter them.

![image alt](https://github.com/DPhyrom/python_test/blob/feb452df2c6cf314ebe8af4ba104e7cfa20e7d4e/Screenshot%202025-01-28%20104555.png)

- Once you click on /product/1, it will take you to the next page, which displays the product by its ID, and you can also update or delete it.
- About /category and /category/1 they work the same way as /product.

![image alt](https://github.com/DPhyrom/python_test/blob/25de69d4ebf15799fc7335f2172da1bfdfb0f0ee/Screenshot%202025-01-28%20104815.png)

## image search engine
Image search engine: such an interesting concept.
- Use Postman or Insomnia to test.
- In Insomnia, click on Multipart and select Form Data.

![image alt](https://github.com/DPhyrom/python_test/blob/a6275b822221d6a49188e6634788eb1941c647cc/Screenshot%202025-01-28%20114619.png)

- Then, input the variable name (image).
- Select the dropdown icon to choose a file.
- Finally, click to select the image."
- Products will be listed and sorted by similarity score, returning the top 10 most similar products.

![image alt](https://github.com/DPhyrom/python_test/blob/588b5e67f2b89b6fb8a20173f9ba4cf7bb9838f7/Screenshot%202025-01-28%20115519.png)

