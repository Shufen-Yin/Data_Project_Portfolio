# Healthcare Cost Drivers Analysis

## Project Overview
This project explores factors influencing **annual medical costs** using patient demographics, lifestyle habits, chronic conditions, and insurance data. The goal is to identify **high-cost patient groups** and **key cost drivers**, providing actionable business insights for preventive interventions and cost optimization.

## Dataset
- **File:** `data/medical_cost.csv`  
- **Size:** 5,000 patients  
- **Key Features:** age, gender, smoker, BMI, chronic conditions (diabetes, hypertension, heart disease, asthma), physical activity level, daily steps, sleep hours, stress level, doctor visits per year, hospital admissions, medication count, insurance type, insurance coverage %, city type, previous year cost, annual medical cost  
- **Missing Values:** `insurance_type` has 1,048 missing values (~21%), handled in preprocessing by filling with `'Unknown'`  
- **Description:** This dataset contains health, lifestyle, and demographic information used to analyze key drivers of annual medical expenses and identify high-cost patient segments. The dataset is included in the repository for demonstration purposes.

## Tools & Skills
- Python: Pandas, NumPy, Matplotlib, Seaborn  
- Data cleaning & preprocessing (handling missing values, encoding categorical variables)  
- Exploratory Data Analysis (EDA)  
- Feature engineering (e.g., age groups)  
- Business insight extraction  
- Optional: Tableau dashboard for visualization  

## Key Insights
- **Cost concentration:** Annual medical costs are highly **right-skewed** (skewness = 1.68), with the **top 5% of patients (250 individuals exceeding $23,684)** driving a disproportionate share of total spending.  
- **Major cost drivers:** Smoking, chronic conditions (diabetes, hypertension, heart disease, asthma), high BMI, frequent doctor visits, hospital admissions, and medication count.  
- **High-cost patient profile:** Older, overweight, multiple chronic conditions, often smokers — ideal targets for **preventive interventions**.  
- **Moderate factors:** Stress levels and physical activity have some effect; gender and city type are minor drivers.  
- **Smoking insight:** Although smokers are fewer, their **median and upper-quartile annual medical costs are significantly higher** than non-smokers, making smoking an **independent risk factor** for elevated costs.

## 💎 Key Business Takeaways (Diamond Insights)
- **Targeted interventions:** Focus on high-cost patient segments (top 5%) for **maximum ROI**.  
- **Preventive programs:** Chronic disease management and lifestyle interventions (smoking cessation, BMI control) can reduce long-term costs.  
- **Predictive modeling:** Use healthcare utilization metrics (doctor visits, hospital admissions, medication counts) to identify potential high-cost patients.  
- **Insurance optimization:** While high-cost patients exist across all insurance types, coverage strategies can influence utilization patterns.  

## Next Steps
- Build a **predictive model** to identify high-cost patients  
- Explore **longitudinal trends** if multi-year data becomes available  
- Optional: Create a **Tableau dashboard** to communicate key cost drivers visually  

## Project Structure
```
Healthcare_Cost_Analysis/
│
├── notebooks/ # Step-by-step analysis, visualizations, and EDA(Healthcare_cost.ipynb)/PDF
├── data/ # CSV dataset (medical_cost.csv)
├── outputs/ # Key plots and figures (e.g., annual cost distribution, smoker vs cost, high-cost patients)
└── README.md # Project overview, dataset info, key insights, and business takeaways
```

