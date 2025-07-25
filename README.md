# 🚆 KPA Wheel Specification & Bogie Checksheet API

A Django-based backend API project for managing Wheel Specifications and Bogie Checksheets, powered by PostgreSQL.

---

## 🛠 Tech Stack

- **Backend**: Django (Django REST Framework)
- **Database**: PostgreSQL
- **Environment Variables**: Managed using `python-decouple`
- **API Testing**: Postman / Thunder Client

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aman235-code/kpa-django-api.git
   cd kpa-django-api
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

4. **Set up PostgreSQL**

   Ensure PostgreSQL is running and execute the following SQL in `psql` or PGAdmin:

   ```sql
   CREATE DATABASE kpa_db;
   CREATE USER kpa_user WITH PASSWORD 'kpa_pass';
   GRANT ALL PRIVILEGES ON DATABASE kpa_db TO kpa_user;

   -- Recommended permissions:
   GRANT ALL ON SCHEMA public TO kpa_user;
   GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO kpa_user;
   GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO kpa_user;
   ```

5. **Create a `.env` file in the root folder** (same level as `manage.py`)
   ```env
   DB_NAME=kpa_db
   DB_USER=kpa_user
   DB_PASSWORD=kpa_pass
   DB_HOST=localhost
   DB_PORT=5432
   ```

6. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

---

## 🔌 API Endpoints

### ✅ 1. Create Wheel Specification
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/forms/wheel-specifications`
- **Description**: Submits a new wheel specification form.
- **Content-Type**: `application/json` 
- **Sample Request**:
  ```json
 { "form_number": "WHEEL-2025-001",
  "submitted_by": "user_id_123",
  "submitted_date": "2025-07-03",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    "condemningDia": "825 (800-900)",
    "wheelGauge": "1600 (+2,-1)",
    "variationSameAxle": "0.5",
    "variationSameBogie": "5",
    "variationSameCoach": "13",
    "wheelProfile": "29.4 Flange Thickness",
    "intermediateWWP": "20 TO 28",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "wheelDiscWidth": "127 (+4/-0)"
  }
}


- **Sample Response**:

  HTTP/1.1 201 Created
  Content-Type: application/json
  {
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03",
    "status": "Saved"
  }
}


### ✅ 2. Get Wheel Specifications
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/forms/wheel-specifications?formNumber=WHEEL-2025-001`
- **Description**: Retrieves the specified wheel specification form.


- **Sample Response**:

 {
  "id": 1,
  "form_number": "WHEEL-2025-001",
  "submitted_by": "user_id_123",
  "submitted_date": "2025-07-03",
  "fields": {
    "wheelGauge": "1600 (+2,-1)",
    "wheelProfile": "29.4 Flange Thickness",
    "condemningDia": "825 (800-900)",
    "wheelDiscWidth": "127 (+4/-0)",
    "intermediateWWP": "20 TO 28",
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    "variationSameAxle": "0.5",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "variationSameBogie": "5",
    "variationSameCoach": "13",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)"
  }
}



### ✅ 3. Create Bogie Checksheet
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/createBasicInfo`
- **Description**: Creats a basic information of the user.
- **Content-Type**: `application/json` 


- **Sample Request**:
 {
  "name": "Aman",
  "phone": "7760873976",
  "email": "aman@example.com",
  "address": "Kolkata, India"
}

- **Sample Response**:

 {
  "id": 1,
  "name": "Aman",
  "phone": "7760873976",
  "email": "aman@example.com",
  "address": "Kolkata, India"
}

### ✅ 4. Get the user basic info by their phone number
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/getBasicInfoByPhoneNumber/7760873976`
- **Description**: Retrieves the user profile based on their phone number.

- **Sample Response**:

 {
  "id": 1,
  "name": "Aman",
  "phone": "7760873976",
  "email": "aman@example.com",
  "address": "Kolkata, India"
}

---

## ⚠️ Assumptions & Limitations

- No authentication (open access for testing).
- CSRF checks are disabled for API testing ease.
- Only minimal validation for demo purposes.
- Database setup must match `.env` values manually.

---

## 🧪 Recommended Tools

- [Postman](https://www.postman.com/)
- [Thunder Client (VS Code Extension)](https://www.thunderclient.com/)

---

## 📄 License

This project is licensed under the **MIT License**.
