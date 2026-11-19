# Stock Data Service

A Python Flask REST API microservice that retrieves stock market prices using Finnhub.

## Features

- Retrieves the latest available stock price by ticker symbol.
- Returns stock price information in JSON format.
- Handles invalid or unavailable stock prices.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file containing:

```text
FINNHUB_API=your_api_key
```

Run the service:

```bash
python app.py
```

## API

**GET /price/{ticker}**

Example:

`http://127.0.0.1:5003/price/AAPL`

## Development Status

Initial API implementation completed. Additional functionality will be added as development continues.