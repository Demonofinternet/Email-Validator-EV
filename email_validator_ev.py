import os
import requests
import logging
from requests.exceptions import RequestException

# Define file name and version
support ="Support: Demonofinternet0@gmail.com"
youtube = "Youtube: DemonofInternet"
file_name = "Email Validator EV"
version = "1.0"

# ASCII art of a cat with file name and version
cat_art = f"""
  /\_/\\  
 ( o.o ) 
  > ^ <

********** {file_name} - Version {version} **********

 {support}
 {youtube}
"""

# Configuring logging
def setup_logging():
    logging.basicConfig(filename='validation_logs.log', level=logging.INFO,
                        format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Do not modify or remove the credit section below.
# This script is created by @Doimous.
# If you find this tool helpful, consider providing credit to the author.
CREDIT_SECTION = """
********** Created By Telegram ID: @Doimous **********
Donate to Bitcoin: 1PhgZqoWxr33mTSGefB1dW3QhjLVrG4MCV
Donate to USDT TRON(TRC20): TCXRkkQ27xdHUxTnEM1WJdneJfHtU4vpPo

For assistance and support, please reach out to Demonofinternet0@gmail.com
"""

# Default API keys
ZEROBOUNCE_API_KEY = "25a084ff87d04f04b59ec391d0772e0b"
ABSTRACT_API_KEY = "508d6a5d8dd94bc998c8f745e0640261"
PROOFY_API_KEY = "ORReeSFspsJh4EJzcGIWBS7P"
PROOFY_USER_ID = "56222"

def configure_logging():
    logging.getLogger().handlers = []
    logging.basicConfig(filename='validation_logs.log', level=logging.INFO,
                        format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def configure_settings():
    global ZEROBOUNCE_API_KEY, ABSTRACT_API_KEY, PROOFY_API_KEY, PROOFY_USER_ID
    print("***** Configuration Settings *****")
    ZEROBOUNCE_API_KEY = input("Enter your ZeroBounce API key (press Enter to keep default): ").strip() or ZEROBOUNCE_API_KEY
    ABSTRACT_API_KEY = input("Enter your Abstract API key (press Enter to keep default): ").strip() or ABSTRACT_API_KEY
    PROOFY_API_KEY = input("Enter your Proofy API key (press Enter to keep default): ").strip() or PROOFY_API_KEY
    PROOFY_USER_ID = input("Enter your Proofy User ID (press Enter to keep default): ").strip() or PROOFY_USER_ID
    print("***** Configuration Updated Successfully *****")

    # Update the default API keys
    update_default_keys()

def update_default_keys():
    # Update the default API keys in the script
    global ZEROBOUNCE_API_KEY, ABSTRACT_API_KEY, PROOFY_API_KEY, PROOFY_USER_ID
    with open(__file__, 'r') as file:
        script_content = file.read()

    script_content = script_content.replace('"25a084ff87d04f04b59ec391d0772e0b"', f'"{ZEROBOUNCE_API_KEY}"')
    script_content = script_content.replace('"508d6a5d8dd94bc998c8f745e0640261"', f'"{ABSTRACT_API_KEY}"')
    script_content = script_content.replace('"ORReeSFspsJh4EJzcGIWBS7P"', f'"{PROOFY_API_KEY}"')
    script_content = script_content.replace('"56222"', f'"{PROOFY_USER_ID}"')

    with open(__file__, 'w') as file:
        file.write(script_content)

def reset_default_keys():
    # Reset the default API keys to the original values
    global ZEROBOUNCE_API_KEY, ABSTRACT_API_KEY, PROOFY_API_KEY, PROOFY_USER_ID
    ZEROBOUNCE_API_KEY = "25a084ff87d04f04b59ec391d0772e0b"
    ABSTRACT_API_KEY = "508d6a5d8dd94bc998c8f745e0640261"
    PROOFY_API_KEY = "ORReeSFspsJh4EJzcGIWBS7P"
    PROOFY_USER_ID = "56222"

    # Update the default API keys in the script
    update_default_keys()

def validate_email_with_zerobounce(email):
    api_endpoint = "https://api.zerobounce.net/v2/validate"
    params = {"email": email, "api_key": ZEROBOUNCE_API_KEY}

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(api_endpoint, params=params, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses

        result = response.json()

        if "status" in result:
            if result["status"] == "valid":
                log_result(email, True, 'zerobounce')
                return True
            else:
                log_result(email, False, 'zerobounce')
                return False
        else:
            logging.error(f"Error in ZeroBounce API response: {result}")
            return False

    except RequestException as e:
        logging.error(f"Error calling ZeroBounce API: {str(e)}")
        return False

def validate_email_with_abstractapi(email):
    api_endpoint = "https://emailvalidation.abstractapi.com/v1"
    params = {"api_key": ABSTRACT_API_KEY, "email": email}

    try:
        response = requests.get(api_endpoint, params=params)
        response.raise_for_status()

        result = response.json()

        if "deliverability" in result and result["deliverability"] == "DELIVERABLE":
            log_result(email, True, 'abstractapi')
            return True
        else:
            log_result(email, False, 'abstractapi')
            return False

    except RequestException as e:
        logging.error(f"Error calling Abstract API: {str(e)}")
        return False

def validate_email_with_proofy(email):
    api_endpoint = "https://api.proofy.io/verifyaddr"
    params = {"aid": PROOFY_USER_ID, "key": PROOFY_API_KEY, "email": email}

    try:
        response = requests.get(api_endpoint, params=params)
        response.raise_for_status()

        result = response.json()

        if "cid" in result:
            check_id = result["cid"]
            return get_proofy_result(check_id, email)
        else:
            logging.error(f"Error in Proofy.io API response: {result}")
            return False

    except RequestException as e:
        logging.error(f"Error calling Proofy.io API: {str(e)}")
        return False

def get_proofy_result(check_id, email):
    api_endpoint = "https://api.proofy.io/getresult"
    params = {"aid": PROOFY_USER_ID, "key": PROOFY_API_KEY, "cid": check_id}

    try:
        response = requests.get(api_endpoint, params=params)
        response.raise_for_status()

        result = response.json()

        if "checked" in result and result["checked"]:
            email_result = next((item for item in result["result"] if item["email"] == email), None)
            if email_result:
                status_name = email_result["statusName"]
                log_result(email, status_name == "deliverable", 'proofy')
                return status_name == "deliverable"
            else:
                logging.error(f"Email {email} not found in Proofy.io result.")
                return False
        else:
            logging.error(f"Error in Proofy.io result: {result}")
            return False

    except RequestException as e:
        logging.error(f"Error getting Proofy.io result: {str(e)}")
        return False

def log_result(email, is_valid, service):
    filename = f"validemail_{service}.txt" if is_valid else f"unvalidemail_{service}.txt"
    with open(filename, "a") as file:
        file.write(f"{email}\n")

def display_menu():
    clear_console()
    print(cat_art)
    print("********** Email Validator **********")
    print("1. Validate with ZeroBounce")
    print("2. Validate with Abstract")
    print("3. Validate with Proofy")
    print("4. Configure Settings")
    print("5. Exit")

def get_user_choice(valid_choices):
    while True:
        user_input = input("Enter your choice: ").strip()
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid choice. Please enter a valid option.")

def api_menu(api_name, validate_function):
    while True:
        clear_console()
        print(cat_art)
        print(f"********** {api_name} Validation **********")
        print("1. Single Email Validation")
        print("2. Bulk Email Validation")
        print("3. Back to Main Menu")

        valid_choices = ["1", "2", "3"]
        api_choice = get_user_choice(valid_choices)

        if api_choice == "1":
            single_email_validator(validate_function, api_name)
            break
        elif api_choice == "2":
            bulk_email_validator(validate_function, api_name)
            break
        elif api_choice == "3":
            break


def single_email_validator(validate_function, service):
    email = input("Enter the email address to validate: ")
    try:
        is_valid = validate_function(email)
        result_text = f"{email} is {'valid' if is_valid else 'invalid'}.\n"
        print(result_text)
        display_credit()
        logging.info(f"Validation result for {email} using {service}: {'valid' if is_valid else 'invalid'}")
    except Exception as e:
        logging.error(f"Error during validation: {str(e)}")
        print("An error occurred during validation. Please check logs for more details.")
    
    # Ask for user's choice again
    input("Press Enter to continue...")

def bulk_email_validator(validate_function, service):
    file_path = input("Enter the path to the file containing email addresses: ")
    try:
        with open(file_path, "r") as file:
            emails = file.read().splitlines()

        for email in emails:
            try:
                is_valid = validate_function(email)
                result_text = f"{email} is {'valid' if is_valid else 'invalid'}."
                print(result_text)
                logging.info(f"Validation result for {email} using {service}: {'valid' if is_valid else 'invalid'}")
            except Exception as e:
                logging.error(f"Error during validation of {email}: {str(e)}")

        print("\nBulk validation completed.")
        display_credit()
        
    except FileNotFoundError:
        logging.error(f"Error: File '{file_path}' not found.")
        print(f"Error: File '{file_path}' not found.")
    
    # Ask for user's choice again
    input("Press Enter to continue...")

def display_credit():
    print(CREDIT_SECTION)

def clear_console():
    # Clear console in a cross-platform way
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    try:
        setup_logging()  # Centralized logging configuration
        while True:
            display_menu()
            valid_choices = ["1", "2", "3", "4", "5"]
            choice = get_user_choice(valid_choices)

            # Clear the console before processing the user's choice
            clear_console()

            if choice == "1":
                api_menu("ZeroBounce", validate_email_with_zerobounce)
            elif choice == "2":
                api_menu("Abstract", validate_email_with_abstractapi)
            elif choice == "3":
                api_menu("Proofy", validate_email_with_proofy)
            elif choice == "4":
                settings_menu()
            elif choice == "5":
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Exiting gracefully. Goodbye!")

def settings_menu():
    while True:
        display_settings_menu()
        valid_choices = ["1", "2", "3"]  # Include "3" as a valid choice
        choice = get_user_choice(valid_choices)

        if choice == "1":
            configure_settings()
        elif choice == "2":
            confirm_reset = input("Are you sure you want to reset API keys? (Y/N): ").strip().upper()
            if confirm_reset == "Y":
                reset_default_keys()
                print("***** API Keys Reset Successfully *****")
            else:
                print("API Keys reset aborted.")
        elif choice == "3":
            break  # Break out of the settings menu and return to the main menu
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def display_settings_menu():
    print(cat_art)
    print("********** Settings Menu **********")
    print("1. Configure API Keys")
    print("2. Reset API Keys")
    print("3. Back to Main Menu")

if __name__ == "__main__":
    main()
