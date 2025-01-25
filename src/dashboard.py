import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def load_data():
    return pd.read_csv('data/call_data.csv')

def create_dashboard():
    st.set_page_config(layout="wide")
    st.title("Call Center Analytics Dashboard")

    df = load_data()
    df['week'] = pd.to_datetime(df['week'])

    # KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Average Resolution Rate", f"{(df['resolved_calls'].sum() / df['total_calls'].sum() * 100):.1f}%")
    with col2:
        st.metric("Avg Resolution Time", f"{df['average_resolution_time'].mean():.1f} min")
    with col3:
        st.metric("Avg Customer Satisfaction", f"{df['customer_satisfaction'].mean():.1f}/5.0")
    with col4:
        st.metric("Escalation Rate", f"{(df['escalated_calls'].sum() / df['total_calls'].sum() * 100):.1f}%")

    # Weekly Resolution Rate
    st.subheader("Weekly Call Resolution Rate")
    resolution_rate = df.assign(
        resolution_rate=df['resolved_calls'] / df['total_calls'] * 100
    )
    fig1 = px.line(resolution_rate, x='week', y='resolution_rate',
                   title="Weekly Resolution Rate (%)")
    st.plotly_chart(fig1, use_container_width=True)

    # Customer Satisfaction Trend
    st.subheader("Customer Satisfaction Trend")
    fig2 = px.line(df, x='week', y='customer_satisfaction',
                   title="Weekly Customer Satisfaction Score")
    st.plotly_chart(fig2, use_container_width=True)

    # Call Volume Analysis
    st.subheader("Call Volume Analysis")
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=df['week'], y=df['total_calls'], name='Total Calls'))
    fig3.add_trace(go.Scatter(x=df['week'], y=df['resolved_calls'], name='Resolved Calls'))
    fig3.update_layout(title="Weekly Call Volumes")
    st.plotly_chart(fig3, use_container_width=True)

if __name__ == "__main__":
    create_dashboard()