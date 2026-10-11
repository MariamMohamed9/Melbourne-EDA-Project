import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Melbourne Housing Dashboard", page_icon="🏠", layout="wide"
)

#title
st.markdown(
    "<h1 style='text-align: center;'>Melbourne House Prices EDA Project</h1>",
    unsafe_allow_html=True,
)

# image in the center of the page
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(
        "https://images.adsttc.com/media/images/6854/8198/8a40/7a01/8689/6242/newsletter/melbourne-architecture-city-guide-the-architectural-landmarks-that-make-one-of-the-worlds-most-liveable-cities_22.jpg?1750368681",
        width=600,  
        caption=None,  
    )

st.write("---")  

# load Data
df = pd.read_parquet("cleaned_data.parquet")

#Show sample of data
st.subheader("📋 Data Overview")
st.dataframe(df.head(10), use_container_width=True)

# columns descriptions
column_descriptions = {
    "Suburb": "Name of the suburb where the property is located",
    "Address": "Detailed address of the property",
    "Rooms": "Number of rooms in the property",
    "Type": "Property type (br: bedroom, h: house, t: townhouse, u: unit)",
    "Price": "Price of the property in AUD",
    "Method": "Method of sale (S: property sold, SP: property sold prior...)",
    "SellerG": "Real Estate Agent selling the property",
    "Date": "Date of sale",
    "Distance": "Distance from Central Business District (CBD) in kilometers",
    "Postcode": "Postal code of the area",
    "Bedroom2": "Scraped # of Bedrooms from different source",
    "Bathroom": "Number of Bathrooms",
    "Car": "Number of car spots",
    "Landsize": "Land Size in square meters",
    "BuildingArea": "Building Size in square meters",
    "YearBuilt": "Year the house was built",
    "CouncilArea": "Governing council for the area",
    "Regionname": "General Region (West, North West, North, etc.)",
    "Propertycount": "Number of properties that exist in the suburb",
}

# Create description table
description_df = pd.DataFrame(
    [
        {
            "Column": column,
            "Description": column_descriptions.get(
                column, "Description not available"
            ),
        }
        for column in df.columns
        if not column.endswith("_id")
    ]
)

# Display title
st.subheader("📋 Dataset Column Descriptions")
# Display table
st.table(description_df)