import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from configs.plots import bar_plot

st.set_option('deprecation.showPyplotGlobalUse', False)

# Operators Data
l2_operators_data = pd.read_csv('Data/L2_operators.csv')
l2_operators_decision = pd.read_csv('Data/L2_operators_Decision.csv').iloc[:, 1:]
l3_operators_data = pd.read_csv('Data/L3_operators.csv')
l3_operators_decision = pd.read_csv('Data/L3_operators_Decision.csv')


def overall_perf():
    # SideBar heading
    st.header('# Overall Performance of the Operator')

    # Operator selection
    st.sidebar.header('Select the operator')
    options = st.sidebar.radio('Operator Selection:', ['L2 Operator',
                                                       'L3 Operator'])

    # L2 Operator
    if options == 'L2 Operator':
        # Total operators present
        st.sidebar.write('Total number of operators present in L2:',
                 l2_operators_data['L2_LoginID'].nunique())
        # Selection of the L2 operator ID
        l2_operators = st.sidebar.selectbox('Select the ID:',
                                            l2_operators_data['L2_LoginID'].unique())
        # Extracting data
        l2_perf_data = l2_operators_data[l2_operators_data['L2_LoginID'] == l2_operators]
        l2_dec_data = l2_operators_decision[l2_operators_decision['L2_LoginID'] == l2_operators]
        # Plotting the data
        bar_plot(l2_perf_data['L2_Operator_Performance'],
                 l2_perf_data['L2_Operator_Performance_Count'])
        plt.title(f'Operator {l2_operators}')
        st.pyplot()
        # Plotting the data
        bar_plot(l2_dec_data['L2_Decision'],
                 l2_dec_data['L2_Decision_Count'])
        plt.title(f'Operator {l2_operators}')
        st.pyplot()

    # L3 Operator
    elif options == 'L3 Operator':
        # Total operators present
        st.sidebar.write('Total number of operators present in L3:',
                 l3_operators_data['L3_LoginID'].nunique())
        # Selection of the L2 operator ID
        l3_operators = st.sidebar.selectbox('Select the ID:',
                                            l3_operators_data['L3_LoginID'].unique())
        # Extracting data
        l3_perf_data = l3_operators_data[l3_operators_data['L3_LoginID'] == l3_operators]
        l3_dec_data = l3_operators_decision[l3_operators_decision['L3_LoginID'] == l3_operators]
        # Plotting the data
        bar_plot(l3_perf_data['L3_Operator_Performance'],
                 l3_perf_data['L3_Operator_Performance_Count'])
        plt.title(f'Operator {l3_operators}')
        st.pyplot()
        # Plotting the data
        bar_plot(l3_dec_data['L3_Decision'],
                 l3_dec_data['L3_Decision_Count'])
        plt.title(f'Operator {l3_operators}')
        st.pyplot()
