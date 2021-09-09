import streamlit as st
from configs.new_operators import new_op_details
from configs.predictions import model_inputs

# Data configuration
decisions = ['Accept', 'Reject', 'Time out']


# New Operator
def new_operator():
    st.header('# New Operator Details:')
    options, ids, df = new_op_details(decisions)

    # Make predictions
    model_inputs(options, ids, df)


if __name__ == '__main__':
    new_operator()