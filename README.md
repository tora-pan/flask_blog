# Flask Blog Application

This is a basic blog application built using Python with Flask framework and PostgreSQL as the database. This will be used for my personal website's blog page eventually if I get around to it

## Features

- User authentication (signup, login, logout)
- Create, edit, and delete blog posts
- PostgreSQL database backend

## Prerequisites

Before running this application, ensure you have the following installed:

- Python (3.7 or higher)
- Flask
- PostgreSQL

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/flask-blog.git
   cd flask-blog

2. **Install dependencies:**

  ```bash
  pip install -r requirements.txt  
  ```

3. **Setup DB:**

  ```bash
  createdb flask_blog_db
  flask db init
  flask db migrate
  flask db upgrade
  ```

4. **Setup ENV vars:**  
  ```
  FLASK_APP=app.py
  FLASK_ENV=development
  DATABASE_URL=postgresql://username:password@localhost/flask_blog_db
  SECRET_KEY=your_secret_key_here  
  ```
4. **Run the application:**  

  ```bash
  flask run
  ```



