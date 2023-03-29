# Forms Clone [Backend]

<a href="https://www.repostatus.org/#wip"><img src="https://www.repostatus.org/badges/latest/wip.svg" alt="Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public." /></a>

## Running the project in local

### 🛠️ Installation

### Backend

1. Create and activate virtual environment

   _Windows:_

   ```sh
   py -3 -m venv ve
   ve\Scripts\activate
   ```

   _macOs/Linux:_

   ```sh
   python3 -m venv ve
   . ve/bin/activate
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```
3. Create an **.env** file and add the credentials
   ```
   MYSQL_HOST = localhost
   MYSQL_USER = user_here
   MYSQL_DATABASE = quick_forms
   MYSQL_PASSWORD = password_here
   MYSQL_PORT = 3306
   ```
4. Create tables into database _(you need to previously create the database)_:
   ```
   python create_tables.py
   ```
5. To run the application:
   ```
   flask --app app --debug run
   ```

[Frontend repo]()
