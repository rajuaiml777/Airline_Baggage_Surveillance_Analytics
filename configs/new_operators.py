import streamlit as st
import pandas as pd
import ast


def new_op_details(decisions):
    """
    New Operator's Details.

    Args:
        decisions: Operator's Decision

    Returns:
        New operator's ID, Decision, Decision Time in DataFrame
    """
    col1, col2 = st.columns(2)
    # Baggage ID and its respective Airlines name
    bag_id = col1.text_input('Bag ID (BHSID)', '0879553646_0309SF')
    if len(bag_id) < 4:
        st.error("Entered wrong Bag ID. Please try agian")
    else:
        pass

    # loading the file containing the airline codes and airline names
    file = open('configs/airlines.txt', 'r')
    # read the data
    contents = file.read()
    # loading the as dictionary
    airline_codes = ast.literal_eval(contents)
    # close the opened file
    file.close()

    # extracting the code from BHSID
    bag_code = ''.join(bag_id.split('_')[0][1:4])
    if str(bag_code) in airline_codes.keys():
        airline_name = airline_codes[bag_code]
    else:
        airline_name = 'Other'

    # Airline name
    airlines = col2.text_input('Airlines', airline_name)

    # select L2 operator or L3 operator
    new_op = st.sidebar.radio('Please select:', ['L2 Operator', 'L3 Operator'])
    if new_op == 'L2 Operator':
        st.subheader('Enter the details of the L2 operator')
    else:
        st.subheader('Enter the details of the L3 operator')

    # Operator ID
    new_id = st.text_input("New Operator's ID", 100)

    # Operator Decision
    new_decision = st.selectbox('Operator decision', decisions)

    # Decision Time
    new_decision_time = st.number_input('Operator decision Time (secs)', 1, 150, 25)

    # Creating the dataframe from inputs
    inputs_new = {'LoginID': new_id,
                  'Decision': new_decision,
                  'Decision_Time': new_decision_time}
    new_data = pd.DataFrame(inputs_new, index=[0])
    """new_data["Decision"] = new_data["Decision"].map({'Accept': 0,
                                                     'Reject': 1,
                                                     'Time out': 2})"""
    # Combines user input features with entire dataset
    # This will be useful for the encoding phase
    dummy_data = pd.read_csv(r'Data/dummy_data.csv')
    df = pd.concat([new_data, dummy_data], axis=0)

    # Encoding of ordinal features
    encode = ['Decision']
    for col in encode:
        dummy = pd.get_dummies(df[col], prefix=col)
        df = pd.concat([df, dummy], axis=1)
        del df[col]
    df = df[:1]  # Selects only the first row (the user input data)

    return new_op, new_id, df
