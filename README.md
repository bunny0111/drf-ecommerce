# drf-ecommerce

# code to create virtual environment
python3 -m venv env  <!-- env is the environment name -->

# activate environment in Linux/Mac
source env/bin/activate

# activate environment in Windows
env\Scripts\activate

# code to create new project
django-admin startproject drfEcommerce

# code to run the server
python3 manage.py runserver

# code to generate secret_key
import secrets

secret_key = secrets.token_hex(32)  # Generates a 64-character hexadecimal string (32 bytes)
print(secret_key)

# After installation python-dotenv, you can start using python-dotenv in your Python scripts or projects. Remember to create a .env file in your project directory and define your environment variables there. The library will help load those variables into your Python environment.
pip install python-dotenv 1.0.0

# code to install rest_framework
pip install djangorestframework

# code to install pytest
pip install pytest <!-- Pytest is a Python testing framework that originated from the PyPy project. It can be used to write various types of software tests, including unit tests, integration tests, end-to-end tests, and functional tests. Its features include parametrized testing, fixtures, and assert re-writing. -->

# code to install pytest-django
pip install pytest-django