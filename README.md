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

1. Start the Program:
  Run python main.py in the terminal.
  
2. Register or Login:
  Register as a new user with your email and a secure password.
  Login to access the main functionalities.
  
3. Select a Stock Ticker:
  Type the initial letter and choose the drop-down menu to select a company ticker 

    •	        Top Glove Corporation Bhd: 7113.KL

    •	        Malayan Banking Berhad (Maybank): 1155.KL

    •	        Public Bank Berhad: 1295.KL

    •	        CIMB Group Holdings Berhad: 1023.KL

    •	        Petronas Chemicals Group Berhad: 5183.KL

    •	        IHH Healthcare Berhad: 5225.KL

    •	        Maxis Berhad: 6012.KL

    •	        Digi.Com Berhad: 6947.KL

    •	        Genting Berhad: 3182.KL

    •	        Axiata Group Berhad: 6888.KL

  
4. Choose a Backtesting Period:
  Select one of the three available options:

    •     Past Day

    •     Past Week

    •     Past Month
    
6. View Analysis Results:
  The program will fetch historical stock data, analyze it, and display results including:
    Average closing price.
    Percentage change.
    Highest and lowest prices.
    
7. Save and View Data:
  Results are saved automatically in user_data.csv.
  
**You can view previously saved data by filtering it with your email.**
