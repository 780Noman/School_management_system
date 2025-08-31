---
title: School Management System
emoji: 🏫
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
secrets:
  - SECRET_KEY
  - DJANGO_SUPERUSER_USERNAME
  - DJANGO_SUPERUSER_EMAIL
  - DJANGO_SUPERUSER_PASSWORD
  - ALLOWED_HOSTS
  - CSRF_TRUSTED_ORIGINS
---
# School Management System

## Project Overview

The School Management System is a robust and user-friendly web application built with Django, designed to streamline and enhance the administrative and academic processes within educational institutions. This project aims to provide a centralized platform for managing courses, student registrations, course enrollments, and fees, offering a seamless experience for both students and administrators.

Developed with a focus on security, responsiveness, and an intuitive user interface, this system serves as a testament to modern web development practices and efficient data management.

## Features

* **Dynamic Course Management:** Easily add, view, and manage a catalog of courses, each with a name, description, and associated fee.
* **Secure User Authentication:** Implements a complete authentication flow including:
  * **Registration:** Secure user registration using Django's built-in `User` model, with redirection to login upon successful signup.
  * **Login/Logout:** Robust login and logout functionalities.
  * **Conditional Navigation:** Navbar dynamically displays "Register," "Login," "Logout," and "My Courses" links based on user authentication status.
* **Course Enrollment Logic:**
  * Registered and logged-in students can enroll in specific courses.
  * Prevents duplicate enrollments for the same user in the same course.
  * Provides clear success/error messages for enrollment actions.
  * Redirects unauthenticated users to the registration/login page with an informative message if they attempt to enroll.
* **"My Courses" Section:** Authenticated users can view a personalized list of all courses they are currently enrolled in.
* **Fee Management:** Transparent display of course fees.
* **Responsive & Attractive GUI:**
  * Modern, eye-catching dark theme with a custom color palette (Deep Purple and Light Blue accents).
  * Utilizes Bootstrap 5 for responsive layout and components.
  * Custom CSS for enhanced visual appeal, including card hover effects, styled buttons, and refined typography.
  * Sticky footer ensuring consistent layout across varying content lengths.
  * Optimized for various screen sizes (mobile, tablet, desktop).
* **Dynamic Home Page:** Displays a dynamic list of "Top Courses" fetched directly from the database.
* **Comprehensive "About" Page:** Provides a detailed overview of the project's purpose, features, and development philosophy.

## Technologies Used

* **Backend:** Python 3.12, Django 5.1
* **Database:** SQLite (development), PostgreSQL (production-ready via `dj-database-url`)
* **Frontend:** HTML5, CSS3 (Bootstrap 5, Custom CSS), JavaScript
* **Deployment Utilities:**
  * `python-dotenv`: For managing environment variables.
  * `WhiteNoise`: For serving static files efficiently in production.
  * `dj-database-url`: For flexible database configuration.
  * `Gunicorn`: Production WSGI HTTP Server.
* **Version Control:** Git, GitHub

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

* Python 3.8+
* pip (Python package installer)
* Git

### 1. Clone the Repository

```bash
git clone https://github.com/780Noman/School_management_system
cd schoolproj
```

### 2. Set up Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

Install all required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the root of your `schoolproj` directory (the same level as `manage.py`) and add the following:

```
DEBUG=True
SECRET_KEY='your_django_secret_key_here' # Generate a strong, unique key
ALLOWED_HOSTS=127.0.0.1,localhost
```

* **`SECRET_KEY`**: Replace `'your_django_secret_key_here'` with a strong, randomly generated Django secret key. You can generate one using `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
* **`ALLOWED_HOSTS`**: For local development, `127.0.0.1,localhost` is sufficient. For production, this will be your domain.

### 5. Database Setup

Apply database migrations to create the necessary tables:

```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin Account)

Create an administrator account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your username, email, and password.

### 7. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

* **Home Page (`/`):** Explore the main landing page with a hero section and dynamic "Top Courses."
* **Browse Courses (`/cor/`):** View the full list of available courses.
* **Course Details (`/cor/<course_id>/`):** Click on a course to see its details.
* **Register (`/enroll/reg/`):** Create a new user account. After successful registration, you will be redirected to the login page.
* **Login (`/accounts/login/`):** Log in with your registered credentials.
* **Logout (`/accounts/logout/`):** Log out of your account.
* **Enroll in a Course:** From a course detail page, click "Enroll in this Course." If not logged in, you'll be prompted to register/login.
* **My Courses (`/enroll/my_courses/`):** View all courses you are enrolled in (visible only when logged in).
* **Admin Panel (`/admin/`):** Access the Django administration interface using your superuser credentials to manage users, courses, fees, and enrollments.

## Deployment Considerations

This project is configured for easy deployment to cloud platforms like Render. Key considerations include:

* **Environment Variables:** All sensitive data and configuration (e.g., `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DATABASE_URL`) are managed via environment variables.
* **Static Files:** `WhiteNoise` is integrated for efficient static file serving in production.
* **Database:** Configured to use `dj-database-url` for seamless transition from SQLite (development) to PostgreSQL or other production databases.
* **WSGI Server:** `Gunicorn` is included in `requirements.txt` as the production WSGI server.

## Contributing

Feel free to fork the repository, create feature branches, and submit pull requests.

## License

This project is open-source and available under the [MIT License](LICENSE).

For any questions or feedback, please contact [nomanamjad78600@gmail.com].
