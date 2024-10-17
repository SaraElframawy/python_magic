import plotly.express as px

data = {'Country': ['United States', 'Canada', 'Brazil', 'Russia', 'India','Egypt'], 'Values': [100, 50, 80, 90, 70,100]}

fig = px.choropleth(
    data,
    locations='Country',
    locationmode='country names',  # Corrected: use 'country names' in lowercase
    color='Values',
    color_continuous_scale='Reds',
    title='Map Values'
)

fig.show()
