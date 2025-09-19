
# Ponisha Ads Extractor

## Description

Ponisha Ads Extractor is a Python script that uses Selenium to log in to the Ponisha website, extract job postings, and gather related data such as titles, descriptions, and other job-specific information. This script is designed to automate the process of collecting job listings from Ponisha, making it easy for users to gather job data for analysis, research, or archiving.

## Features

- Logs into Ponisha using a provided account.
- Scrapes job listings, including titles, descriptions, and other relevant details.
- Utilizes Selenium WebDriver for dynamic content loading and interaction.
- Simple to use and configure for various scraping needs.

## Requirements

Before running the script, you need to have the following dependencies installed:

- Python 3.6+
- `selenium` for web scraping.
Install the required libraries by running the following command:

```bash
pip install selenium
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/soroushsohrabi/Ponisha-Scraper.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd ponisha-ads-extractor
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Configure the script:**

   Open `ads_extractor.py` and modify the login credentials for the Ponisha website (if needed).

   ```python
   driver.get("https://ponisha.ir/")
   inpts = driver.find_elements(By.ID, "input-username")
   inpts[0].send_keys("your_email")
   ```

2. **Run the script:**

   To start extracting job ads from Ponisha, run the following command:

   ```bash
   python ads_extractor.py
   ```

   The script will log in to the Ponisha platform, navigate to the appropriate sections, and begin scraping job ads.

3. **Check the output:**

   The script will print job listings to the console, or you can modify the script to save the output to a CSV or JSON file.

## Example Output

The script will output job listings in a structured format with details such as:

- **Job Title**
- **Job Description**
- **Skills_required**
- **Salary**

## Contributing

Contributions to this project are welcome! If you find any bugs or want to add new features, feel free to fork the repository and submit a pull request.
