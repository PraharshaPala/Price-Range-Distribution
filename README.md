# 🍽️ Price Range Distribution Analysis

## 📌 Project Overview

This project analyzes the **price range distribution of restaurants** using Python and the Pandas library.

The analysis identifies how restaurants are distributed across different price ranges and represents the results using a **bar chart** for easy understanding.

This project is part of a **Data Analysis** practice project using a restaurant dataset.

---

## 🎯 Objectives

The main objectives of this project are:

* Analyze the number of restaurants in each price range.
* Calculate the percentage of restaurants belonging to each price range.
* Visualize the price range distribution using a bar chart.
* Understand the overall pricing pattern of restaurants in the dataset.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data loading and analysis
* **Matplotlib** – Data visualization
* **CSV Dataset** – Restaurant information

---

## 📂 Project Structure

```text
Price-Range-Distribution/
│
├── price_range_distribution.py
├── Dataset.csv
├── price_range_distribution.png
└── README.md
```

---

## 🔍 Analysis Performed

### 1. Load the Dataset

The restaurant dataset is loaded using Pandas:

```python
df = pd.read_csv("Dataset .csv", encoding="latin1")
```

### 2. Count Restaurants by Price Range

The number of restaurants in each price range is calculated using:

```python
price_range_counts = df['Price range'].value_counts().sort_index()
```

### 3. Calculate Percentages

The percentage distribution of restaurants across different price ranges is calculated using:

```python
price_range_percentages = (
    df['Price range'].value_counts(normalize=True).sort_index() * 100
)
```

### 4. Create Visualization

A bar chart is created using Matplotlib to visually represent the number of restaurants in each price range.

```python
price_range_counts.plot(kind='bar')
```

---

## 📊 Output

The project produces:

* The **number of restaurants** in each price range.
* The **percentage distribution** of restaurants.
* A **bar chart** showing the distribution of restaurants across price ranges.

Example:

```text
Price Range  →  Number of Restaurants
     1       →  ███████████████████
     2       →  █████████████████████████
     3       →  ███████████
     4       →  ███
```

*The actual values depend on the dataset used.*

---

## 💡 Key Insights

This analysis can help understand:

* Which price range contains the largest number of restaurants.
* How restaurants are distributed across different pricing categories.
* The overall pricing pattern present in the restaurant dataset.

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project Folder

```bash
cd Price-Range-Distribution
```

### Step 3: Install Required Libraries

```bash
pip install pandas matplotlib
```

### Step 4: Run the Python File

```bash
python price_range_distribution.py
```

The analysis results will be displayed in the terminal and the price range distribution chart will be generated.

---

## 📚 Skills Demonstrated

* Data Loading
* Data Cleaning & Preparation
* Exploratory Data Analysis (EDA)
* Categorical Data Analysis
* Percentage Calculation
* Data Aggregation
* Data Visualization
* Python Programming
* Pandas
* Matplotlib

---

## 🚀 Future Improvements

The project can be extended by:

* Adding more visualizations such as pie charts.
* Comparing price range with restaurant ratings.
* Analyzing price range by city.
* Creating an interactive dashboard using **Power BI** or **Plotly**.
* Adding more detailed statistical analysis.

---

## 👩‍💻 Author

**Pala Praharsha**

B.Tech – Artificial Intelligence & Data Science

---

⭐ If you find this project useful, consider giving the repository a star!
