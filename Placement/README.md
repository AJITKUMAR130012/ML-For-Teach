# Placement Prediction ML Project

This project predicts whether a student will get placed or not based on various features such as IQ and CGPA.

## 📂 Project Files

- `placement.ipynb` – Exploratory Data Analysis (EDA) on student placement data.
- `end_to_end_ml.ipynb` – Complete machine learning pipeline for training the model.
- `placement.csv` – Dataset containing student information.
- `requirement.txt` – Python dependencies.
- `Deployment.py` – Streamlit-based UI using trained model and scaler.

---

## 🚀 How to Run

### ✅ Step 1: Create a Virtual Environment

#### Linux

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

#### Window

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

### ✅ Step 2: Install Requirements

```bash
pip install -r requirement.txt
```

 ### ✅ Step 3: Train the Model
Run end_to_end_ml.ipynb <br>
This will generate:

model.pkl – Trained ML model.

scaler.pkl – Fitted scaler for input preprocessing.

### ✅ Step 4: Launch the UI

```bash
streamlit run Deployment.py
```

### 🖼️ Sample UI

![image](https://github.com/user-attachments/assets/3832c967-2122-4c09-ba9b-876ab4a664bf)




