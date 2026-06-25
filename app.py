import streamlit as st
import numpy as np
import joblib


model = joblib.load("salary_model.pkl")


st.set_page_config(
    page_title="Employee Salary Prediction",
    page_icon="💰",
    layout="centered"
)


st.title("💰 Employee Salary Prediction System")
st.markdown("### Machine Learning Powered Salary Prediction")
st.write(
    "Predict employee salary using Education, Experience, Job Role and Working Hours."
)


age = st.number_input(
    "Age",
    min_value=18,
    max_value=65,
    value=30
)

education = st.selectbox(
    "Education",
    ["High School", "Bachelor", "Master", "PhD"]
)

experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=40,
    value=5
)

job_role = st.selectbox(
    "Job Role",
    [
        "Accountant",
        "Data Analyst",
        "Data Scientist",
        "HR",
        "Manager",
        "Software Engineer"
    ]
)

working_hours = st.number_input(
    "Working Hours Per Week",
    min_value=20,
    max_value=80,
    value=40
)


education_mapping = {
    "Bachelor": 0,
    "High School": 1,
    "Master": 2,
    "PhD": 3
}

job_mapping = {
    "Accountant": 0,
    "Data Analyst": 1,
    "Data Scientist": 2,
    "HR": 3,
    "Manager": 4,
    "Software Engineer": 5
}


if st.button("Predict Salary"):

    employee = np.array([[
        age,
        education_mapping[education],
        experience,
        job_mapping[job_role],
        working_hours
    ]])

    prediction = model.predict(employee)

    st.success(
        f"Predicted Salary: ${prediction[0]:,.2f}"
    )


    st.write("Predicted Value:", round(prediction[0], 2))

    # Salary Category
    st.subheader("Salary Category")

    if prediction[0] < 30000:
        st.warning("Low Salary Range")

    elif prediction[0] < 60000:
        st.success("Medium Salary Range")

    else:
        st.balloons()
        st.success("High Salary Range")

    # Career Suggestions
    st.subheader("Career Suggestions")

    if experience < 5:
        st.info(
            "Gain more experience to improve earning potential."
        )

    if education in ["High School", "Bachelor"]:
        st.info(
            "Pursuing a Master's degree may increase salary opportunities."
        )

    st.info(
        "Recommended Skills: Python, SQL, Power BI, Machine Learning"
    )

    st.info(
        "Continuous learning and certifications can improve career growth."
    )

    
    st.subheader("Employee Summary")

    st.write(f"Age: {age}")
    st.write(f"Education: {education}")
    st.write(f"Experience: {experience} Years")
    st.write(f"Job Role: {job_role}")
    st.write(f"Working Hours: {working_hours}")

    
    report = f"""
Employee Salary Prediction Report

Age: {age}
Education: {education}
Experience: {experience}
Job Role: {job_role}
Working Hours: {working_hours}

Predicted Salary: ${prediction[0]:,.2f}
"""

    st.download_button(
        label="📥 Download Prediction Report",
        data=report,
        file_name="salary_prediction_report.txt",
        mime="text/plain"
    )


st.markdown("---")
st.caption("Adil Malook - Employee Salary Prediction Project")