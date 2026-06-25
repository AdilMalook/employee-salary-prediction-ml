Employee Salary Prediction Using Machine Learning
Project Overview
This project predicts employee salaries based on various factors such as:
•	Age
•	Education Level
•	Years of Experience
•	Job Role
•	Working Hours
The project applies Machine Learning techniques to analyze employee data, compare multiple regression models, and predict salary accurately. A Streamlit web application is also developed to allow users to interact with the trained model.
________________________________________
Objectives
•	Perform Data Cleaning and Preprocessing
•	Conduct Exploratory Data Analysis (EDA)
•	Train Multiple Machine Learning Models
•	Compare Model Performance
•	Build a Salary Prediction Web Application
•	Generate AI-Based Career Insights
________________________________________
Dataset
Dataset File:
employee_salary_dataset_records.csv
Features:
Feature	Description
Age	Employee age
Education	Education level
Experience	Years of experience
JobRole	Employee job role
WorkingHours	Weekly working hours
Salary	Target variable
Total Records: 200
________________________________________
Data Preprocessing
The following preprocessing steps were performed:
•	Duplicate removal
•	Data validation
•	Label Encoding
•	Feature selection
•	Train-Test Split
________________________________________
Exploratory Data Analysis
EDA includes:
•	Salary Distribution
•	Experience vs Salary
•	Age vs Salary
•	Education Impact on Salary
•	Job Role Salary Analysis
•	Correlation Heatmap
•	Experience Group Analysis
________________________________________
Machine Learning Models
The following regression models were trained:
1. Linear Regression
Used as the baseline model.
2. Decision Tree Regressor
Captures nonlinear relationships.
3. Random Forest Regressor
Provides improved accuracy and robustness.
________________________________________
Model Evaluation Metrics
Models were evaluated using:
•	Mean Absolute Error (MAE)
•	Mean Squared Error (MSE)
•	Root Mean Squared Error (RMSE)
•	R² Score
________________________________________
Best Model
Random Forest Regressor achieved the highest performance and was selected as the final model.
Saved Model:
salary_model.pkl
________________________________________
Streamlit Web Application
Features:
•	User-friendly interface
•	Salary prediction
•	Interactive inputs
•	Real-time results
•	Career recommendations
Run Application:
streamlit run app.py
________________________________________
Extra Enhancements
Feature Importance Analysis
Identifies which features contribute most to salary prediction.
Correlation Heatmap
Visualizes relationships among numerical variables.
Experience Group Analysis
Analyzes salary trends across experience ranges.
Career Recommendations
Provides suggestions for improving salary potential.
Salary Category Classification
Categorizes salaries into:
•	Low Salary
•	Medium Salary
•	High Salary
________________________________________
Technologies Used
•	Python
•	Pandas
•	NumPy
•	Matplotlib
•	Seaborn
•	Scikit-Learn
•	Joblib
•	Streamlit
________________________________________
Project Structure
Employee_Salary_Prediction/
├── employee_salary_dataset_records.csv
├── Task 6.ipynb
├── salary_model.pkl
├── app.py
├── requirements.txt
├── README.md
└── Screenshots/
________________________________________
Future Work
•	Integration with real-world salary datasets
•	XGBoost implementation
•	Hyperparameter tuning
•	Deployment on Streamlit Cloud
•	Integration with Gemini/OpenAI APIs
•	Salary trend forecasting
________________________________________
Author
Adil Malook
Employee Salary Prediction Using Machine Learning
