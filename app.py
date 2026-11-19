import os
from flask import Flask, jsonify
import requests
from dotenv import load_dotenv

# load env values
load_dotenv()

app = Flask(__name__)

FINNHUB_API= os.getenv("FINNHUB_API")

FINNHUB_ADDRESS = "https://finnhub.io/api/v1/quote"

@app.route("/price/<ticker>", methods=["GET"])
def get_stock_price(ticker):
    """CAll finnhub API for market price of stock"""

    if not FINNHUB_API:
        return jsonify({"error": "finnhub API key not configured"}), 503

    ticker = ticker.strip().upper()

    if not ticker or len(ticker) > 5:
        return jsonify({"error":" Invalid ticker"}), 400

    try:
        response = requests.get(
            FINNHUB_ADDRESS, params={"symbol": ticker, "token":FINNHUB_API}, timeout=6
            )

        response.raise_for_status()

        stock_info = response.json()
        current_price = stock_info.get("c")

        if not isinstance(current_price, (int,float)) or current_price <= 0:
            return jsonify({"error": "No valid stock price"}), 404

        return jsonify({
            "ticker": ticker,
            "current_price": str(current_price),
            "currency": "USD",
            "timestamp": stock_info.get("t")
        }), 200

    except requests.exceptions.RequestException as error:
        print(f"API request error: {error}")
        return jsonify({"error":"Price unavailable"}), 503

    except (ValueError, TypeError, AttributeError):
        return jsonify({"error": "Invalid response from PAI server"}), 502

if __name__ == "__main__":
    app.run(port=5003, debug =True)