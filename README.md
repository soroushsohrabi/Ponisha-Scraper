
# Ponisha Ads Extractor

## Description

Ponisha Ads Extractor is a Python script that uses Selenium to log in to the Ponisha website, extract job postings, and gather related data such as **job title**, **description**, **required skills**, and **salary**. This script automates the process of collecting job listings from Ponisha and saves them in a **JSON format**. The extracted data includes:

- **Job Title**
- **Job Description**
- **Required Skills**
- **Salary**

## Features

- Logs into Ponisha using a provided account.
- Scrapes job listings including:
  - **Job Title**
  - **Job Description**
  - **Required Skills**
  - **Salary**
- Utilizes Selenium WebDriver for dynamic content loading and interaction.
- Saves the data in **JSON format**.

## Requirements

Before running the script, you need to have the following dependencies installed:

- Python 3.6+
- `selenium` for web scraping.
- `chromedriver` for browser automation (make sure you have the correct version for your Chrome browser).

Install the required libraries by running the following command:

```bash
pip install selenium
```

You also need to have `chromedriver` installed and added to your PATH. You can download it from [here](https://sites.google.com/chromium.org/driver/).

## Installation

1. **Clone the repository:**

   ```bash
   git clone git clone https://github.com/soroushsohrabi/Ponisha-Scraper.git
   ```

2. **Install dependencies:**

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

   The script will save the extracted job listings in a JSON file named `ads.json`. The file will contain the following structure:

   ```json
   [
       {
           "title": "Job Title",
           "description": "Job Description",
           "skills": "Required Skills",
           "salary": "Salary"
       },
       ...
   ]
   ```

   Example of a saved entry in `ads.json`:

   ```json
   {
       "title": "Web Developer",
       "description": "Develop and maintain websites.",
       "skills": "Python, Django, HTML, CSS",
       "salary": "100,000 IRR/month"
   }
   ```

## Contributing

Contributions to this project are welcome! If you find any bugs or want to add new features, feel free to fork the repository and submit a pull request.
