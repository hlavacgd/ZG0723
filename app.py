
import streamlit as st
import requests

# Streamlit alkalmazás címe
st.title("Decision Tree Model - Predikció")

# Bemeneti adatok bekérése
st.write("Add meg az adatok jellemzőit:")
age = st.number_input("Age", min_value=0, max_value=100, value=20)
gender = st.selectbox("Gender", options=["Male", "Female"])
admission_test_score = st.number_input("Admission Test Score", min_value=0.0, max_value=100.0, value=50.0)
high_school_percentage = st.number_input("High School Percentage", min_value=0.0, max_value=100.0, value=70.0)
city = st.selectbox("City", options=["City1", "City2", "City3"])  # Példaként

# Konvertálás a modell bemenetéhez szükséges formátumba
gender_encoded = 0 if gender == "Male" else 1
city_encoded = 0 if city == "City1" else 1 if city == "City2" else 2  # Példaként
input_features = [age, gender_encoded, admission_test_score, high_school_percentage, city_encoded]

# Predikció indítása
if st.button("Predikció"):
    response = requests.post("http://127.0.0.1:8000/predict", json={"features": input_features})
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.write(f"A predikció: {'Accepted' if prediction == 1 else 'Rejected'}")
    else:
        st.write("Hiba történt a predikció során.")
    