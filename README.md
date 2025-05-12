# Open Naturalist

Open Naturalist is a web application inspired by [iNaturalist](https://www.inaturalist.org/). It allows users to log and share wildlife sightings, including the animal name and geolocation, and provides user authentication and role-based access to user data.

## Features -- WORK IN PROGRESS

- **User Registration & Login:** Secure authentication using JWT.
- **Wildlife Sightings:** Users can submit sightings with animal name and location.
- **Modern Frontend:** Built with React and Tailwind CSS.
- **REST API:** Flask backend with SQLAlchemy ORM.

## Setup Instructions

### Prerequisites

- Python 3.10+
- Node.js 18+
- [pip](https://pip.pypa.io/en/stable/installation/)
- [npm](https://www.npmjs.com/get-npm)

---

### Backend Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/stan-zapalikov/open-naturalist.git
   cd open-naturalist/backend
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv env
   env\Scripts\activate  # On Windows
   # source env/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy `.env.example` to `.env` and fill in the required values (or set `FLASK_APP=main.py` and your secret keys).

5. **Initialize the database:**
   ```sh
   python
   >>> from main import create_app
   >>> from extensions import db
   >>> app = create_app()
   >>> with app.app_context():
   ...     db.create_all()
   ... 
   >>> exit()
   ```

6. **Run the backend server:**
   ```sh
   flask --app main run
   ```

---

### Frontend

1. **Navigate to the client directory:**
   ```sh
   cd ../client
   ```

2. **Install dependencies:**
   ```sh
   npm install
   ```

3. **Start the development server:**
   ```sh
   npm run dev
   ```

4. **Open your browser:**  
   Visit [http://localhost:5173](http://localhost:5173) (or the port shown in your terminal).

---

## Usage

- **Register/Login:** Use the `/auth/register` and `/auth/login` endpoints to create and authenticate users.
- **Submit Sightings:** Use the frontend form to submit new wildlife sightings.
- **View Sightings:** All sightings are listed on the main page.
- **Staff Endpoints:** The `/users/all` endpoint is restricted to staff users (see `main.py` for staff logic).

---

## Project Structure

```
open-naturalist/
├── backend/
│   ├── auth.py
│   ├── extensions.py
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   ├── schemas.py
│   └── users.py
└── client/
    ├── src/
    │   ├── App.jsx
    │   └── components/
    ├── index.html
    └── package.json
```


