import dash_html_components as html
import dash_core_components as dcc


def load_layout(app):
    app.layout = html.Div([
        html.Div(  # header
            [
                html.Div(
                    [
                        html.H2('Image Classification'),
                        # html.A(html.H4('API Example'), href='/api/v1/history?ticker=MMM', target="_blank"),
                    ],

                    className='eight columns'
                ),

                html.Div(

                    className='two columns'
                ),


                html.A([
                  
                        html.Img(
                        src="https://github.githubassets.com/images/modules/logos_page/Octocat.png",
                        style={'height': '100%',
                               'width': '50%', 'float': 'right'},
                        title='Github Repo',
                        )
                
                    
                ],
                    href="https://github.com/quazirab/image_classification_webapp",
                    className='two columns',
                    target="_blank",
                ),

            ],
            id="header",
            className='row',
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                        [
                                dcc.Loading(
                                    id="loading-1",
                                    type="default",
                                    children=[
                                        dcc.Upload(
                                    id='upload-data',
                                    children=html.Div([
                                        'Drag and Drop or ',
                                        html.A('Select Files.'),
                                        ' Max Size 1MB'
                                    ]),
                                    style={
                                        'width': '100%',
                                        'height': '60px',
                                        'lineHeight': '60px',
                                        'borderWidth': '1px',
                                        'borderStyle': 'dashed',
                                        'borderRadius': '5px',
                                        'textAlign': 'center',
                                        'margin': '10px'
                                    },
                                    # Allow multiple files to be uploaded
                                    multiple=False,
                                    max_size=1000000,
                                ),
                                        dcc.Store(
                                        id='aggregate_data')
                                        
                                        ],
                                ),
                            ],
                            id="upload_Container",
                            className="pretty_container"
                        ),
                    ],
                    className="twelve columns"

                ),

            ],
            id="row1",
            className="row"
        ),

        dcc.Loading(
            id="loading-2",
            type="default",
            children=html.Div(
                id="row2",
                className="row"
            ),
        ),

        html.Div(
            id="row3",
            className="row"
        ),




    ],
        id="mainContainer",
        style={
        "display": "flex",
        "flex-direction": "column"
    }
    )
