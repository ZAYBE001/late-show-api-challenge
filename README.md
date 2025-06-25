# late-show-api-challenge# Late Show API

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Authentication Flow](#authentication-flow)
- [Route List](#route-list)
- [Postman Usage Guide](#postman-usage-guide)
- [GitHub Repository Link](#github-repository-link)

## Setup Instructions

### Prerequisites
- **PostgreSQL**: Ensure PostgreSQL is installed and running.
- **Python 3.8+**: Ensure Python 3.8 or higher is installed.
- **pipenv**: Ensure pipenv is installed. You can install it using `pip install pipenv`.

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/late-show-api-challenge.git
   cd late-show-api-challenge

### Set Environment Variables:
* Create a .env file in the root directory and set the necessary environment variables:
  env
  Copy

* FLASK_APP=server/app.py
* FLASK_ENV=development
* DATABASE_URL=postgresql://username:password@localhost:5432/late_show_db
* SECRET_KEY=your_secret_key
* JWT_SECRET_KEY=your_jwt_secret_key

## Set Environment Variables:
Create a .env file in the root directory and set the necessary environment variables:
env


```bash  
FLASK_APP=server/app.py
FLASK_ENV=development
DATABASE_URL=postgresql://username:password@localhost:5432/late_show_db
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key