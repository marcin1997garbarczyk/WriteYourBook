# WriteYourBook

## Project Description

**WriteYourBook** is a web application that allows users to create interactive stories in various genres such as fantasy, romance, children's stories, and crime tales. Users can make decisions at the end of each chapter, which shape the further development of the story. The application supports user registration and login, as well as a coin validation system that users can use to continue their stories.

## Features

- Create interactive stories in various genres
- Users make decisions that affect the course of the story
- User registration and login system
- Coin validation system for continuing stories
- Going back to existing stories and possibility to continue it

## Demo
Register page:
![register.png](imageForReadme%2Fregister.png)

Login page:
![login.png](imageForReadme%2Flogin.png)

Form for creation story:
![form1.png](imageForReadme%2Fform1.png)

Dynamic background change depend on story type:
![form2.png](imageForReadme%2Fform2.png)

Creating first story  based on previous form:
![story1.png](imageForReadme%2Fstory1.png)

Continue story with selecting answer:
![story2.png](imageForReadme%2Fstory2.png)

Go back to all stories and continue one of them:
![myStories.png](imageForReadme%2FmyStories.png)

## Technologies

- **Backend**: Python, Django
- **Frontend**: HTML, JavaScript
- **Database**: SQLite

## Requirements

- Python 3.8+
- Django 3.2+
- SQLite

## Installation

1. Clone the repository

    ```bash
    git clone https://github.com/your-repo/writeyourbook.git
    cd writeyourbook
    ```

2. Create and activate a virtual environment

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Unix systems
    venv\Scripts\activate      # On Windows systems
    ```

3. Install required packages

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations

    ```bash
    python manage.py migrate
    ```

5. Run the development server

    ```bash
    python manage.py runserver
    ```

## Usage

After starting the development server, open your browser and go to `http://127.0.0.1:8000/` to access the application.

Register or log in to start creating your own interactive stories or continue existing ones.

## Project Structure

- `writeyourbook/` - Main Django project directory
  - `frontEndApp/` - Frontend application directory
  - `backEndApp/` - Backend application directory
- `templates/` - HTML templates
- `static/` - Static files (CSS, JavaScript)

## Contribution

All suggestions and contributions are welcome! Please open issues and pull requests on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


---

Created with passion by Marcin Garbarczyk