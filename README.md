# Django REST API with JWT Authentication and PostgreSQL

## Project Setup & Execution Steps

### 1. Clone the Repository
git clone git@github.com:harikrishna0944/customer_api.git
cd customer_api
#### 2. Create Virtual environment 
python3 -m venv venv
source venv/bin/activate
#### Install Dependencies
pip install -r requirements.txt
### Apply Migrations
python manage.py makemigrations
python manage.py migrate
#### Run Development Server
python manage.py runserver 0.0.0.0:8000



# PostgreSQL Database Setup and Django Connection

This project uses **PostgreSQL** as the database backend. Follow the steps below to set up the database and configure the connection in your Django project.

---

## 1. Install PostgreSQL (Ubuntu)

sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql

## 2. Create Database and User
sudo -i -u postgres
psql

##3. Create Database and password
CREATE DATABASE customerdb;
CREATE USER postgres WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE customerdb TO postgres;
\q
exit

##4.Configure Django settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'customerdb',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


