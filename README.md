# EV-Range-and-Battery-Health-Prediction

#Project Overview
This project focuses on predicting two key performance metrics of electric vehicles:

Driving Range (in kilometers)

Battery Health (as a performance or degradation indicator)

Using machine learning techniques, the project analyzes electric vehicle specifications such as battery capacity, energy efficiency, charging rate, and model characteristics to estimate how far an EV can travel on a full charge and how its battery health changes over time or usage.

#Objectives
• Predict the driving range of electric vehicles using their technical specifications.
• Evaluate the battery health and performance efficiency based on historical and specification data.
• Identify the most influential factors affecting EV range and battery degradation.
• Support the development of data-driven insights for electric vehicle design and optimization.

#Problem Statement
The challenge addressed in this project is to build reliable machine learning models that can forecast the driving range and assess the battery health of electric vehicles.
Accurate predictions in these areas can help manufacturers improve EV design, assist consumers in understanding battery performance, and promote sustainable mobility solutions.

#Dataset Information
Dataset Name: Electric Vehicle Specs Dataset (2025)
Source: Kaggle (or any open EV dataset)
Key Attributes:
• Brand and Model
• Battery Capacity (kWh)
• Range (km)
• Efficiency (Wh/km)
• Charging Rate (kW)
• Price (€)
• Battery Health or Degradation Percentage (if available)

#Workflow

Data Collection – Importing and inspecting the dataset.

Data Cleaning – Handling missing values, removing duplicates, and correcting data types.

Exploratory Data Analysis – Understanding relationships among EV features through visualizations.

Feature Engineering – Selecting and transforming relevant variables for model training.

Model Building – Training regression and predictive models to estimate range and battery health.

Evaluation – Comparing model performance using metrics such as R² score, MAE, and RMSE.

Future Integration – Deploying models using Streamlit or Flask for user interaction.

#Tools and Technologies Used
Programming Language: Python
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
Environment: Jupyter Notebook or Google Colab
Visualization Tools: Seaborn and Matplotlib

#Key Insights (from EDA and Modeling)
• Battery capacity has a strong positive correlation with range.
• Efficiency and vehicle weight significantly influence range prediction.
• Models with optimized parameters (like Random Forest or Gradient Boosting) perform well.
• Battery health prediction can be improved by including temperature and usage data in future versions.

#Next Steps
• Enhance model accuracy using deep learning or hybrid models.
• Integrate real-world usage data for better battery health forecasting.
• Develop an interactive dashboard or web app for predictions using Streamlit.
