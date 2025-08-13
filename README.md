# Diabetes Prediction App (Frontend)

The **Diabetes Prediction App** is a web-based frontend built with **Streamlit** that allows users to input patient health data and receive real-time diabetes predictions. It communicates with a backend **FastAPI** service powered by a trained machine learning model.

---

## Features

- Interactive and intuitive user interface
- Input patient metrics including glucose, BMI, age, and more
- Real-time prediction of diabetes risk (Diabetic / Not Diabetic)
- Confidence score displayed for each prediction
- Connects directly to the backend API

---

## 🛠️ Tech Stack

| Layer       | Technology     |
|-------------|----------------|
| Frontend    | Streamlit      |
| Backend API | FastAPI        |

## Technologies Used

- **Streamlit** for frontend UI
- **Python 3** for application logic
- **Requests** library for API communication

---

## Project Structure
```bash
frontend/
│
├── frontend.py           # Streamlit frontend application
└── requirements.txt      # Python dependencies
README.md                 # Documentation for the frontend project (located outside this folder)
```

---

## Dataset Reference
- The app uses predictions from the **Pima Indians Diabetes Dataset model** trained in the backend
- Dataset link: [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---

## Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/Farhan00000000/diabetes-prediction-app.git
   cd diabetes-prediction-app

   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run frontend.py
   ```
5. Make sure the API_URL in frontend.py points to the deployed backend API:
   ```bash
   API_URL = "https://diabetes-prediction-api-frontend.onrender.com/predict"
   ```
   
   ---

## Live Deployment
- Streamlit frontend app: [https://diabetes-prediction-app-4smzcurnuqvwawcwbmnjhs.streamlit.app](https://diabetes-prediction-app-4smzcurnuqvwawcwbmnjhs.streamlit.app)
- Backend API: [Backend API: https://diabetes-prediction-api-frontend.onrender.com](https://diabetes-prediction-api-frontend.onrender.com)

---

## GitHub Repository
- Backend repo: [Diabetes-Prediction-API-Frontend](https://github.com/Farhan00000000/Diabetes-Prediction-API-Frontend.git)
- Frontend repo: [diabetes-prediction-app](https://github.com/Farhan00000000/diabetes-prediction-app.git)

---

## Author
[Farhan00000000](https://github.com/Farhan00000000)

---

## License
This project is open-source and available under the MIT License.

---

## This README includes:
- Description, features, technologies
- Project structure
- Dataset reference
- Local setup instructions
- Deployment links
- GitHub repository links








