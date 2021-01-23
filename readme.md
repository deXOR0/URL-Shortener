# Flask-CS

## About
Flask CS is a template for the Flask Micro Web Framework, the structures is inspired by [Corey Shcafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g)

## Why
Flask is a great framework to create web apps, but the vanilla flask is very basic, in the [documentation](https://flask.palletsprojects.com/en/1.1.x/) and many YouTuber tutorials, they use a single python file for everything from routes, forms, models, etc. Altough this is fine for small web applications, this will get very confusing and messy very quickly once you scale up your web application.

## How it works
I have included some essential modules such as
- SQLAlchemy
- Bcrypt
- Flask-WTF
- WTForms
- Flask-Login
- email-validator
- Flask-Migrate
- Flask-Script

In addition, this template is also equipped with Bootstrap 5

I also structured the template so that everything is laid out nicely. The inspiration for the template structure is taken from one of Corey Schafer's video on Flask, I would highly suggest you to check out his channel if you're new to Python or Flask.

## How to use
- Clone this repository
- Create a virtual environment inside the template's directory
    ```
    python -m venv venv
    ```
- Activate the virtual environment
    ```
    . venv/bin/activate
    ```
- For Windows use
    ```
    . venv\Scripts\activate
    ```
- Install the requirements with 
    ```
    pip install -r requirements.txt
    ```
- Start the project with this command
    ```
    python run.py runserver --debug
    ```

## Prerequisites
- Python 3.x
- pip
- venv
