import streamlit as st


def about_app():
    # Heading
    st.header('# About: ')
    st.write('''
                The Operator Performance Prediction WebApp helps to find the performace 
                of the operators at the airport baggage section.\n
             ''')
    st.subheader('WebApp has 3 sections:')
    # Page 2
    st.subheader('1. Existing Operator Performace: ')
    st.write('Here we can check how the operator performace is based on time taken '
             'by him to make a decision and also get information about the luggage.')
    # Page 3
    st.subheader('2. New Operator Performace: ')
    st.write('In this, if new operator joins we can check his performance here and '
             'assign him new operator ID.')
    # Page 4
    st.subheader('3. Overall Performance: ')
    st.write('Here we get know the overall performance of the operator.')




    '''This WebApp has 3 sections\n
                \n
                \n
                3. Overall Performance\n'''

