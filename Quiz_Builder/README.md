# Quiz Builder


##### This is a Python script using the Flask web framework to create a simple quiz application.




This script creates a web-based quiz application where users can view existing quizzes, create new quizzes, and play quizzes with a scoring system. The quiz data is stored in an SQLite database.

it can be broken down into 5 main parts:

## 1. Imports:

Flask: The Flask web framework.
render_template: Used for rendering HTML templates.
request: Provides access to incoming request data.
redirect, url_for: Used for URL redirection.
SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.


## 2. App Configuration and Database Setup:

The Flask app is created and configured to use SQLite as its database (quizzes.db).
An instance of SQLAlchemy (db) is created and associated with the Flask app.
The Quiz class is defined, which represents the model for quizzes in the database. It has columns for id (primary key), questions, options, and answers.


## 3. Routes:

	- / (index):

Retrieves all quizzes from the database and converts them into a dictionary format suitable for rendering in the HTML template.
Renders the index.html template, passing the quizzes data.

	- /create (create_quiz):

Handles both GET and POST requests.
GET: Renders the create.html template.
POST: Processes the form data submitted for creating a new quiz. It generates a unique ID using uuid, extracts questions, options, and answers from the form, creates a new Quiz instance, adds it to the database, and redirects to the index page.

	- /play/<quiz_id> (play_quiz):

Retrieves a specific quiz based on the provided quiz_id.
If the quiz is found:
GET: Renders the play.html template, passing the quiz data.
POST: Processes the submitted answers, compares them with the correct answers, calculates the score, and renders the score.html template with the score.

## 4. Database Initialization and App Run:

The script initializes the database tables by calling db.create_all() within the Flask app context.
The application runs in debug mode if executed directly.


## 5. Templates:

The application uses HTML templates (index.html, create.html, play.html, score.html) for rendering different views.



---------------------------------![Alt Text](https://cssbud.com/wp-content/uploads/2021/05/thanks-for-your-time.gif)---------------------------------------------
