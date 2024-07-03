# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
import streamlit as st # Now you can import streamlit
warnings.filterwarnings('ignore')

df = pd.read_excel('Canada.xlsx', sheet_name='Canada by Citizenship (2)')

df1=df.set_index('OdName')

d1=df1.iloc[:,8:]
d1= pd.DataFrame(d1)
column_sums = d1.sum()
column_sums = pd.DataFrame(column_sums)
column_sums=column_sums.reset_index()
column_sums.columns = ['year','count'] 
# Assign the single name 'count' to the column
total=column_sums['count'].sum()
#pd.set_option('display.max_columns',None)
st.sidebar.header(" Immegration to Canada ")
st.sidebar.image("download.jpeg")
st.sidebar.write("This dataset provides detailed insights into Immegration to canada")
 
st.sidebar.markdown("Made with  :heart_eyes: by Eng. [Mariam Naeim ](https://www.linkedin.com/in/mariam-naeim-a8a02821a)")
# Create the Plotly figure
st.write("")
st.sidebar.write("filter your data")
#cat_filter=st.sidebar.selectbox("Countries",[df['OdName'].unique])









def format_large_number(number):
    suffixes = ["", "K", "M", "B", "T"]  # Suffixes for thousands, millions, billions, etc.
    for suffix in suffixes:
        if abs(number) < 1000:
            return f"{number:.1f}{suffix}"
        number /= 1000
    return f"{number:.1f}T"  # If the number is very large
Immegrations=format_large_number(total)
Countries=format_large_number(d1.index.value_counts().sum().round(0))
a1,a2,a3=st.columns(3)
a1.metric("Total immigrants",Immegrations)
a2.metric("Countries",Countries)
a3.subheader("Between 1980 to 2013")












c1,c2=st.columns(2)

fig = go.Figure(data=go.Scatter(x=column_sums['year'], y=column_sums['count'])) # Now df has 'x' and 'y' columns
fig.update_layout(
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)
# Display the plot in Streamlit
#st.title("Line Plot Example")
c1.plotly_chart(fig, use_container_width=True)


# Create the Plotly figure
column_sums['year']=column_sums['year'].astype(str)
column_sums_sorted = column_sums.sort_values(by='count',ascending=False)
# Create the Plotly figure (Bar Chart)
fig1 = go.Figure(data=go.Bar(x=column_sums_sorted['year'], y=column_sums_sorted['count']))
fig1.update_layout(
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    ),
  xaxis_tickangle=-45
)
c2.plotly_chart(fig1, use_container_width=True)


dt=d1.T

row_sums = d1.sum(axis=1)
row_sums = pd.DataFrame(row_sums)
row_sums=row_sums.reset_index()
row_sums.columns = ['OdName','count']

# Create the Plotly figure (Bar Chart)
st.subheader("immigrants from each country")

import plotly.express as px

fig7 = px.choropleth(
    row_sums,
    locations='OdName',
    locationmode='country names',
    color='count',
    hover_name='OdName',
    title='World immegration Density',
    color_continuous_scale='Viridis',
)
 # Removed animation_frame as 'year' column doesn't exist
st.plotly_chart(fig7)


fig2 = go.Figure(data=go.Bar(x=row_sums['OdName'], y=row_sums['count']))

st.plotly_chart(fig2)
st.write("")
fig3= px.line(dt, x=dt.index, y=dt.columns[0:]) 
fig3.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
st.plotly_chart(fig3)


# Count occurrences of each category
a1,a2=st.columns(2)
category_counts1 = df['AreaName'].value_counts()

# Create the bar chart using Plotly Express
fig4 = px.bar(x=category_counts1.values, y=category_counts1.index
             )

fig4.update_layout(title="immigration from continents")
a1.plotly_chart(fig4)
# Count occurrences of each category
category_counts2 = df['DevName'].value_counts()

# Create the bar chart using Plotly Express
fig5= px.bar(x=category_counts2.values, y=category_counts2.index
          )

fig5.update_layout(title="the status of the countries")
a2.plotly_chart(fig5)
import dash