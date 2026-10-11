import pandas as pd
import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="Regional Market Explorer",
    page_icon="🔍",
    layout="wide"
)

# sidebar
st.markdown("""
<style>
    
    .stMultiSelect [data-baseweb="tag"] {
        background-color: #145C6D !important;
    }
</style>
""", unsafe_allow_html=True)

# header
st.markdown("<h1 style='text-align: center;'>🔍 Regional Market Explorer</h1>", unsafe_allow_html=True)

st.markdown("""
<style>
    
    .stMultiSelect [data-baseweb="tag"] {
        background-color: #E0F2FE !important;  /* خلفية لبني فاتح */
        border: 1px solid #38BDF8 !important;  /* إطار أزرق فاتح */
    }
    
   
    .stMultiSelect [data-baseweb="tag"] span,
    .stMultiSelect [data-baseweb="tag"] svg {
        color: #0369A1 !important;
        fill: #0369A1 !important;
    }
</style>
""", unsafe_allow_html=True)

# load data
cleaned_df = pd.read_parquet("cleaned_data.parquet")

# Sidebar
st.sidebar.header("📍 Filter Options")

# Regions
regions_list = ['All Regions'] + cleaned_df['Regionname'].dropna().unique().tolist()
region = st.sidebar.multiselect('Select Region:', regions_list, default=['All Regions'])

if 'All Regions' not in region and region:
    cleaned_df = cleaned_df[cleaned_df['Regionname'].isin(region)]

# Date Range
cleaned_df['Date'] = pd.to_datetime(cleaned_df['Date'])
min_date = cleaned_df['Date'].min().date()
max_date = cleaned_df['Date'].max().date()

st.sidebar.markdown("---")
st.sidebar.subheader("📅 Date Range")

start_date = st.sidebar.date_input('From:', value=min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input('To:', value=max_date, min_value=min_date, max_value=max_date)


cleaned_df = cleaned_df[
    (cleaned_df['Date'].dt.date >= start_date) & 
    (cleaned_df['Date'].dt.date <= end_date)
]


st.markdown("---")

# 
st.subheader("📋 Explorer Data Table")
st.dataframe(cleaned_df, use_container_width=True, hide_index=True)