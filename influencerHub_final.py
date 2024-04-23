from tabulate import tabulate

#sample database
KOL_database = [
     {'username': '@budireview', 
      'name'    : 'Budi',
      'industry': 'Technology', 
      'location': 'Jakarta', 
      'fol_count': 116000, 
      'avg_views': 110000, 
      'rate': 6250000, 
      'email': 'budi@ganteng.com'
      },
     {'username': '@ratunyemil',
      'name': 'Ratu',
      'industry': 'Culinary', 
      'location': 'Bandung', 
      'fol_count': 621000, 
      'avg_views': 607000, 
      'rate': 17500000, 
      'email': 'ratu@kenyang.com'
      },
     {'username': '@tamitami',
      'name': 'Tami',
      'industry': 'Fashion',
      'location': 'Surabaya',
      'fol_count': 408000,
      'avg_views': 534000,
      'rate': 12000000,
      'email': 'tami@cantik.com'
      },
      {'username': '@kitajalan',
      'name': 'Kiki',
      'industry': 'Travel',
      'location': 'Surabaya',
      'fol_count': 273000,
      'avg_views': 398000,
      'rate': 9800000,
      'email': 'kita@capek.com'
      },
]

#display the main menu options
def display_menu():
    print("""
Main Menu List:
1. Show database
2. Filter database
3. Add new influencer
4. Remove an influencer
5. Edit influencer data
6. Compare CPV
7. Exit Program""")

#display the influencer database
def display_database():
    headers = ["Index", "Username", "Name", "Industry", "Location", "Follower Count", "Average Views", "Rate per Video", "E-mail"]
    table_data = [(index+1, KOL['username'], KOL['name'], KOL['industry'], KOL['location'], KOL['fol_count'], KOL['avg_views'], KOL['rate'], KOL['email']) for index, KOL in enumerate(KOL_database)]
    print(tabulate(table_data, headers=headers, stralign="center", numalign="center", tablefmt="fancy_outline"))

#filter the database based on specified criteria
def filter_database(industry=None, location=None, min_fol_count=None, max_fol_count=None, min_avg_views=None, max_avg_views=None, min_rate=None, max_rate=None):
    filtered_KOL = []
    while True:
        print("""
Filter Options:
1. Industry
2. Location
3. Follower Count
4. Average Views
5. Rate per Video
6. Return to Main Menu
              """)
        filter_choice = input("Enter your choice (1-6): ")
        if filter_choice in ["1", "2"]:
            # Filter by industry or location
            field = "industry" if filter_choice == "1" else "location"
            value = input(f"Enter {field.capitalize()}: ")
            filtered_KOL = [KOL for KOL in KOL_database if KOL[field].lower() == value.lower()]
        elif filter_choice in ["3", "4", "5"]:
            # Filter by follower count, average views, or rate per video
            fields = ["fol_count", "avg_views", "rate"]
            field = fields[int(filter_choice) - 3]
            min_value = input(f"Enter minimum {field.replace('_', ' ').capitalize()}: ")
            max_value = input(f"Enter maximum {field.replace('_', ' ').capitalize()}: ")
            if min_value.isdigit() and max_value.isdigit():
                min_value, max_value = int(min_value), int(max_value)
                filtered_KOL = [KOL for KOL in KOL_database if min_value <= KOL[field] <= max_value]
            else:
                print(f"Error: {field.replace('_', ' ').capitalize()} must be a valid integer. Please try again.")
                continue
        elif filter_choice == "6":
            # Returning to main menu
            break
        else:
            print("Invalid choice. Please enter a valid choice (1-6).")
            continue
        
        # Displaying the result (if available)
        headers = ["Username", "Name", "Industry", "Location", "Follower Count", "Average Views", "Rate per Video", "E-mail"]
        table_data = [(KOL['username'], KOL['name'], KOL['industry'], KOL['location'], KOL['fol_count'], KOL['avg_views'], KOL['rate'], KOL['email']) for KOL in filtered_KOL]
        if table_data:
            print("\nFiltered Result:")
            print(tabulate(table_data, headers=headers, stralign="center", numalign="center", tablefmt="fancy_outline"))
            break
        else:
            print("No influencers match the specified filters.")
            return

#validate integer
def valid_int(prompt):
    while True:
        user_input = input(prompt)
        if user_input:
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Please enter a number for this column. Please try again.")
        else:
            print("Input cannot be empty.")

#validate string
def valid_str(prompt):
    while True:
        user_input = input(prompt)
        if user_input:
                return (user_input).capitalize()
        else:
            print("Input cannot be empty.")

#add new influencer to the database
def add_influencer():
    while True:
        print("""
Add influencer options:
1. Add influencer
2. Return to Main Menu
              """)
        filter_choice = input("Enter your choice (1-2): ")
        if filter_choice == "1":
            display_database()
            input_username = valid_str("Enter the influencer's username (starting with @): ")
            if not input_username.startswith("@"):
                print("Username must start with @.")
                continue
            if any(KOL['username'] == input_username for KOL in KOL_database):
                print("\nThis username is already in the database. Please edit their existing data instead.")
                return
            input_name = valid_str("Enter the influencer's name: ")
            input_industry = valid_str("Enter the influencer's industry: ")
            input_location = valid_str("Enter the influencer's location: ")
            input_fol_count = valid_int("Enter the influencer's follower count: ")
            input_avg_views = valid_int("Enter the influencer's average views: ")
            input_rate = valid_int("Enter the influencer's rate per video: ")
            while True:
                input_email = input("Enter the influencer's e-mail (please include @ and .): ")
                if "@" in input_email and "." in input_email:
                    break
                else:
                    print("Invalid email format. Please include @ and . in the email address.")
            KOL_database.append({
                'username': input_username,
                'name': input_name, 
                'industry': input_industry, 
                'location': input_location, 
                'fol_count': input_fol_count, 
                'avg_views': input_avg_views, 
                'rate': input_rate, 
                'email': input_email
            })
            print("\nThe new data has been successfully inserted into the database.")
            display_database()
            break
        elif filter_choice == "2":
            break
        else:
            print("Invalid choice. Please enter a valid option (1-2).")

#prompts the user to enter the influencer's index
def user_prompt(key):
    while True:
        user_input = input(f"\nwhich influencer do you want to {key}? Please enter their index number:")
        if user_input.isdigit():
            if 0 < int(user_input) <= len(KOL_database):
                return int(user_input)
            else:
                print("Invalid Index. Please enter a valid index.")
        else:
            print("Invalid input. Please insert a number.")

#removes an influencer from the database
def remove_influencer():
    print("""
Remove influencer options:
1. Remove influencer
2. Return to Main Menu
              """)
    while True:
        remove_choice = valid_int("Enter your choice (1-2): ")
        if remove_choice == 1:
            while True:
                display_database()
                del_input = valid_int("Enter the index of the influencer to remove: ")
                if 1 <= del_input <= len(KOL_database):
                    del KOL_database[del_input - 1]
                    print("The data has been successfully removed from the database.")
                    print("\nHere is the current database:")
                    display_database()
                    break
                else:
                    print("Invalid index. Please enter a valid index.")
            break
        elif remove_choice == 2:
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

#edit data of an existing influencer in the database
def edit_influencer():
    while True:
        print("""
Edit influencer options:
1. Edit influencer
2. Return to Main Menu
              """)
        edit_choice = valid_int("Enter your choice (1-2): ")
        if edit_choice == 1:
            display_database()
            index_input = user_prompt("edit")
            index = index_input - 1
            if index >= 0:
                print("""
Which part of the data do you want to edit?
1. Influencer's username
2. Influencer's name
3. Influencer's industry
4. Influencer's location
5. Influencer's follower count
6. Influencer's average views
7. Influencer's rate per video
8. Influencer's e-mail  
""")
                choice_input = valid_int("Enter the number of the part that you want to edit: ")
                if 1 <= choice_input <= 8:
                    fields = ["username", "name", "industry", "location", "fol_count", "avg_views", "rate", "email"]
                    field = fields[choice_input - 1]
                    if field in {"name", "industry", "location"}:
                        new_value = input(f"Enter the new value for the influencer's {field}: ").capitalize()
                    elif field in {"fol_count", "avg_views", "rate"}:
                        while True:
                            new_value = input(f"Enter the new value for the influencer's {field}: ")
                            if new_value.isdigit():
                                new_value = int(new_value)
                                break
                            else:
                                print("Invalid input. Please enter a valid integer.")
                    elif field in {"email"}:
                        while True:
                            new_value = input(f"Enter the new value for the influencer's {field}: ")
                            if "@" in new_value and "." in new_value:
                                break
                            else:
                                print("Invalid email format. Please include @ and . in the email address.")
                    KOL_database[index][field] = new_value
                    print("\nThe data has been successfully updated.")
                    display_database()
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 8.")
            else:
                print("Invalid index. Please enter a valid index.")
        elif edit_choice == 2:
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
#compare CPV of selected influencers    
from tabulate import tabulate

def compare_CPV():
    while True:
        print("""
Cost per View (CPV) Comparison options:
1. Compare CPV
2. Return to Main Menu
              """)
        choice = input("Enter your choice (1-2): ")
        
        if choice == "1":
            print("Which influencer(s) do you want to compare?")
            display_database()
            comparison = []
            selected_indices = set()
            
            while True:
                index_input = input("\nPlease enter the influencer's index number (or type 'done' to finish): ")
                
                if index_input.lower() == "done":
                    break
                elif index_input.isdigit():
                    index = int(index_input) - 1
                    
                    if 0 <= index < len(KOL_database) and index not in selected_indices:
                        influencer = KOL_database[index]
                        cpv = influencer["rate"] / influencer["avg_views"]
                        comparison.append((influencer["username"], influencer["rate"], influencer["avg_views"], cpv))
                        selected_indices.add(index)
                    else:
                        print("Invalid index or influencer already selected. Please choose another.")
                else:
                    print("Invalid input. Please enter a valid index number or 'done' to finish.")
            
            if not comparison:
                print("No influencers selected for comparison.")
                return
            
            print("\nCost per View (CPV) Comparison List:")
            headers = ["Username", "Rate", "Average Views", "CPV"]
            comparison.sort(key=lambda x: x[3])  # Sort by CPV
            table_data = [[username, rate, avg_views, cpv] for username, rate, avg_views, cpv in comparison]  # Corrected line
            print(tabulate(table_data, headers=headers, stralign="center", numalign="center", tablefmt="fancy_outline"))
            
            while True:
                analysis_option = input("""
What would you like to do next?
1. Show influencer(s) with the highest CPV
2. Show influencer(s) with the lowest CPV
3. Show mean CPV of all influencers
4. Return to main menu
                                
Enter your choice (1/2/3/4): """)
                
                if analysis_option == "1":
                    print(f"\nThe influencer(s) with the highest CPV: {[name for name, _, _, cpv in comparison if cpv == comparison[-1][3]]}")
                elif analysis_option == "2":
                    print(f"\nThe influencer(s) with the lowest CPV: {[name for name, _, _, cpv in comparison if cpv == comparison[0][3]]}")
                elif analysis_option == "3":
                    print(f"\nThe mean CPV of all influencers is: {sum(cpv for _, _, _, cpv in comparison) / len(comparison):.2f}")
                elif analysis_option == "4":
                    return
                else:
                    print("Invalid input. Please enter 1, 2, 3, or 4.")
        elif choice == "2":
            return
        else:
            print("Invalid choice. Please enter 1 or 2.")

#welcome message
print("""        
Welcome to TikTokerHub!
A TikTok influencer database for KOL Specialists.
How can we help you today?""")
#main menu
while True:    
    display_menu()
    menu_input = input("\nPlease insert a number from the menu: ")
    if menu_input.isdigit():
        menu = int(menu_input)
        if 1 <= menu <= 7:
            if menu == 1:
                display_database()
            elif menu == 2:
                display_database()
                filter_database()
            elif menu == 3:
                add_influencer()
            elif menu == 4:
                remove_influencer()
            elif menu == 5:
                edit_influencer()
            elif menu == 6:
                compare_CPV()
            elif menu == 7:
                print("Thank you for using TikTokerHub. We hope to see you again!")
                break
        else:
            print("\nThe number you inserted is not listed in the menu. Please try again.")
    else:
        print("\nInvalid input. Please insert a number.")
