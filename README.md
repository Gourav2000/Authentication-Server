# Authentication Server

This repository contains a simple authentication server built using Flask. It provides basic functionalities such as user registration, login, and logout.

## Features
- **User Registration**: Allows users to register with email and password.
- **User Login**: Validates user credentials and logs them in.
- **User Logout**: Provides functionality to log out.
- **SQLite Database**: Uses SQLite to store user data.
- **Password Hashing**: Implements password hashing for security.

## Repository Structure
- `app.py`: The main Flask application file.
- `templates/`: Directory containing HTML templates.
  - `login.html`: Login page template.
  - `signup.html`: Signup page template.
- `templates/static/`: Directory for static files like CSS.
- `userdb.db`: SQLite database for user data.

## Endpoints
- `/`: Main endpoint that redirects to the profile or login page based on the session.
- `/login`: Endpoint for user login.
- `/signup`: Endpoint for user registration.
- `/profile_signup`: Endpoint to handle the signup process.
- `/profile_login`: Endpoint to handle the login process.
- `/profile`: Endpoint to display the user's profile.
- `/logout`: Endpoint to log the user out.

## How to Run
1. Clone the repository.
2. Install the required packages.
3. Run `app.py`.
