# Django Project Setup Guide


[Deployed link](https://todoreminder.onrender.com/)
## Steps to Run and Test the Project

### 1. Clone the Project Repository
* Clone the repository from GitHub:
  ```bash
  git clone https://github.com/Vipulpatil1704/todoReminder.git
  cd todo
  ```

### 2. Install Dependencies
* Use the `requirements.txt` file to install all necessary libraries:
  ```bash
  pip install -r requirements.txt
  ```

### 3. Run the Project
* Start the Django development server:
  ```bash
  python manage.py runserver
  ```

### 4. Access the Project
* Open your browser and go to:
  ```
  http://127.0.0.1:8000/
  ```

### 5. Test the Project
* Run tests using:
  ```bash
  python manage.py test
  ```

---

## Database Configuration Instructions

If you just want to test the project without setting up a new database, the project is preconfigured to use the following test and development database URLs:

- **Test Database URL:** `mongodb+srv://user:user@cluster0.8byaj.mongodb.net/testdb?retryWrites=true&w=majority&appName=Cluster0`
- **Development Database URL:** `mongodb+srv://user:user@cluster0.8byaj.mongodb.net/todo?retryWrites=true&w=majority&appName=Cluster0&authSource=admin`

### To Use Preconfigured Database
1. Simply run the project as outlined above without changing the database settings.

### To Set Up a New Database
If you want to create and use your own database, follow these steps:

1. **Update Database Configuration**
   - Open `settings.py` and replace the `DATABASES` section with your database connection details:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'djongo',
             'NAME': 'your_database_name',
             'CLIENT': {
                 'host': 'your_host',
                 'port': 27017,
                 'username': 'your_username',
                 'password': 'your_password',
             }
         }
     }
     ```

2. **Apply Migrations**
   - Set up the database schema:
     ```bash
     python manage.py migrate
     ```

3. **Run the Project**
   - Start the server:
     ```bash
     python manage.py runserver
     ```

