# DecodeLabs Project 2: Backend API Development

This repository contains the second milestone of the DecodeLabs Industrial Training Program (Batch 2026). [cite_start]The objective of this phase is to engineer the "nervous system" of a full-stack web application—a robust backend API that handles application logic, data validation, and seamless communication with the frontend interface[cite: 204, 218, 226].

## 🧠 The Architecture
This API is built using **Django** and adheres strictly to the architectural constraints outlined in the DecodeLabs blueprint. [cite_start]It prioritizes logical consistency over visual flair, ensuring data integrity before any information reaches the persistence layer[cite: 205, 259, 277].

## 🛡️ Core Engineering Principles
* **RESTful Naming:** Strict adherence to resource-based routing. [cite_start]Endpoints use nouns (e.g., `/users/`) and rely on HTTP methods (Verbs) to define the action, avoiding incorrect mutations like `/createUser`[cite: 338, 341, 342, 345, 346, 350].
* [cite_start]**The Gatekeeper Rule:** "Never Trust the Client."[cite: 355, 356]. [cite_start]The application implements dual-layer validation (syntactic format checking and semantic logic verification) to prevent malformed data or pathogens from breaching the database[cite: 357, 360, 361, 362, 365].
* [cite_start]**Semantic Status Codes:** Communicates server state unambiguously using standard HTTP codes (e.g., `200 OK`, `201 Created`, `400 Bad Request`, `500 Internal Error`)[cite: 377, 399, 404, 414].
* [cite_start]**Stateless Communication:** All data exchange is handled via lightweight, machine-parsable JSON payloads[cite: 303, 369, 370].

## 📖 API Blueprint (Endpoints)

### 1. Retrieve All Users
* [cite_start]**Endpoint:** `/users/` [cite: 345]
* [cite_start]**Method:** `GET` [cite: 345]
* [cite_start]**Description:** Safe, idempotent retrieval of the user list[cite: 322].
* **Success Response:** `200 OK`
  ```json
  {
    "status": "success",
    "data": [
      {
        "id": 1,
        "name": "Jane Doe",
        "email": "jane@example.com",
        "role": "user"
      }
    ]
  }
2. Create a UserEndpoint: /users/   Method: POST   Description: Unsafe, non-idempotent creation of a new user resource.  Request Body:JSON{
  "name": "John Doe",
  "email": "john@example.com"
}
Success Response: 201 Created   JSON{
  "status": "success",
  "data": {
    "id": 2,
    "name": "John Doe",
    "email": "john@example.com",
    "role": "user"
  }
}
Error Responses: * 400 Bad Request (Missing fields, invalid JSON, or semantic errors like duplicate emails).
 🚀 Running the API LocallyEnsure Python is installed on your machine.
Clone this repository and navigate to the project directory in your terminal.
Install Django:
pip install django
Run the database migrations to set up the SQLite schema:
Bash
python manage.py migrate
Start the local development server:
Bash
python manage.py runserver
The API is now actively listening for requests.
Architect: Muhammad Qasim Imran
Developed for the DecodeLabs Full Stack Engineering Track.
