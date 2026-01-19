
# 📉 Netflix Customer Churn Prediction (End-to-End ML Project)

## 📌 Project Overview

This project is an **end-to-end machine learning application** that predicts whether a Netflix customer is likely to **churn (cancel their subscription)**. The solution is deployed using a **Streamlit-based web interface**, allowing users to input customer details and receive predictions along with **actionable business recommendations**.

## 🎯 Problem Statement

Customer churn is a major challenge for subscription-based platforms like Netflix. Identifying customers who are at risk of leaving helps businesses take **proactive retention actions**, such as discounts, offers, or personalized engagement.

This project focuses on building a churn prediction system that supports **data-driven business decisions**.

## 📊 Dataset

* **Type:** Custom structured dataset (CSV)
* **Target Variable:** `churn`

  * `1` → Customer churned
  * `0` → Customer stayed

### Features Used:

* `watch_time` – Total watch time of the user
* `last_login` – Days since the user last logged in
* `monthly_charges` – Monthly subscription cost

## 🧠 Machine Learning Approach

* **Model Used:** Logistic Regression
* **Preprocessing Steps:**

  * Feature selection
  * Feature scaling using StandardScaler
  * Column validation for data consistency
* **Evaluation Metric:** Accuracy Score

The model outputs:

* **Churn prediction (Yes / No)**
* **Churn probability (%)**

## 💡 Business Recommendations

The application translates ML predictions into **business actions**:

* **If the customer is likely to churn:**

  * Offer personalized discounts
  * Trigger re-engagement notifications
  * Recommend relevant or trending content

* **If the customer is likely to stay:**

  * Provide loyalty rewards
  * Promote premium or long-term subscription plans
  * Encourage referrals

This makes the project **business-focused**, not just model-focused.

## 🖥️ Web Application (Streamlit)

The Streamlit interface allows users to:

* Input customer behavior details
* View churn prediction results
* See churn probability as a percentage
* Check model accuracy
* Receive business recommendations

## 📁 Project Structure

```
netflix_customer_churn/
│
├── app.py              # Streamlit application
├── model.py            # Model training & evaluation logic
├── churn_data.csv      # Custom dataset
├── requirements.txt    # Project dependencies

```

## 🛠️ Tech Stack

**Programming Language**

* Python

**Libraries & Frameworks**

* Streamlit
* Pandas
* NumPy
* Scikit-learn

**Machine Learning**

* Logistic Regression
* StandardScaler
* Train-test split

**Tools**

* VS Code
* GitHub

## 📊 Key Performance Indicators (KPIs)

### 🔹 ML KPIs

* **Accuracy Score** – Measures prediction performance
* **Churn Probability (%)** – Indicates customer churn risk

### 🔹 Business KPIs (Conceptual)

* Churn rate reduction
* Customer retention rate
* Revenue retention
* Offer conversion rate
* Customer lifetime value (CLV) impact

---

## ▶️ How to Run the Project

```bash
pip install -r requirements.txt
streamlit run app.py
```

