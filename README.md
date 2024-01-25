# Email Validator EV - Version 1.0

![Cat Art](cat_art.png)

**Support:** Demonofinternet0@gmail.com  
**Youtube:** DemonofInternet

## Description
Email Validator EV is a script that allows you to validate email addresses using different validation services.

## Setup

### Prerequisites
Make sure you have the following installed on your machine:

- Python (version 3.6 or higher)

### Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/email-validator-ev.git
    cd email-validator-ev
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration
Before using the script, you need to configure your API keys for the validation services. Follow these steps:

1. Open the script (`email_validator_ev.py`) in a text editor.

2. Find the section with the default API keys:

    ```python
    ZEROBOUNCE_API_KEY = "Paste_Your_Api_Key_Here"
    ABSTRACT_API_KEY = "Paste_Your_Api_Key_Here"
    PROOFY_API_KEY = "Paste_Your_Api_Key_Here"
    PROOFY_USER_ID = "Paste_Your_Api_Key_Here"
    ```

3. Replace the default API keys with your own keys.

4. Save the file.

## Usage

### Single Email Validation
1. Run the script:

    ```bash
    python email_validator_ev.py
    ```

2. Choose the validation service and select "Single Email Validation."

3. Enter the email address when prompted.

### Bulk Email Validation
1. Prepare a text file with one email address per line.

2. Run the script:

    ```bash
    python email_validator_ev.py
    ```

3. Choose the validation service and select "Bulk Email Validation."

4. Enter the path to the file when prompted.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
