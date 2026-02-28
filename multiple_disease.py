import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loaing the saved model
diabetes_model = pickle.load(open("diabetes.sav", 'rb'))
heart_disease_model = pickle.load(open("heart_model.sav", 'rb'))
breast_cancer_model = pickle.load(open("breast_cancer_model.sav", 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Breast Cancer Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)
    
# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies')
        Glucose = st.number_input('Glucose Level')
        BloodPressure = st.number_input('Blood Pressure value')
        
    with col2:
        SkinThickness = st.number_input('Skin Thickness value')
        Insulin = st.number_input('Insulin Level')
        BMI = st.number_input('BMI value')
        
    with col3:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
        Age = st.number_input('Age of the Person')
        
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
            
    st.success(diab_diagnosis)
    
# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input('Age of the Person')
        sex = st.number_input('Sex (1 = male, 0 = female)')
        
    with col2:
        cp = st.number_input('Chest Pain types (0-3)')
        trestbps = st.number_input('Resting Blood Pressure')
        
    
    col3, col4  = st.columns(2)
    with col3:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')
        
        
    with col4:
        restecg = st.number_input('Resting Electrocardiographic results (0-2)')
        thalach = st.number_input('Maximum Heart Rate achieved')
        
        
    
    col5, col6 = st.columns(2)    
        
    with col5:
        exang = st.number_input('Exercise Induced Angina (1 = yes; 0 = no)')
        oldpeak = st.number_input('ST depression induced by exercise relative to rest')
        slope = st.number_input('Slope of the peak exercise ST segment (0-2)')
        
        
    with col6:
        
        ca = st.number_input('Number of major vessels (0-3) colored by flourosopy')
        thal = st.number_input('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversable defect)')
        
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
            
    st.success(heart_diagnosis)
    
    
# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        mean_radius = st.number_input('Mean Radius')
        mean_texture = st.number_input('Mean Texture')
        mean_perimeter = st.number_input('Mean Perimeter')
    with col2:
        mean_area = st.number_input('Mean Area')
        mean_smoothness = st.number_input('Mean Smoothness')
        mean_compactness = st.number_input('Mean Compactness')
    with col3:
        mean_concavity = st.number_input('Mean Concavity')
        mean_concave_points = st.number_input('Mean Concave Points')
        mean_symmetry = st.number_input('Mean Symmetry')
    col4, col5, col6 = st.columns(3)
    with col4:
        mean_fractal_dimension = st.number_input('Mean Fractal Dimension')
        radius_error = st.number_input('Radius Error')
        texture_error = st.number_input('Texture Error')
    with col5:
       
        perimeter_error = st.number_input('Perimeter Error')
        area_error = st.number_input('Area Error')
        smoothness_error = st.number_input('Smoothness Error')
        
    with col6:
        compactness_error = st.number_input('Compactness Error')
        concavity_error = st.number_input('Concavity Error')
        concave_points_error = st.number_input('Concave Points Error')
        
    col7, col8, col9 = st.columns(3) 
        
    with col7:
        
        symmetry_error = st.number_input('Symmetry Error')
        fractal_dimension_error = st.number_input('Fractal Dimension Error')
        worst_radius = st.number_input('Worst Radius')
        
    with col8:
        worst_texture = st.number_input('Worst Texture')
        worst_perimeter = st.number_input('Worst Perimeter') 
        worst_area = st.number_input('Worst Area')
        
    with col9:
        worst_smoothness = st.number_input('Worst Smoothness')
        worst_compactness = st.number_input('Worst Compactness')
        worst_concavity = st.number_input('Worst Concavity')
        
    col10, col11,col12 = st.columns(3)
    with col10:
        worst_concave_points = st.number_input('Worst Concave Points')
        
        
    with col11:
        worst_symmetry = st.number_input('Worst Symmetry')
        
    with col12:
        worst_fractal_dimension = st.number_input('Worst Fractal Dimension')
        diab_diagnosis = ''
        
        
# code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Breast Cancer Test Result'):
        breast_cancer_prediction = breast_cancer_model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_error, texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension]])
        
        if breast_cancer_prediction[0] == 1:
            breast_cancer_diagnosis = 'The person is having Breast Cancer'
        else:
            breast_cancer_diagnosis = 'The person does not have any Breast Cancer'
            
    st.success(breast_cancer_diagnosis)
    



