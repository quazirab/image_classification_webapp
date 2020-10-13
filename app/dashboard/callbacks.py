from dash.dependencies import Input, Output, State
from plotly.graph_objs._figure import Figure
import dash_table

import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

from app.dashboard.image_processing import b64_to_pil, img_to_list, prediction, DisplayImagePIL, barChart

approved_file_extenstions = ['.jpg', 'jpeg', '.png']


def load_callbacks(app):

    @app.callback(Output('aggregate_data', 'data'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename')])
    def update_output(content, filename):
        if filename:
            if any(approved_file_extenstion in filename for approved_file_extenstion in approved_file_extenstions):
                string = content.split(';base64,')[-1]

                img = b64_to_pil(string)
                img_list = img_to_list(img)
                predictions = prediction(img_list)

                data = {}
                data.update(predictions)
                data['image'] = string

                return data

    @app.callback(Output('row2', 'children'),
                  [Input('aggregate_data', 'data')])
    def update_table(data):
        if data:
            image = data['image']
            prediction = data['prediction']

            return [
                    html.Div([
                        html.Div(
                            [
                                DisplayImagePIL(image)
                            ],
                            id="image_container",
                            className="pretty_container"
                        ),

                        ],
                        className="six columns"
                        ),
                html.Div([
                        html.Div(
                            [
                                barChart(prediction)
                            ],
                            id="image_container",
                            className="pretty_container"
                        ),

                        ],
                        className="six columns"
                        ),
                ]
