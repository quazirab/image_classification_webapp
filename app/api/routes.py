from flask import request,Response, Blueprint, jsonify, send_file
from flask_restful import Resource,Api
import json
from market_data import market_data

# ====================================================================

api_blueprint = Blueprint('api', __name__)
api =Api(api_blueprint)


def error_response(msg:str):
  return jsonify((dict(error=msg)))

@api.resource('/history')
class history(Resource):
    
    def get(self):
        if 'ticker' in request.args:
            ticker = request.args['ticker']

            with open('assets/tickers.json') as f:
                tickers = json.load(f)
            
            # Single line list comprehension
            tickers = [_ticker['value'] for _ticker in tickers]

            if ticker in tickers:
                return jsonify(market_data(ticker).dict_api)

            else:
                return error_response("Ticker not in S&P 500")
        else:
            return error_response("Required param: ticker")