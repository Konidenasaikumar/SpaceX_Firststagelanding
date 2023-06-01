import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import pickle
from streamlit_option_menu import option_menu
import base64


# Set page configuration
st.set_page_config(layout='wide')

# Create option menu
selected = option_menu(
    menu_title=None,
    options=['Home', 'Project', 'Contact'],
    icons=['house', 'book', 'envelope'],
    menu_icon=':rocket:',
    default_index=0,
    orientation='horizontal'
)

# Styling
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #00FFFF;
    }
    
    .section-title {
        font-size: 24px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 10px;
        color: #00FF00;
    }
    
    .content {
        font-size: 18px;
        margin-bottom: 20px;
    }
    
    .menu-container {
        background-color: #F9F9F9;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    
    .menu-item {
        display: inline-block;
        margin-right: 20px;
    }
    
    .menu-item a {
        text-decoration: none;
        font-size: 20px;
        padding: 10px 15px;
        border-radius: 5px;
        color: #FFF;
    }
    
    .menu-item a:hover {
        background-color: #2196F3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if selected == 'Home':
    st.markdown("<h1 class='title'>SpaceX Falcon 9 First Stage Landing Prediction</h1>", unsafe_allow_html=True)

    with open('Images/image.png', "rb") as file:
        image_data = file.read()

    image_base64 = base64.b64encode(image_data).decode()

    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/jpeg;base64,{image_base64}" width="500">
        </div>
        """,
        unsafe_allow_html=True
)



    st.markdown("""
        <div class='section-title'>Introduction</div>
        <div class='content'>
        This project aims to predict whether the first stage of the Falcon 9 rocket will successfully land. The ability to accurately predict the landing outcome is crucial as it directly impacts the cost of a launch. SpaceX, known for its cost-effective operations, advertises Falcon 9 rocket launches on its website with a price tag of 62 million dollars, significantly lower than other providers whose costs can go up to 165 million dollars per launch. This cost advantage is largely due to SpaceX's ability to reuse the first stage of the Falcon 9 rocket.
        </div>
        
        <div class='section-title'>Objective</div>
        <div class='content'>
        The primary objective of this project is to develop a prediction model that can determine if the first stage of the Falcon 9 rocket will land successfully. By accurately predicting the landing outcome, we can estimate the cost of a launch. This information will be valuable for alternate companies planning to bid against SpaceX for a rocket launch, allowing them to assess the cost competitiveness of their proposals.
        </div>
        
        <div class='section-title'>Dataset</div>
        <div class='content'>
        The dataset used for this project consists of historical data related to Falcon 9 launches. It includes various features such as launch date, mission details, technical specifications, and the landing outcome of the first stage. The dataset will be utilized to train and evaluate the prediction model.
        </div>
    """, unsafe_allow_html=True)

if selected == 'Project':

    st.markdown("<h1 class='title'>Falcon 9 First Stage Landing Prediction</h1>", unsafe_allow_html=True)
    with st.container():
        st.write("<div class='section-title'>Choose the parameters to predict the first stage landing 🚀</div>", unsafe_allow_html=True)
        categorical_features = ['BoosterVersion', 'Orbit', 'LaunchSite', 'GridFins', 'Reused', 'Legs']
        numerical_features = ['Block']
        BoosterVersion= 'Falcon 9'
        Orbit= st.selectbox(
        'Which orbit are you aiming to launch?',
        ('LEO', 'ISS', 'PO', 'GTO', 'ES-L1', 'SSO', 'HEO', 'MEO', 'VLEO','SO', 'GEO'), help='Each launch aims to an dedicated orbit, and here are some common orbit types:LEO Low Earth orbit (LEO), VLEO: Very Low Earth Orbits (VLEO), GTO-A geosynchronous orbit ns and surveillance, SSO (or SO): It is a Sun-synchronous orbit , ES-L1 : placed in orbit there is in equilibrium relative to the center of mass, HEO- A highly elliptical orbit, ISS- A modular space station (habitable artificial satellite) in low Earth orbit, MEO-Geocentric orbits ,HEO -Geocentric orbits,GEO- It is a circular geosynchronous orbit, PO ')
        LaunchSite=st.selectbox(
        'Choose the launch site?',
        ('CCSFS SLC 40', 'VAFB SLC 4E', 'KSC LC 39A'), help='The data contains several Space X  launch facilities, For reference-"https://en.wikipedia.org/wiki/List_of_Cape_Canaveral_and_Merritt_Island_launch_sites?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork865-2023-01-01"')
        GridFin=st.selectbox(
        "Whether the rocket's first stage has Grid Fins?",
        ('Yes', 'No'),help='Grid fins are aerodynamic surfaces attached to the rocket that help stabilize it during descent and landing')
        Gridfins=''
        if GridFin=='Yes':
            GridFins='True'
        else:
            GridFins='False'
        Reusedd=st.selectbox(
        "whether the rocket's first stage has been reused?",
        ('Yes', 'No'), help=' If the value is "True," it means the first stage has been previously flown and recovered for reuse. If the value is "False," it means the first stage is being used for the first time.')
        Reused=''
        if Reusedd=='Yes':
            Reused='True'
        else:
            Reused='False'
        Leg=st.selectbox(
        "whether the rocket's first stage has landing legs?",
        ('Yes', 'No'), help=' If the value is "True," it means the first stage has been previously flown and recovered for reuse. If the value is "False," it means the first stage is being used for the first time.')
        Legs=''
        if Leg=='Yes':
            Legs='True'
        else:
            Legs='False'
        #LandingPad=st.selectbox(
        #   "Which landing pad was used for rocket's first stage landing?",
        #  ('5e9e3032383ecb6bb234e7ca', '5e9e3032383ecb761634e7cb','5e9e3032383ecb267a34e7c7', '5e9e3033383ecbb9e534e7cc','5e9e3032383ecb554034e7c9'),help='It provides information about the specific location where the rocket successfully landed after its mission.')
        Block=st.selectbox(
            'What is the version or block of Falcon 9 rocket?', (1.0,2.0,3.0,4.0,5.0), help='The "Block" column refers to the version or block of the Falcon 9 rocket. SpaceX divides the Falcon 9 rockets into different blocks, each representing a specific version or iteration of the rocket design. Higher block numbers usually indicate newer versions or upgrades of the Falcon 9 rocket. Tracking the block number can provide insights into the evolution of the Falcon 9 design and any performance improvements over time.')
        PayloadMass=st.slider('Enter the Payload mass in kg', min_value=300.0, max_value=20000.0, value=750.0, step=50.0, help='The Payload Mass refers to the mass of the payload carried by the Falcon 9 rocket for each launch. It represents the total mass of the payload, including any satellites, cargo, or other objects being transported into space.') 
        #Calling the model object with the help of pickle module(Model used is Logistic Regression))
        with open('model_pickle', 'rb') as f:
            mp=pickle.load(f)
        #Taking input into dictionary
        dict= {'BoosterVersion':BoosterVersion , 'Orbit':Orbit , 'LaunchSite': LaunchSite,'Reused':Reused, 'GridFins': GridFins, 'Legs': Legs}
        dict1={'Block':Block, 'PayloadMass':PayloadMass}
        df1= pd.DataFrame(dict, index=[0])
        df2= pd.DataFrame(dict1, index=[0])

        #st.write(df1)
        #calling pickle file for encoding
        with open('encoder_pickle', 'rb') as f:
            en=pickle.load(f)
        #encoding using the pickle module
        encoded_data = en.transform(df1)
        encoded_data=  np.concatenate((encoded_data.toarray(), df2), axis=1)
        predictions = mp.predict(encoded_data)
        # Make predictions using the loaded model
        if st.button('Predict'):
            
            if predictions == 0:
                st.write('First Stage landing might not be succesfull')
                st.image('/Volumes/Sk_drive_space/Python_practise/SpaceX/Images/crash.gif')
            else:
                st.write('First Stage landing will be succesfull')
                st.image('/Volumes/Sk_drive_space/Python_practise/SpaceX/Images/landing_1.gif')
if selected == 'Contact':
    st.markdown("<h1 class='title'>Contact Information</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 20px; background-color:  #333333; border-radius: 10px;">
            <p style="color: #00FFFF;">
                If you have any questions or inquiries, feel free to reach out to me:
                <br>
                <strong>Name:</strong> Sai Kumar Konidena
                <br>
                <strong>Email:</strong> saikumar.konidena@gmail.com
                <br>
                <strong>Github:</strong> <a href="https://github.com/Konidenasaikumar" style="color: #00FFFF;">Konidenasaikumar</a>
                <br>
                <strong>Address:</strong> Freiburg im Breisgau, Germany.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )