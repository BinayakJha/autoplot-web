import os
import time
import sys
import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .stConnectionStatus{visibility: hidden;}
            </style>
            
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# Title
st.title('Autoplot Maker And Predictor')
filepath = st.text_input('Please enter the file path here (note: do not give a path or anything else we will find the file itself :) = ')

# Asking start
X = st.text_input('[?] please enter the data table heading which you want to show in x axis = ')
y = st.text_input('[?] please enter the data table heading which you want to show in y axis = ')
x_label = st.text_input('[?] please enter the x axis label = ')
y_label = st.text_input('[?] please enter the y axis label = ')
heading = st.text_input('[?] please enter the heading of the graph = ')

st.write('Please enter the type of graph you want to show')
type_graph = st.radio('', ['1. Line Plot ', '2. Scatter Plot', '3. Histogram', '4. Box Plot', '5. Bar Plot', '6. Pie Chart'])
# save graph
st.write('')
st.write('')
save_graph = st.checkbox('Save Graph')

if save_graph:
    save_graph_name = st.text_input('Please enter the name of the graph you want to save = ')


st.write('')
st.write('')

# plot graph function start

if st.button('Search file and Plot Graph'):
    df = pd.read_csv(filepath)
    st.write('Plotting...')
    fig= plt.figure()
    
    if type_graph == '1. Line Plot ':
        plt.plot(df[X], df[y])
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(heading)
        st.pyplot(fig)
    elif type_graph == '2. Scatter Plot':
        plt.scatter(df[X], df[y])
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(heading)
        st.pyplot(fig)
    elif type_graph == '3. Histogram':
        plt.hist(df[y])
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(heading)
        st.pyplot(fig)
    elif type_graph == '4. Box Plot':
        plt.boxplot(df[y])
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(heading)
        st.pyplot(fig)
    elif type_graph == '5. Bar Plot':
        plt.bar(df[X], df[y])
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(heading)
        st.pyplot(fig)
    elif type_graph == '6. Pie Chart':
        plt.pie(df[y], labels=df[X])
        plt.title(heading)
        st.pyplot(fig)
    
    if save_graph:
        if os.path.exists(save_graph_name):
            st.write('File already exists')
        plt.savefig(save_graph_name)

  
# # math statistics function start
st.write('')
st.write('')
st.write('')
save_math = st.checkbox('Maths( Statistics )')
if save_math:
    df = pd.read_csv(filepath)
    st.write('Please select a number from list:')
    st.write('1. Standard Deviation')
    st.write('2. Mean')
    st.write('3. Variance')
    st.write('4. Median')
    st.write('5. Mode')
    st.write('6. Range')
    st.write('7. Quartile')
    st.write('8. Quartile 3')
    st.write('9. All')
    me = st.selectbox('Select a number from list:', ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    if st.button('Show The Answers'):
        if me == '1':
            std = df[y].std()
            st.write('Standard Deviation = ', str(std))
        elif me == '2':
            mean = df[y].mean()
            st.write('Mean = ', str(mean))
        elif me == '3':
            var = df[y].var()
            st.write('Variance = ', str(var))
        elif me == '4':
            median = df[y].median()
            st.write('Median = ', str(median))
        elif me == '5':
            mode = df[y].mode()
            st.write('Mode = ', str(mode))
        elif me == '6':
            range = df[y].max() - df[y].min()
            st.write('Range = ', str(range))
        elif me == '7':
            q1 = df[y].quantile(0.25)
            st.write('Q1 = ', str(q1))
        elif me == '8':
            q3 = df[y].quantile(0.75)
            st.write('Q3 = ', str(q3))
        elif me == '9':
                st.write('''
                Standard deviation of the data is {} \n
                Mean of the data is {} \n
                Variance of the data is {} \n
                Median of the data is {} \n
                Range of the data is {} \n
                Quartile1 of the data is {} \n
                Quartile3 of the data is {} \n
                '''.format(df[y].std(),df[y].mean(),df[y].var(),df[y].median(),df[y].max() - df[y].min(),df[y].quantile(0.25),df[y].quantile(0.75)))
                st.write('Mode of the data is  ', df[y].mode())

# prediction

st.write('')
st.write('')
st.write('')
prediction = st.checkbox('Prediction')
if prediction:
    df = pd.read_csv(filepath)
    st.write('Still In development ..')
    st.write('1. Linear Regression')
    if st.button('Predict'):
        lr = LinearRegression()
        lr.fit(df[[X]], df[[y]])
        st.write('Prediction = ', lr.predict(df[[X]]))
    