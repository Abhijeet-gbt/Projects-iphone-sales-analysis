# 📱 iPhone Resale Market Intelligence (EDA Project)

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on iPhone resale market data in the USA.
The goal is to uncover insights about pricing trends, storage impact, geographical variation, and resale patterns.

---

## 📂 Dataset

* File: `iphone_resale_market_intelligence_usa_2026.csv` 
* Contains data about:

  * iPhone models
  * Prices
  * Storage variants
  * Availability & sales
  * US states
  * Discounts
  * Last updated timestamps

---

## 🛠️ Tech Stack

* **Python**
* **Pandas** → Data Cleaning & Manipulation
* **Seaborn & Matplotlib** → Data Visualization

---

## 🔍 Key Steps Performed

### 1. Data Cleaning

* Handled missing values using:

  * Mean (for numerical columns)
  * Mode (for categorical columns)
* Removed duplicates
* Converted date columns into proper datetime format

---

### 2. Feature Engineering

* Extracted **year** from `lastUpdated`
* Converted storage data into numeric format

---

### 3. Data Analysis

* 📊 Average price by iPhone model
* 📍 State-wise price variation
* 📅 Year-wise price trends
* 💾 Storage vs Price relationship
* 🔥 Correlation analysis between variables

---

## 📈 Visualizations

### 📉 Price Trend Over Time

* Line plot showing average resale price across years

### 📊 Price Distribution

* Histogram with KDE to understand pricing spread

### 💾 Storage vs Price

* Bar plot showing how storage affects price

### 📱 Model vs Price (Year-wise)

* Comparison of iPhone models across years

### 🔥 Correlation Heatmap

* Identifies relationships between numerical variables

---

## 📊 Key Insights

* Higher storage variants generally have higher resale value
* Some states show significantly higher average prices
* Price trends vary across years depending on model demand
* Discounts influence resale price distribution

---

## 📸 Sample Outputs

(All graphs are saved as high-quality PNG images)

* `Average iphone resale price over years.png`
* `Distribution of iphone prices.png`
* `Storage(GB) Vs Prices.png`
* `All iPhones model Average prices over years.png`
* `Correlation.png`

---

## ▶️ How to Run

```bash
# Clone repository
git clone https://github.com/your-username/repository-name.git

# Navigate to folder
cd repository-name

# Install dependencies
pip install pandas seaborn matplotlib

# Run the script
python hello.py
```

---

## 🎯 Future Improvements

* Add interactive dashboards using **Plotly / Power BI**
* Build price prediction model (Machine Learning)
* Deploy as web app (Streamlit)

---

## 👨‍💻 Author

**Abhijeet**
Aspiring Data Analyst | Python | EDA | Visualization

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
