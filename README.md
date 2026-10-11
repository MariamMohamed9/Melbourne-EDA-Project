# 🏢 Melbourne Housing Market Analysis & Interactive Dashboard

An end-to-end Data Analysis project examining real estate trends, pricing patterns, and seller performances in the Melbourne housing market (2016–2018). This repository includes full Data Cleaning, Exploratory Data Analysis (EDA), statistical insights, and a multi-page interactive dashboard built with Streamlit and Plotly.

---

## 📌 Project Overview
The main objective of this project is to provide actionable business insights for prospective buyers, real estate investors, and market analysts by analyzing property characteristics, regional pricing dynamics, and sales revenue distribution.

---

## 🛠️ Tech Stack & Tools
* *Programming Language:* Python
* *Data Processing & Manipulation:* Pandas, NumPy
* *Data Visualizations:* Plotly Express
* *Missing Value Imputation:* KNN Imputer (Scikit-Learn)
* *Web Dashboard:* Streamlit
* *Version Control:* Git & GitHub

---

## 🧼 Data Exploration & Cleaning Pipeline
1. *Handling Missing Values:*
   * Handled 23% missing price entries using *KNN Imputer* to maintain dataset integrity while using separate strict subsets (successful_sales) for financial metrics to prevent skewing revenue calculations.
2. *Outlier Detection & Removal:*
   * Analyzed extreme outliers across attributes.
   * Identified and dropped an extreme unfeasible outlier (a property with *31 rooms* near CBD with a disproportionately low price). Valid high-value property outliers were preserved.
3. *Feature Engineering:*
   * Extracted Year, Month, YearMonth, and Day from transaction dates.
   * Categorized distance from CBD into intuitive ranges for non-technical stakeholders.

---

## 📊 Key Business Insights
* *Regional Disparities:* Metropolitan regions (specifically *Southern Metropolitan) command significantly higher average property prices compared to Victoria regions (Western Victoria* being the most affordable).
* *Location vs. Price:* Properties within a 0–10 km radius of the Central Business District (CBD) exhibit the highest market values, with price gradually decreasing as distance increases.
* *Correlations:*
  * *Strong Positive Correlation (0.42)* between the number of rooms and property price.
  * *Moderate/Weak Correlation* for distance alone, as pricing is multi-factorial (influenced by property type, suburb, and total area).
* *Revenue & Sales Trends:*
  * *2017* recorded the highest sales volume and annual revenue.
  * Peak sales months occur between *March and May, with lower activity observed in **July* as well as *January and February*.

---

## 🧩 Streamlit Dashboard Structure
The interactive dashboard consists of 3 dedicated pages:
1. *📊 Executive Overview:*
   * High-level KPIs (Total Properties, Total Revenue, Average Price).
   * Regional price metrics displayed in modern card layouts.
   * Side-by-side comparison of *Top 10 Most Expensive vs. Top 10 Most Affordable Suburbs*.
   * Breakdown of sales by property type and top-performing real estate sellers.
2. *🧩 Market Breakdown:*
   * Interactive distributions for *Property Attributes* (Rooms, Distance, Price) and *Sales Attributes* (Type, Method, Suburb).
   * Distance range impact analysis.
3. *🔍 Regional Market Explorer:*
   * Dynamic filtering by regions and custom date ranges with real-time tabular data inspection.
