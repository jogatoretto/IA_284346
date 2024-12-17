from datetime import datetime, timedelta
from functions import (
    register_user, authenticate_user, get_closing_prices,
    analyze_closing_prices, save_to_csv, read_from_csv, clear_screen, select_ticker
)

def main():
    while True:
        clear_screen()  
        print("Welcome to the Stock Selection Tool!")
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            clear_screen() 
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if register_user(email, password):
                print("Registration successful!")
            else:
                print("Registration failed. Please try again.")
            input("Press Enter to continue...")

        elif choice == "2":
            clear_screen()  
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if authenticate_user(email, password):
                while True:
                    clear_screen()  
                    print(f"Welcome, {email}!")
                    print("\nSub-Menu:")
                    print("1. Fetch Stock Data")
                    print("2. View Saved Data")
                    print("3. Logout")
                    sub_choice = input("Choose an option: ")

                    if sub_choice == "1":
                        clear_screen()  
                        ticker = select_ticker()
                        if not ticker:
                            input("Press Enter to continue...")
                            continue

                        clear_screen()  
                        print("Choose backtesting period:")
                        print("1. Past Day")
                        print("2. Past Week")
                        print("3. Past Month")
                        period_choice = input("Enter your choice: ")

                        
                        current_date = datetime.today()
                        if period_choice == "1":
                            start_date = current_date - timedelta(days=1)
                        elif period_choice == "2":
                            start_date = current_date - timedelta(days=7)
                        elif period_choice == "3":
                            start_date = current_date - timedelta(days=30)
                        else:
                            print("Invalid choice. Using Past Day as default.")
                            start_date = current_date - timedelta(days=1)

                        start_date_str = start_date.strftime("%Y-%m-%d")
                        end_date_str = current_date.strftime("%Y-%m-%d")

                        
                        data = get_closing_prices(ticker, start_date_str, end_date_str)
                        if data is not None:
                            clear_screen()  
                            print("\nClosing Prices:")
                            print(data)

                            
                            analysis = analyze_closing_prices(data)
                            if analysis:
                                print("\nAnalysis Results:")
                                print(f"Average Closing Price: {analysis['average']:.2f}")
                                print(f"Percentage Change: {analysis['percentage_change']:.2f}%")
                                print(f"Highest Price: {analysis['highest']:.2f}")
                                print(f"Lowest Price: {analysis['lowest']:.2f}")

                                save_to_csv(
                                    [email, ticker, analysis['average'], analysis['percentage_change'], analysis['highest'], analysis['lowest']],
                                    "user_data.csv"
                                )
                                print("\nData saved successfully!")
                            else:
                                print("Failed to analyze data.")
                        else:
                            print("No data fetched. Please try again.")
                        input("Press Enter to continue...")

                    elif sub_choice == "2":
                        clear_screen()  
                        email_filter = input("Enter your email to filter data: ")
                        print("\nSaved Data:")
                        read_from_csv("user_data.csv", email_filter)
                        input("Press Enter to continue...")

                    elif sub_choice == "3":
                        clear_screen()
                        print("Goodbye !")
                        break
                         

                    else:
                        print("Invalid option. Try again.")
                        input("Press Enter to continue...")

            else:
                print("Invalid email or password.")
                input("Press Enter to continue...")

        elif choice == "3":
            clear_screen()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
