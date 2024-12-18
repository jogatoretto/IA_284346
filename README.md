# STOCK SELECTION TOOL


**Stock Selection Tool: Setup and Installation**

System Requirements
Ensure your system meets the following requirements:

Python Version: 3.7 or later.

Operating System: Windows, macOS, or Linux.

Required Libraries:

**pandas** , 
**yfinance** ,
**prompt_toolkit** ,

**Folder Structure**
The project folder is structured as follows:


├── main.py          # Main script managing user interaction

├── functions.py     # Core functions for authentication, analysis, and data handling

├── users.csv        # (Auto-generated) File storing user credentials

├── user_data.csv    # (Auto-generated) File storing analysis results


**How to Use the Tool**

Start the Program:
  Run python main.py in the terminal.
  
Register or Login:
  Register as a new user with your email and a secure password.
  Login to access the main functionalities.
  
Select a Stock Ticker:
  Use the drop-down menu to select a company ticker (e.g., 7113.KL for Top Glove).
  
Choose a Backtesting Period:
  Select one of the three available options:
  
    Past Day 
    
    Past Week
    
    Past Month
    
View Analysis Results:
  The program will fetch historical stock data, analyze it, and display results including:
    Average closing price.
    Percentage change.
    Highest and lowest prices.
    
Save and View Data:
  Results are saved automatically in user_data.csv.
  
**You can view previously saved data by filtering it with your email.**
