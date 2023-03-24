import pandas as pd
import hvplot.pandas
import panel as pn

df = pd.read_csv('vgsales.csv')

total_per_genre = df.groupby(['Genre', 'Year'])['Global_Sales'].sum().reset_index()

def plot_genre(genre):
    plot_data = total_per_genre[total_per_genre['Genre'] == genre]
    return plot_data.hvplot.bar(x='Year', y='Global_Sales', 
                                title=f'Total Sales of Video Games in the {genre} Genre Every Year',
                                xlabel='Year (1980 - 2017)', ylabel='Global Sales',
                                width=800, height=500, color='Genre', line_color=None)

genre_list = total_per_genre['Genre'].unique().tolist()
genre_widget = pn.widgets.Select(options=genre_list)

pn.interact(plot_genre, genre=genre_widget)
