# Multi Author Blog Platform

A modern multi-author blog platform built with Django and PostgreSQL.

## Features

- User registration and authentication
- Login / Logout system
- Create, edit and delete blog posts
- Multi-author support
- Categories and tags
- Comment system
- Image upload for posts
- RSS feed
- Bootstrap 5 dark UI
- PostgreSQL database integration

## Technologies Used

- Python 3
- Django 6
- PostgreSQL
- Bootstrap 5
- HTML5 / CSS3

## Project Structure

multi_avtor/
│
├── posts/
├── comments/
├── users/
├── categories/
├── ai_tools/
├── templates/
├── media/
├── config/
└── manage.py

## Installation

### 1. Clone repository

git clone YOUR_GITHUB_LINK
cd multi_avtor

### 2. Create virtual environment

python -m venv venv

### 3. Activate virtual environment

Windows:

venv\Scripts\activate

Linux / MacOS:

source venv/bin/activate

### 4. Install dependencies

pip install -r requirements.txt

### 5. Configure PostgreSQL database

Update database settings in:

config/settings.py

### 6. Run migrations

python manage.py makemigrations
python manage.py migrate

### 7. Create superuser

python manage.py createsuperuser

### 8. Start server

python manage.py runserver

## RSS Feed

RSS feed is available at:

/rss/

## Screenshots

* Home page
* Post detail page
* Authentication system
* Create post page
* RSS feed

## Future Improvements

* AI-powered post summaries
* Search system
* Pagination
* User profiles
* Like system

## Author

Mariia Komar, TK-31
