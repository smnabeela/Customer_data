import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Wholesale Customer Data')
data = pd.read_csv('mentornow/Wholesale_customers_data.csv')


a=data['Region'].unique()
display=['Chennai','Ahmedabad','Banglore']
s1= st.sidebar.selectbox('Select Region',(a),format_func = lambda x:display[x-2])


b=data['Channel'].unique()
display=['Hotel','Retail']
s2= st.sidebar.selectbox('Select Channel',(b),format_func = lambda x:display[x-1])

c1,c2,c3 =st.columns(3)

c=data[(data['Region'] ==s1) & (data['Channel']==s2)]

c1.metric(label='Total Fresh',value=round(c['Fresh'].sum(),2)) 
c2.metric(label='Total Milk',value=round(c['Milk'].sum(),2))
c3.metric(label='Total Grocery',value=round(c['Grocery'].sum(),2))

c4,c5,c6 =st.columns(3)
c4.metric(label='Total Frozen',value=round(c['Frozen'].sum(),2)) 
c5.metric(label='Total Detergent_paper',value=round(c['Detergents_Paper'].sum(),2)) 
c6.metric(label='Total Delicassen',value=round(c['Delicassen'].sum(),2)) 

st.write(c)
st.header('Sales Chart')
Total={
    'Fresh':round(c['Fresh'].sum(),2),
    'Milk':round(c['Milk'].sum(),2),
    'Grocery':round(c['Grocery'].sum(),2),
    'Frozen':round(c['Frozen'].sum(),2),
    'Detergent_Paper':round(c['Detergents_Paper'].sum(),2),
    'Delicassen':round(c['Delicassen'].sum(),2)}
st.bar_chart(Total)

fig = px.pie(values=list(Total.values()),
             names=list(Total.keys()),
             title='Distribution by Category')
st.plotly_chart(fig)