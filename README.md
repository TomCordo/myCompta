# MyCompta Application

## Running the Application

### 1. Set Up the Back End

1. **Navigate to the backend directory:**

    ```bash
    cd backend
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

4. **Install dependencies:**

    ```bash
    pip install fastapi sqlalchemy uvicorn passlib
    ```

5. **Run the FastAPI server:**

    ```bash
    uvicorn app.main:app --reload
    ```

### 2. Set Up the Front End

1. **Navigate to the frontend directory:**

    ```bash
    cd frontend
    ```

2. **Install dependencies:**

    ```bash
    npm install
    ```

3. **Run the React development server:**

    ```bash
    npm start
    ```

The React app will be available at `http://localhost:3000` and the FastAPI server will be available at `http://127.0.0.1:8000`.
