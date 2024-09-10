# Event Management Web Application (Django)

This is a hands-on event management web application developed using **Django**, intended to provide a deep understanding of Django's architecture and how to build web applications using its features.

## Features
- **User Authentication**: Login, Logout, and User Registration using Django's built-in authentication system.
- **Model Handling**: Learn how to manage models and interact with databases efficiently.
- **Forms and ModelForms**: Create and handle forms for user inputs, including custom user forms extending Django's `User` model.
- **CRUD Operations**: Implement Create, Read, Update, and Delete operations on table contents for better comprehension of Django's ORM.
- **File Download**: A module for downloading content as PDF, CSV, and text files.
- **Static & Media Files**: Gain insights on handling static files (CSS, JS) and media files (images, documents).
- **Template Tags**: Master the use of Django's template system to create dynamic and reusable HTML.

## Getting Started

### Prerequisites
- Python 3.x
- Git
- Virtualenv

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/event-management.git
   cd event-management


### 2. **Create a Virtual Environment**:
```bash
   python -m venv env
   On Mac use     - source env/bin/activate
   On Windows use - `env\Scripts\activate`


### 3. Install Dependencies: Install the required packages from requirements.txt:
- Open Cmd and move on to you virtual environment
-  ```bash
      pip insall -r requirements.txt .

### 4. Run Migrations:
- Open Cmd and move on to you virtual environment 
- type   `python manage.py migrate` .

### 5. Start the Server:
- Open Cmd and move on to you virtual environment 
- type  `python manage.py runserver` .

### 5. Acces the Application:
- copy & paste the url in browser `http://127.0.0.1:8000/` 


## Project Structure
- **Authentication**: User login, logout, and registration.
- **CRUD Operations**: Manage event data using models and forms.
- **File Downloads**: Export data to PDF, CSV, or text files.
- **Templates**: Custom templates with reusable blocks and static files handling.
  
## Acknowledgments and Gratitude
- Codemy YouTube Channel: For a hands-on approach to learning Django.
- Corey Schafer YouTube Channel: For deep dives into Django concepts and best practices.
