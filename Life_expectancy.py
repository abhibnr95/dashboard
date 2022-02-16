import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

path = 'C:\life_expectancy.csv'
data = pd.read_csv(path)
data_cols = [x for x in data.columns]
y = data['Life expectancy']
#cat_x = data[['Country', 'Year', 'Status', 'continent', 'Life expectancy']]
cat_x_cols = ['Country', 'Year', 'Status', 'continent']
num_x = data[['Population', 'GDP', 'Schooling']]

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(children = [
    # html.H1('This is H1 title'),
    dcc.Dropdown(id = 'drop', options = [{'label' : x, 'value' : x} for x in data.columns], value = 'continent'),
    dcc.Graph(id = 'graph')
])

@app.callback(
    Output('graph', 'figure'),
    [Input('drop', 'value')]
)

def update_graph(selection_drop) :
    if selection_drop in cat_x_cols :
        fig = px.bar(data_frame =data.groupby([selection_drop]).mean().reset_index(), 
        x = selection_drop,  
        hover_name = selection_drop, 
        y = 'Life expectancy', 
        color = selection_drop,
        height = 400,
        title = f'Life expectancy vs {selection_drop}')
    else :
        fig = px.scatter(data, x = selection_drop, y = 'Life expectancy',
        height=400,
        color= selection_drop, 
        hover_name = selection_drop, 
        #color_continuous_scale=px.colors.sequential.Viridis, # theme : Virdis
        title = f'Life expectancy vs {selection_drop}')
    return fig

if __name__ == "__main__" :
    app.run_server(debug = True)