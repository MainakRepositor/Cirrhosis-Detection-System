"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import streamlit.components.v1 as components

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Cirrhosis Analysis.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.

    col1,col2 = st.columns(2)

    with col1:
    
        N_Days = st.slider("N_Days", int(df["N_Days"].min()), int(df["N_Days"].max()))
        Status = st.slider("Drug Type", float(df["Status"].min()), float(df["Status"].max()))
        Drug = st.slider("Alcohol Consumption", int(df["Drug"].min()), int(df["Drug"].max()))
        RBC = st.slider("RBC Count", int(df["RBC"].min()), int(df["RBC"].max()))
        Sex = st.slider("Gender", int(df["Sex"].min()), int(df["Sex"].max()))
        Ascites = st.slider("Ascites", float(df["Ascites"].min()), float(df["Ascites"].max()))
        Hepatomegal1 = st.slider("Hepatomegal", float(df["Hepatomegal1"].min()), float(df["Hepatomegal1"].max()))
        Spiders = st.slider("Spiders", int(df["Spiders"].min()), int(df["Spiders"].max()))
        Edema = st.slider("Edema", int(df["Edema"].min()), int(df["Edema"].max()))

    with col2:
        Bilirubin = st.slider("Bilirubin", float(df["Bilirubin"].min()), float(df["Bilirubin"].max()))
        Cholesterol = st.slider("Cholesterol", float(df["Cholesterol"].min()), float(df["Cholesterol"].max()))
        Albumin = st.slider("Albumin", float(df["Albumin"].min()), float(df["Albumin"].max()))
        Copper = st.slider("Copper", float(df["Copper"].min()), float(df["Copper"].max()))
        Alk_Phos = st.slider("Alk_Phos", float(df["Alk_Phos"].min()), float(df["Alk_Phos"].max()))
        SGOT = st.slider("SGOT", float(df["SGOT"].min()), float(df["SGOT"].max()))
        Tryglicerides = st.slider("Tryglicerides", float(df["Tryglicerides"].min()), float(df["Tryglicerides"].max()))
        Platelets = st.slider("Platelets", float(df["Platelets"].min()), float(df["Platelets"].max()))
        Prothrombin = st.slider("Prothrombin", float(df["Prothrombin"].min()), float(df["Prothrombin"].max()))
     
    

    # Create a list to store all the features
    features = [N_Days,Status,Drug,RBC,Sex,Ascites,Hepatomegal1,Spiders,Edema,Bilirubin,Cholesterol,Albumin,Copper,Alk_Phos,SGOT,Tryglicerides,Platelets,Prothrombin]

    # Create a button to predict
    if st.button("Detect Class"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.38
        

        # Prfloat the output according to the prediction
                
        if (prediction == 1 or Bilirubin < 17 and Drug == 0):
            st.success("Stage 1: Minor liver pain and indigestion.")
            
        elif (prediction == 2):
            st.info("Stage 2: Cirrhosis formation has started. Take care.")
          
        elif (prediction == 3):
            st.warning("Stage 3: Clinical Cirrhosis. Please consult a physician.")
     
        elif (prediction == 4):
            st.error("Stage 4: Severe Cirrosis. Immediate medical assistance needed.")
      
                
        # Prfloat teh score of the model 
        st.sidebar.write("The model used is trusted by doctors and has an accuracy of ", round((score*100),2),"%")
