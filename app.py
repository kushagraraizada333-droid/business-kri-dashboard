import streamlit as st
import pandas as pd, numpy as np
import plotly.express as px
st.set_page_config(layout="wide",page_title="Business KRI Monitoring Dashboard")
st.title("📊 Business KRI Monitoring Dashboard")
months=pd.date_range("2024-01-01",periods=24,freq="MS")
df=pd.DataFrame({
"Month":months,
"Credit Risk":np.random.randint(40,90,24),
"Cyber Incidents":np.random.randint(5,30,24),
"Attrition %":np.random.uniform(5,20,24),
"Customer Churn %":np.random.uniform(2,12,24)})
c1,c2,c3,c4=st.columns(4)
c1.metric("Credit Risk",int(df['Credit Risk'].iloc[-1]))
c2.metric("Cyber Incidents",int(df['Cyber Incidents'].iloc[-1]))
c3.metric("Attrition %",f"{df['Attrition %'].iloc[-1]:.1f}%")
c4.metric("Churn %",f"{df['Customer Churn %'].iloc[-1]:.1f}%")
st.plotly_chart(px.line(df,x="Month",y=["Credit Risk","Cyber Incidents"]),use_container_width=True)
st.plotly_chart(px.bar(df,x="Month",y="Credit Risk"),use_container_width=True)
st.plotly_chart(px.scatter(df,x="Attrition %",y="Customer Churn %",size="Cyber Incidents"),use_container_width=True)
st.success("AI Insight: Cyber incidents are increasing. Monitor operational controls.")
