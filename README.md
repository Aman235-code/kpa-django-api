# 🚆 KPA Wheel Specification & Bogie Checksheet API

A Django-based backend API project for managing Wheel Specifications and Bogie Checksheets, powered by PostgreSQL.

---

## 🛠 Tech Stack

- **Backend**: Django (REST Framework)
- **Database**: PostgreSQL
- **Environment Variables**: `.env` file using `python-decouple`
- **API Testing**: Postman / Thunder Client

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/kpa-api.git
   cd kpa-api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**

   Make sure PostgreSQL is running and create a database/user with these `.env` values:

   Then create the database and user (adjust as needed):

   ```sql
   CREATE DATABASE kpa_db;
   CREATE USER kpa_user WITH PASSWORD 'kpa_pass';
   GRANT ALL PRIVILEGES ON DATABASE kpa_db TO kpa_user;

   -- Additional recommended permissions:
   GRANT ALL ON SCHEMA public TO kpa_user;
   GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO kpa_user;
   GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO kpa_user;


   ```
   DB_NAME=kpa_db
   DB_USER=kpa_user
   DB_PASSWORD=kpa_pass
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

---

## 🔌 API Endpoints

### 1. **Create Wheel Specification**
- **Endpoint**: `POST /api/wheel-specs/`
- **Description**: Submits a new wheel specification form.
- **Request Body**:
  ```json
  {
    "form_number": "WS001",
    "submitted_by": "Engineer A",
    "submitted_date": "2025-07-25"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Wheel specification submitted successfully.",
    "data": {
      "formNumber": "WS001",
      "submittedBy": "Engineer A",
      "submittedDate": "2025-07-25",
      "status": "Saved"
    }
  }
  ```

---

### 2. **Get All Wheel Specifications**
- **Endpoint**: `GET /api/wheel-specs/`
- **Description**: Retrieves all submitted wheel specification forms.

---

### 3. **Create Bogie Checksheet**
- **Endpoint**: `POST /api/bogie-checksheets/`
- **Description**: Submits a bogie checksheet record.

---

### 4. **Get All Bogie Checksheets**
- **Endpoint**: `GET /api/bogie-checksheets/`
- **Description**: Retrieves all bogie checksheet submissions.

---

## ⚠️ Assumptions & Limitations

- No authentication system is implemented (Open API).
- CSRF checks are bypassed for API testing with Postman or Thunder Client.
- No frontend UI; this project only exposes backend APIs.
- Validation assumes minimal required fields for demo purposes.

---

## ✅ Environment Setup Notes

Make sure your `.env` file is present at the root level with the following:

```env
DB_NAME=kpa_db
DB_USER=kpa_user
DB_PASSWORD=kpa_pass
DB_HOST=localhost
DB_PORT=5432
```

---

## 🧪 Recommended Tools

- [Postman](https://www.postman.com/)
- [Thunder Client (VS Code extension)](https://www.thunderclient.com/)

---

## 📄 License

MIT License
