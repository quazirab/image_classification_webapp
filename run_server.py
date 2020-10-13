# from market_data import market_data

# md = market_data("AAPL")

# print(md.df.index.date)

from app import create_server
server = create_server()

if __name__ == '__main__':
    server.run(debug=True)