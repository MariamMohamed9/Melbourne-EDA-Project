import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Executive Overview - Melbourne Housing",
    page_icon="📊",
    layout="wide"
)
st.markdown("""
<style>
[data-testid="stMetricValue"] {
    font-size: 25px;
}
</style>
""", unsafe_allow_html=True)

html ="""
    <div style="text-align: center; color: white; font-size: 30px; font-weight: bold;">
        Melbourne House Prices EDA Project
    </div>
    """
st.markdown(
    "<h1 style='text-align: center;'>Melbourne House Prices EDA Project</h1>",
    unsafe_allow_html=True,)


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(
        "https://images.adsttc.com/media/images/6854/8198/8a40/7a01/8689/6242/newsletter/melbourne-architecture-city-guide-the-architectural-landmarks-that-make-one-of-the-worlds-most-liveable-cities_22.jpg?1750368681",
        width=600, 
        caption=None)

# Load Data

cleaned_df = pd.read_parquet("MELBOURNE_HOUSE_PRICES_LESS.csv/cleaned_data.parquet")


#numbers of sellers 
Total_sellers = cleaned_df['SellerG'].nunique()

#Total number of properties
suburb_per_region = (
    cleaned_df.groupby(["Regionname", "Suburb"])["Propertycount"]
    .first()
    .reset_index())

region_total_properties = ( suburb_per_region.groupby("Regionname")["Propertycount"].sum().astype(int))

grand_total_properties = region_total_properties.sum()

#Average price of properties in Melbourne
successful_sales = cleaned_df[cleaned_df["Method"].isin(["S", "SP", "SA"])]
overall_avg_price = round(successful_sales["Price"].mean(),2)

#Total Revenue from sold properties
sold_properties = cleaned_df[~cleaned_df['Method'].isin(['PI', 'W','VB'])]
total_revenue = sold_properties["Price"].sum().astype(int)


col1, col2, col3,col4 = st.columns(4)

with col1:
    st.metric(label="Total Sellers Agents", value=Total_sellers)

with col2:
    st.metric(label="Total Properties in Melbourne", value=grand_total_properties)

st.subheader("📌 Properties Breakdown by Region")

regions = region_total_properties.index

# region breakdown
mid_point = len(regions) // 2
first_row_regions = regions[:mid_point]
second_row_regions = regions[mid_point:]

# col1
cols1 = st.columns(len(first_row_regions))
for i, region in enumerate(first_row_regions):
  with cols1[i]:
    with st.container(border=True):
      prop_count = region_total_properties[region]
      st.metric(label=region, value=f"{prop_count:,}")

#col2
cols2 = st.columns(len(second_row_regions))
for i, region in enumerate(second_row_regions):
  with cols2[i]:
    with st.container(border=True):
      prop_count = region_total_properties[region]
      st.metric(label=region, value=f"{prop_count:,}")



with col3:
 st.metric(label="Average Price of Properties in Melbourne", value=f"AU${overall_avg_price:,}")

with col4:
 st.metric(label="Total Revenue ", value=f"AU${total_revenue:,}")

# --- Average Property Prices by Region (Cards Layout) ---
st.markdown("### 💰 Average Property Prices by Region")

# avg prices by region
successful_sales = cleaned_df[cleaned_df["Method"].isin(["S", "SP", "SA"])]
avg_by_region = (
    successful_sales.groupby('Regionname')['Price']
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

# cards
cols = st.columns(4)

for index, row in avg_by_region.iterrows():
    col = cols[index % 4]
    region_name = row['Regionname']
    avg_price = row['Price']
    
    with col:
        with st.container(border=True):
            st.metric(
                label=f"📍 {region_name}",
                value=f"${avg_price:,.0f}"


            )

# Avg prices by region

avg_by_region = (successful_sales.groupby('Regionname')['Price']
                   .mean()
                   .sort_values(ascending=False)
                   .reset_index())

fig_reg = px.bar(
    avg_by_region, 
    x='Price', 
    y='Regionname', 
    color='Price',
    text_auto='.2s',
    title='Average Property Prices by Region',
    labels={'Regionname': 'Region Name', 'Price': 'Average Price (AUD)'},
    color_continuous_scale='Blues'
)
fig_reg.update_layout(yaxis={'categoryorder': 'total ascending'}, template='plotly_white')
st.plotly_chart(fig_reg, use_container_width=True)


# Top 10
st.markdown("### 🏆 Most Expensive VS Most Affordable Suburbs")

col_sub1, col_sub2 = st.columns(2)

with col_sub1:
    # top 10 expensive
    top_expensive = successful_sales.groupby('Suburb')['Price'].mean().nlargest(10).reset_index()
    fig_exp = px.bar(
        top_expensive, 
        x='Price', 
        y='Suburb', 
        color='Price',
        text_auto='.2s',
        title='Top 10 Most Expensive Suburbs',
        labels={'Suburb': 'Suburb', 'Price': 'Avg Price (AUD)'},
        color_continuous_scale='Blues'
    )
    fig_exp.update_layout(yaxis={'categoryorder': 'total ascending'}, template='plotly_white')
    st.plotly_chart(fig_exp, use_container_width=True)

with col_sub2:
    # Top 10 cheap
    top_affordable = successful_sales.groupby('Suburb')['Price'].mean().nsmallest(10).reset_index()
    fig_aff = px.bar(
        top_affordable, 
        x='Price', 
        y='Suburb', 
        color='Price',
        text_auto='.2s',
        title='Top 10 Most Affordable Suburbs',
        labels={'Suburb': 'Suburb', 'Price': 'Avg Price (AUD)'},
        color_continuous_scale='Blues_r'
    )
    fig_aff.update_layout(yaxis={'categoryorder': 'total descending'}, template='plotly_white')
    st.plotly_chart(fig_aff, use_container_width=True)

 #Total daily revenue from sold properties
Daily_revenue = (successful_sales.groupby('Date')['Price'] .sum().reset_index())
st.plotly_chart(px.line(data_frame=Daily_revenue,x='Date',y='Price',markers=True,
                        title='Daily Total Revenue over time',
                        labels={'Date':'Date','Price':'Total Revenue'}).update_layout(xaxis_title='Date',yaxis_title='Total Revenue (AUD)'))

#Total monthly revenue from sold properties
successful_sales['YearMonth'] = successful_sales['Date'].dt.strftime('%Y-%m')
monthly_revenue = successful_sales.groupby('YearMonth')['Price'].sum().reset_index()
st.plotly_chart(px.line(data_frame=monthly_revenue,
        x='YearMonth',
        y='Price',  
        labels={'YearMonth':'Month-Year', 'Price': 'Total Revenue'},
        markers=True,
        title='Monthly Total Revenue'
       ).update_layout(xaxis_title='Date', yaxis_title='Total Revenue (AUD)'))

#Total yearly revenue from sold properties
successful_sales['Year'] = successful_sales['Date'].dt.year.astype(str)
Annual_revenue = (successful_sales.groupby('Year')['Price'].sum().reset_index())

st.plotly_chart(px.line(data_frame=Annual_revenue,
        x='Year',
        y='Price',  
        labels={'Year': 'Year', 'Price': 'Total Revenue'},
        markers=True,
        title='Annual Total Revenue'
       ).update_layout(xaxis_title='Date', yaxis_title='Total Revenue (AUD)'))


# properties types & best sellers
col1, col2 = st.columns(2)

with col1:
    # properties types
    sold_properties = cleaned_df[~cleaned_df['Method'].isin(['PI', 'W', 'VB'])]
    type_counts = sold_properties['Type'].value_counts().reset_index()
    type_counts.columns = ['Type', 'Count']
    st.plotly_chart(
        px.pie(
            data_frame=type_counts,
            names='Type',
            values='Count',
            title='Percentage of sold property types',
            color_discrete_sequence=px.colors.sequential.Blues_r
        ),
        use_container_width=True
    )

with col2:
    # best sellers
    top_sellers = sold_properties['SellerG'].value_counts().head(10).reset_index()
    top_sellers.columns = ['Seller', 'Count']
    st.plotly_chart(
        px.bar(
            data_frame=top_sellers,
            x='Count',
            y='Seller',
            color='Count',
            text_auto=True,
            title='Top 10 Real Estate Sellers'
        ),
        use_container_width=True
    )
         