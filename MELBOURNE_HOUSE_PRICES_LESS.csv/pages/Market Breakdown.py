import pandas as pd
import plotly.express as px
import streamlit as st

# page 
st.set_page_config(
    page_title="Market Breakdown - Melbourne Housing",
    page_icon="🧩",
    layout="wide"
)

# header
st.markdown("<h1 style='text-align: center;'>🧩 Market Breakdown & Attributes</h1>", unsafe_allow_html=True)
st.markdown("""
<style>
   
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #145C6D !important;
        border-bottom-color: #145C6D !important;
    }
    
    
    div.stButton > button:first-child {
        background-color: #FFFFFF !important;
        color: #1E293B !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 8px !important;
        transition: all 0.2s ease-in-out !important;
    }
    
    
    div.stButton > button:first-child:hover,
    div.stButton > button:first-child:focus,
    div.stButton > button:first-child:active {
        border-color: #145C6D !important;
        color: #145C6D !important;
        box-shadow: 0 0 0 2px rgba(20, 92, 109, 0.2) !important;
        outline: none !important;
    }
</style>
""", unsafe_allow_html=True)
# load data
from pathlib import Path
import os

BASE_DIR = Path(os.getcwd())
cleaned_df = pd.read_parquet(BASE_DIR / "cleaned_data.parquet")

# tabs
tab1, tab2 = st.tabs(["🔢 Numerical Analysis", "🏷️ Categorical Analysis"])

# --- TAB 1: Numerical Analysis ---
with tab1:
    st.subheader("📊 Property Attributes")
    
    with st.container(border=True):
        num_cols = cleaned_df.select_dtypes(include='number').columns
        col_select = st.selectbox('Select Column to Analyze:', num_cols, key='num_select')
        
        show_hist = st.button('📈 Show Histogram Chart', key=1)
    
    if show_hist:
        fig_num = px.histogram(
            data_frame=cleaned_df,
            x=col_select,
            title=f'Histogram Distribution of {col_select}',
            color_discrete_sequence=['#1f77b4']  # درجة الأزرق الصافية
        )
        fig_num.update_layout(template='plotly_white')
        st.plotly_chart(fig_num, use_container_width=True)


# --- TAB 2: Categorical Analysis ---
with tab2:
    st.subheader("🏷️ Sales & Area Attributes")
    
    with st.container(border=True):
      
        cat_cols = cleaned_df.select_dtypes(include='object').columns.drop(['Postcode', 'Address'], errors='ignore')
        
        col1, col2 = st.columns(2)
        with col1:
            col_select_cat = st.selectbox('Select Category Column:', cat_cols, key='cat_select')
        with col2:
            chart_select = st.radio('Select Chart Type:', ['Histogram', 'Pie Chart'], horizontal=True)
            
        show_cat_chart = st.button('📊 Show Chart', key=2)
        
    if show_cat_chart:
        if chart_select == 'Histogram':
            fig_cat = px.histogram(
                data_frame=cleaned_df,
                x=col_select_cat,
                text_auto=True,
                title=f'Distribution of {col_select_cat}',
                color_discrete_sequence=['#1f77b4']
            )
            fig_cat.update_xaxes(categoryorder='max descending')
            fig_cat.update_layout(template='plotly_white')
            st.plotly_chart(fig_cat, use_container_width=True)
            
        else:
            fig_pie = px.pie(
                data_frame=cleaned_df,
                names=col_select_cat,
                title=f'Pie Chart of {col_select_cat}',
                color_discrete_sequence=px.colors.sequential.Blues_r  # درجات الأزرق المتناسقة
            )
            fig_pie.update_layout(template='plotly_white')
            st.plotly_chart(fig_pie, use_container_width=True)