# 🧠 Alzheimer's Disease Prediction App

This is a machine learning-based web application that predicts whether a person is likely to have Alzheimer's disease based on clinical health parameters.

The app is designed to be easy to use and provides an intuitive interface built with **Streamlit**.

---

## 📌 Project Overview

Alzheimer's is a progressive brain disorder that affects memory and thinking skills. Early detection plays a key role in patient care and treatment planning.

In this project, we used a dataset with the following features:
- **Functional Assessment**
- **ADL (Activities of Daily Living)**
- **MMSE (Mini-Mental State Examination)**
- **Memory Complaints**

---

## 🔬 Machine Learning Models Tested

We experimented with several ML algorithms to find the most accurate model:

| Model                  | Notes                        |
|------------------------|------------------------------|
| ✅ Random Forest        | Highest accuracy (Selected)  |
| Logistic Regression    | Lower performance            |
| Support Vector Machine | Good but slower              |
| K-Means Clustering     | Used for unsupervised learning comparison |

After evaluating performance, **Random Forest** was chosen for deployment due to its superior prediction accuracy and interpretability.

---

## 🚀 Live Demo (Streamlit Interface)

👉 **Try the app now**:  
[https://alzheimers-prediction-app-ezdxv46kwmvnqjnywyy4e4.streamlit.app/](https://alzheimers-prediction-app-ezdxv46kwmvnqjnywyy4e4.streamlit.app/)

Just input the four medical parameters and click “Predict” to see if the subject is likely to have Alzheimer's.

---

## 🧾 Project Structure

| File/Folder               | Description                                      |
|---------------------------|--------------------------------------------------|
| `app.py`                 | Streamlit frontend code                          |
| `alzheimers_model.pkl`   | Trained Random Forest model                      |
| `requirements.txt`       | Python packages needed to run the app            |
| `Models/`                | Jupyter notebooks for various ML algorithms      |
| `project_description.txt`| Text summary of project goals                    |

---

## 💻 Run the App Locally

### 1. Clone the Repository:
```bash
git clone https://github.com/Tanuja-d/alzheimers-prediction-app.git
cd alzheimers-prediction-app
