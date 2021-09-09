import streamlit as st
import pandas as pd


def new_op_details(decisions):
    """
    New Operator's Details.

    Args:
        decisions: Operator's Decision

    Returns:
        New operator's ID, Decision, Decision Time in DataFrame
    """

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
    new_data["Decision"] = new_data["Decision"].map({'Accept': 0,
                                                     'Reject': 1,
                                                     'Time out': 2})

    return new_op, new_id, new_data
