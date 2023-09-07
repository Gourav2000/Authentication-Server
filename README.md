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
- **Main**: `/`
- **Login**: `/login`
- **Signup**: `/signup`
- **Profile Signup**: `/profile_signup`
- **Profile Login**: `/profile_login`
- **Profile**: `/profile`
- **Logout**: `/logout`

## How to Run
1. Clone the repository.
2. Install the required packages.
3. Run `app.py`.
