# BIN Info Checker

BIN Info Checker is a Python script that fetches information about a Bank Identification Number (BIN) from an API and displays it in a user-friendly format.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/emenmousavi/lightBIN-2
   ```

2. Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Usage

Run the script with the following command:

  ```bash
  python lightbin2.py
  ```

# Command-Line Options
-b BIN_NUMBER, --bin BIN_NUMBER: Specify the BIN number to fetch information for.
-v, --verbose: Enable verbose mode to display detailed information during execution.
-o {json,csv}, --output {json,csv}: Specify the output format as JSON or CSV. Default is console output.
