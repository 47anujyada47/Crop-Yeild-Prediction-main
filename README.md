

# 🌾 Crop Yield Prediction with ML  

## 📌 Overview  
This project focuses on predicting crop yield using **machine learning models**. The goal is to analyze how factors like rainfall, fertilizer, and pesticide usage affect agricultural productivity.  

---

## 🎯 Problem Statement  
Predicting crop yield is complex due to fluctuating environmental conditions. Farmers and policymakers need **data-driven insights** to make better decisions and improve efficiency.  

---

## 🚀 Objectives  
- Develop a machine learning model for yield prediction  
- Incorporate environmental and agricultural parameters  
- Deploy the solution via a **Streamlit web app** for real-time use  

---

## 📊 Dataset  
- **Source:** Public agricultural datasets  
- **Features considered:**  
  - Cultivated Area (hectares)  
  - Annual Rainfall (mm)  
  - Fertilizer consumption  
  - Pesticide application  
- **Target variable:**  
  - Yield (tonnes per hectare) 🌱  

---

## 🔍 Exploratory Data Analysis (EDA)  
- Examined dataset structure  
- Checked for missing values  
- Analyzed feature importance  
- Removed sparse or irrelevant categorical fields  

---

## ⚙️ Feature Engineering & Preprocessing  
- Selected key numerical features  
- Filled missing values using **mean imputation**  
- Eliminated invalid/infinite entries  
- Applied **train-test split (80-20)**  

---

## 🤖 Models Implemented  
- **Linear Regression** (baseline)  
- **Decision Tree Regression**  
- **Random Forest Regression** 🌟 (final choice)  

---

## 📈 Model Evaluation  
- **Metric:** R² Score  
- **Best Performer:** Random Forest  
- **Achieved R²:** ~0.13 (moderate accuracy, scope for improvement)  

---

## 🖥️ Deployment  
- Model stored as `.pkl` file  
- Streamlit app built for interactive predictions  
- Users enter values → get instant yield predictions 🌾  

---

## 🛠️ Tech Stack  
- Python 🐍  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Jupyter Notebook  

---

## ▶️ How to Run the Project  
```bash
pip install -r requirements.txt
streamlit run main.py
```

---

