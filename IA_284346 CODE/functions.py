import csv
import pandas as pd
import yfinance as yf
import os  
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from datetime import datetime, timedelta


KLSE_TICKERS = {
    "Top Glove Corporation Bhd": "7113.KL",
    "Malayan Banking Berhad (Maybank)": "1155.KL",
    "Public Bank Berhad": "1295.KL",
    "CIMB Group Holdings Berhad": "1023.KL",
    "Petronas Chemicals Group Berhad": "5183.KL",
    "IHH Healthcare Berhad": "5225.KL",
    "Maxis Berhad": "6012.KL",
    "Digi.Com Berhad": "6947.KL",
    "Genting Berhad": "3182.KL",
    "Axiata Group Berhad": "6888.KL"
}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_email(email):
    if "@" not in email:
        print("Error: Invalid email. Email must include '@'.")
        return False
    return True


def validate_password(password):
    if len(password) < 8:
        print("Error: Password must be at least 8 characters.")
        return False
    return True


def register_user(email, password):
    if not validate_email(email) or not validate_password(password):
        return False

    try:
        with open("users.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email, password])
        return True
    except Exception as e:
        print(f"Error registering user: {e}")
        return False


def authenticate_user(email, password):
    try:
        with open("users.csv", mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == email and row[1] == password:
                    return True
        return False
    except FileNotFoundError:
        print("No users registered yet.")
        return False


def select_ticker():
    ticker_completer = WordCompleter(list(KLSE_TICKERS.keys()), ignore_case=True)

    print("Select a KLSE company to fetch stock data:")
    selected_company = prompt("Choose a company: ", completer=ticker_completer)

    
    ticker_symbol = KLSE_TICKERS.get(selected_company)
    if not ticker_symbol:
        print("Invalid selection. Please try again.")
        return None

    return ticker_symbol


def get_closing_prices(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            print(f"No data available for {ticker} in the selected period ({start_date} to {end_date}).")
            return None
        if "Close" not in data.columns:
            print(f"No closing prices found for {ticker}.")
            return None
        return data["Close"]
    except Exception as e:
        print(f"Error fetching stock data for {ticker}: {e}")
        return None


def analyze_closing_prices(data):
    if data is None or data.empty:
        print("No data available for analysis.")
        return None

    try:

        average_price = data.mean().item()  
        first_value = data.iloc[0].item() 
        last_value = data.iloc[-1].item()  
        percentage_change = ((last_value - first_value) / first_value) * 100
        percentage_change = round(percentage_change, 2)  
        highest_price = data.max().item()  
        lowest_price = data.min().item()  

        return {
            "average": average_price,
            "percentage_change": percentage_change, 
            "highest": highest_price,
            "lowest": lowest_price
        }
    except Exception as e:
        print(f"Error analyzing stock data: {e}")
        return None


def save_to_csv(data, filename):
    try:
        
        formatted_data = [
            f"{item:.2f}" if isinstance(item, (int, float)) else item for item in data
        ]

        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            if file.tell() == 0:  
                writer.writerow(["Email", "Ticker", "Average Closing Price", "Percentage Change", "Highest Price", "Lowest Price"])
            writer.writerow(formatted_data)
    except Exception as e:
        print(f"Error saving data to CSV: {e}")


def read_from_csv(filename, email_filter):
    try:
        data = pd.read_csv(filename)
        filtered_data = data[data['Email'] == email_filter]
        if filtered_data.empty:
            print("No data available for the entered email.")
        else:
            print(filtered_data.to_string(index=False))
    except FileNotFoundError:
        print("No data file found.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")

