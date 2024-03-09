import plotly.graph_objects as go

def generate_visualization(data):
    # Example visualization using Plotly (replace this with your actual visualization code)
    x = list(data.keys())
    y = list(data.values())

    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))
    fig.update_layout(title='Example Visualization', xaxis_title='X Axis', yaxis_title='Y Axis')
    fig.show()