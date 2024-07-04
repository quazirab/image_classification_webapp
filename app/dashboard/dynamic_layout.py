import dash_html_components as html
import plotly.graph_objs as go

from app.dashboard.image_processing import DisplayImagePIL, barChart


def plot_graph(image, prediction):
    return [
        html.Div(
            [
                html.Div(
                    [DisplayImagePIL(image)],
                    id="image_container",
                    className="pretty_container",
                ),
            ],
            className="six columns",
        ),
        html.Div(
            [
                html.Div(
                    [barChart(prediction)],
                    id="image_container",
                    className="pretty_container",
                ),
            ],
            className="six columns",
        ),
    ]


def error_message(error):
    return [
        html.Div(
            [
                html.Div([html.H6(error)], id="error_container", className="pretty_container"),
            ],
            className="twelve columns",
        ),
    ]
