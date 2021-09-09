# Importing Required Packages
import streamlit as st
from configs.operators import operators_list
from configs.l2_l3_operators import op_details
from configs.predictions import model_inputs


# Data configuration
l2_op, l3_op = operators_list()
decisions = ['Accept', 'Reject', 'Time out']


def main():
    # Selection of L2 or L3 Operator
    options = st.sidebar.radio('Operator Selection:', ['L2 Operator',
                                                       'L3 Operator'])

    # L2 operator Details
    if options == 'L2 Operator':
        st.header('# L2 operator Details')
        ids, df = op_details(options, l2_op, decisions)

    # L3 operator Details
    elif options == 'L3 Operator':
        st.header('# L3 operator Details')
        ids, df = op_details(options, l3_op, decisions)

    # Make predictions
    model_inputs(options, ids, df)


if __name__ == '__main__':
    main()
