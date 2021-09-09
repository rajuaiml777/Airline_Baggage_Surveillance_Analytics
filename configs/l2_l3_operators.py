import streamlit as st
import pandas as pd
import ast


def op_details(options, operator_id, decisions):
    """
    Operator's Details.

    Args:
        options: L2 or L3 operator
        operator_id: Operator ID
        decisions: Operator's Decision

    Returns:
        Operator's ID, Decision, Decision Time in DataFrame
    """
    col1, col2 = st.columns(2)
    # Baggage ID and its respective Airlines name
    bag_id = col1.text_input('Bag ID (BHSID)', '0312365545_0282SD')
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

    # Operator ID
    operator_id = st.selectbox(f'{options} ID', operator_id)

    # Opertaor decision
    operator_decision = st.selectbox(f'{options} decision', decisions)

    # L3 decision time
    operator_decision_time = st.number_input('Decision Time (secs)', 1, 150, 10)

    # Creating the dataframe from inputs
    inputs = {'LoginID': operator_id,
              'Decision': operator_decision,
              'Decision_Time': operator_decision_time}
    inputs_df = pd.DataFrame(inputs, index=[0])
    """inputs_df["Decision"] = inputs_df["Decision"].map({'Accept': 0,
                                                       'Reject': 1,
                                                       'Time out': 2})"""
    # Combines user input features with dummy dataset
    # This will be useful for the encoding phase
    dummy_data = pd.read_csv(r'Data/dummy_data.csv')
    df = pd.concat([inputs_df, dummy_data], axis=0)

    # Encoding of ordinal features

    encode = ['Decision']
    for col in encode:
        dummy = pd.get_dummies(df[col], prefix=col)
        df = pd.concat([df, dummy], axis=1)
        del df[col]
    df = df[:1]  # Selects only the first row (the user input data)

    return operator_id, df
