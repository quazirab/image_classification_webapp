from dash import Dash
import json
import os
#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================
from app.dashboard.layouts import load_layout
from app.dashboard.callbacks import load_callbacks

asset_path = os.path.join(os.getcwd(),'assets')

class dashboard(Dash):
    def __init__(self,server):
        super(dashboard,self).__init__(__name__,assets_folder=asset_path, server=server,meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
        self._setup()

    def _setup(self):
        self.title = "Image Classification"
        load_layout(self)
        load_callbacks(self)