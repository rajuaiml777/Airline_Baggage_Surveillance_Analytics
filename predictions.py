import streamlit as st
import pickle

# Load the saved models
l2_model = pickle.load(open('Model/L2_Prediction_model.sav', 'rb'))
l3_model = pickle.load(open('Model/L3_Prediction_model.sav', 'rb'))


def model_inputs(options, ids, df_inputs):
    # Apply model on the given inputs
    st.subheader('# Prediction')
    st.write(f'Hit "Predict" button to check performance of operator {ids}')
    predict_new = st.button('Predict', key='new_performance')
    if predict_new:
        # predictions
        if options == 'L2 Operator':
            prediction = l2_model.predict(df_inputs)
        else:
            prediction = l3_model.predict(df_inputs)

        # output results
        if prediction == 0:
            st.success(f'Performance of operator is Excellent.')
        elif prediction == 1:
            st.success(f'Performance of operator is Good.')
        elif prediction == 2:
            st.success(f'Performance of operator is Normal.')
        else:
            st.error(f'Performance of operator is Bad.')