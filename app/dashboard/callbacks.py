from dash.dependencies import Input, Output, State
from plotly.graph_objs._figure import Figure
import dash_table

import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

from app.dashboard.image_processing import b64_to_pil, img_to_list, prediction, DisplayImagePIL, barChart, model_wakeup

approved_file_extenstions = ['.jpg', 'jpeg', '.png']


def load_callbacks(app):

    @app.callback(Output('aggregate_data', 'data'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename')])
    def update_output(content, filename):
        
        model_wakeup()

        data = {}
        if filename:
            app.logger.debug(f'{filename}')
            if any(approved_file_extenstion in filename.lower() for approved_file_extenstion in approved_file_extenstions):
                app.logger.debug(f'{filename} processing')
                
                try:
                    string = content.split(';base64,')[-1]

                    img = b64_to_pil(string)
                    img_list = img_to_list(img)
                    app.logger.debug(f'{filename} requesting prediction')
                    predictions = prediction(img_list)
                    app.logger.debug(f'{filename} prediction recieved - {prediction}')
                    
                    data.update(predictions)
                    data['image'] = string
                    app.logger.debug(f'{filename} processing finished.')
                    return data
                except:
                    data['error'] = f"File Processing Error, Please try with different Image"
                    return data
            else:
                data['error'] = f"{filename} file not supported. Only PNG and JPG file supported"
                return data

    @app.callback(Output('row2', 'children'),
                  [Input('aggregate_data', 'data')])
    def update_table(data):
        if data:
            app.logger.debug(f'plotting data')
            if not 'error' in data:
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
            else:
                return [
                        html.Div([
                            html.Div(
                                [
                                    html.H6(data['error'])
                                ],
                                id="error_container",
                                className="pretty_container"
                            ),

                            ],
                            className="twelve columns"
                            ),
                    ]
