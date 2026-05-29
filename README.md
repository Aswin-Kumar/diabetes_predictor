# 🩺 Dr.AI - Diabetes Prediction System

A web-based diabetes prediction application powered by Machine Learning. This project uses a Support Vector Machine (SVM) classifier to predict diabetes based on medical parameters, providing an intuitive and modern user interface for health insights.

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Model Details](#model-details)
- [Frontend Features](#frontend-features)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **AI-Powered Prediction**: Uses SVM (Support Vector Machine) classifier for accurate diabetes prediction
- **Modern Web Interface**: Beautiful, responsive UI with dark/light mode toggle
- **Real-time Analytics Dashboard**: Visualize health trends with interactive charts
- **RESTful API**: Clean API endpoint for predictions
- **Input Validation**: Comprehensive error handling and validation
- **Health Recommendations**: Personalized recommendations based on prediction results

## 🛠 Technology Stack

### Backend
- **Python 3.x**: Core programming language
- **Flask**: Web framework for API and server
- **scikit-learn**: Machine learning library (SVM classifier)
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with animations and gradients
- **JavaScript (ES6+)**: Client-side interactivity
- **Chart.js**: Data visualization for analytics dashboard

## 📁 Project Structure

```
diabetes_prediction/
│
├── backend/
│   ├── app.py                 # Flask application and API routes
│   ├── predict_model.py       # ML model training and prediction logic
│   └── diabetes.csv           # Training dataset
│
├── frontend/
│   ├── index.html             # Main prediction page
│   ├── dashboard.html         # Analytics dashboard
│   ├── script.js              # JavaScript functionality
│   └── style.css              # Styling and animations
│
├── venv/                      # Python virtual environment
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Web browser (Chrome, Firefox, Safari, or Edge)

### Step-by-Step Setup

1. **Clone or navigate to the project directory**
   ```bash
   cd diabetes_prediction
   ```

2. **Create a virtual environment** (if not already created)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Verify the dataset exists**
   - Ensure `backend/diabetes.csv` is present in the project

## 💻 Usage

### Starting the Application

1. **Activate the virtual environment** (if not already activated)
   ```bash
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # macOS/Linux
   ```

2. **Run the Flask server**
   ```bash
   cd backend
   python app.py
   ```

3. **Access the application**
   - Open your web browser and navigate to: `http://127.0.0.1:5000`
   - The application will automatically load the prediction interface

### Making Predictions

1. **Fill in the required medical parameters:**
   - Pregnancies: Number of pregnancies
   - Glucose: Plasma glucose concentration (mg/dL)
   - Blood Pressure: Diastolic blood pressure (mm Hg)
   - Skin Thickness: Triceps skin fold thickness (mm)
   - Insulin: 2-Hour serum insulin (mu U/ml)
   - BMI: Body Mass Index (weight in kg/(height in m)²)
   - Diabetes Pedigree Function: Diabetes pedigree function
   - Age: Age in years

2. **Click the "🔍 Predict" button**

3. **View the results:**
   - The prediction will display whether the person is "Diabetic" or "Not Diabetic"
   - Health recommendations will appear based on the result

4. **Access Analytics Dashboard:**
   - Click "📊 View Analytics Dashboard" to see visual health trends

## 📡 API Documentation

### Base URL
```
http://127.0.0.1:5000
```

### Endpoints

#### 1. GET `/`
- **Description**: Serves the main prediction page
- **Response**: HTML page (`index.html`)

#### 2. POST `/api/predict`
- **Description**: Predicts diabetes based on input parameters
- **Request Body**:
  ```json
  {
    "inputs": [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree, age]
  }
  ```
- **Example Request**:
  ```json
  {
    "inputs": [6, 148, 72, 35, 0, 33.6, 0.627, 50]
  }
  ```
- **Success Response** (200):
  ```json
  {
    "prediction": "Diabetic"
  }
  ```
  or
  ```json
  {
    "prediction": "Not Diabetic"
  }
  ```
- **Error Responses**:
  - `400 Bad Request`: Missing or invalid input
    ```json
    {
      "error": "Exactly 8 numeric values required"
    }
    ```
  - `500 Internal Server Error`: Server-side error
    ```json
    {
      "error": "Error message"
    }
    ```

### Example API Usage (cURL)

```bash
curl -X POST http://127.0.0.1:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"inputs": [6, 148, 72, 35, 0, 33.6, 0.627, 50]}'
```

### Example API Usage (Python)

```python
import requests

url = "http://127.0.0.1:5000/api/predict"
data = {
    "inputs": [6, 148, 72, 35, 0, 33.6, 0.627, 50]
}

response = requests.post(url, json=data)
result = response.json()
print(result["prediction"])
```

## 🤖 Model Details

### Algorithm
- **Type**: Support Vector Machine (SVM)
- **Kernel**: Linear
- **Library**: scikit-learn

### Training Process
1. **Data Loading**: Loads diabetes dataset from `diabetes.csv`
2. **Preprocessing**: Standardizes features using `StandardScaler`
3. **Train-Test Split**: 80% training, 20% testing with stratification
4. **Training**: Trains SVM classifier on standardized data
5. **Evaluation**: Calculates accuracy on training and test sets

### Model Performance
- The model prints training and test accuracy when initialized
- Typical accuracy: ~75-80% (varies based on dataset)

### Input Features (8 parameters)
1. Pregnancies
2. Glucose
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. BMI
7. Diabetes Pedigree Function
8. Age

### Output
- `"Diabetic"`: Person is predicted to have diabetes (class 1)
- `"Not Diabetic"`: Person is predicted to not have diabetes (class 0)

## 🎨 Frontend Features

### Main Page (`index.html`)
- **Input Form**: 8 input fields for medical parameters
- **Prediction Button**: Triggers API call and displays results
- **Result Display**: Shows prediction with color-coded results
- **Health Recommendations**: Personalized advice based on prediction
- **Dark/Light Mode Toggle**: Switch between themes
- **Navigation**: Link to analytics dashboard

### Analytics Dashboard (`dashboard.html`)
- **Trend Chart**: Line chart showing diabetes risk trends
- **Distribution Chart**: Bar chart showing population distribution
- **Interactive Visualizations**: Powered by Chart.js
- **Responsive Design**: Works on desktop and mobile devices

### Styling Features
- Gradient background animations
- Glassmorphism effects (backdrop blur)
- Smooth transitions and hover effects
- Responsive grid layout
- Modern typography (Poppins font)

## 🔧 Development

### Running in Development Mode

The Flask app runs in debug mode by default:
```python
app.run(debug=True)
```

This enables:
- Automatic reloading on code changes
- Detailed error messages
- Debug console

### Modifying the Model

To change the ML model or parameters, edit `backend/predict_model.py`:

```python
# Change kernel type
classifier = svm.SVC(kernel='rbf')  # or 'poly', 'sigmoid'

# Adjust train-test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, stratify=Y, random_state=2
)
```

### Adding New Features

1. **Backend**: Add new routes in `app.py`
2. **Frontend**: Update HTML/CSS/JS files in `frontend/`
3. **Model**: Modify `predict_model.py` for ML changes

## 📝 Notes

- **Medical Disclaimer**: This application is for educational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.
- **Data Privacy**: All predictions are processed locally. No data is stored or transmitted to external servers.
- **Model Limitations**: The accuracy depends on the training dataset. For production use, consider:
  - Larger, more diverse datasets
  - Model validation and cross-validation
  - Regular model retraining
  - Additional feature engineering

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Developed with Flask + Machine Learning

## 🙏 Acknowledgments

- scikit-learn community for ML tools
- Flask team for the web framework
- Chart.js for visualization capabilities

---

**🏥 Powered by AI • Developed with Flask + Machine Learning**

