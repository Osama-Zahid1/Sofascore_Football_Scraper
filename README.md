# Sofascore Football Match Scraper

This Python script automates the process of scraping football match details (home and away teams) from the Sofascore website for a specific match day. It utilizes Selenium WebDriver to interact with the webpage, extract data, and save it in a CSV file.

---

## Features
- **Automated Navigation:** Navigates through the Sofascore match day page and clicks on each match to extract details.
- **Data Extraction:** Retrieves the names of the home and away teams for each match.
- **Error Handling:** Handles scenarios where match details or team names are unavailable.
- **Data Storage:** Saves the extracted match data in a structured CSV file for further analysis.

---

## Prerequisites

1. **Python:** Ensure Python 3.7 or higher is installed.
2. **Selenium:** Install Selenium using the following command:
   ```bash
   pip install selenium
   ```
3. **Pandas:** Install Pandas for data manipulation:
   ```bash
   pip install pandas
   ```
4. **ChromeDriver:** Download the appropriate version of ChromeDriver for your Chrome browser from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/) and ensure it’s added to your system PATH.

---

## Setup and Usage

### 1. Clone or Download the Script
Save the script on your local machine.

### 2. Update the Target URL
Replace the target Sofascore URL in the script:
```python
driver.get('https://www.sofascore.com/football/2024-10-05')
```
Use the specific date or match day URL you want to scrape.

### 3. Run the Script
Execute the script in your terminal or IDE:
```bash
python script_name.py
```

### 4. Output
- The script creates a CSV file named `match_data.csv` in the same directory as the script.
- The file contains the following columns:
  - `Home Team`: Name of the home team.
  - `Away Team`: Name of the away team.

---

## Script Workflow

1. **Initialize WebDriver:** Sets up the Chrome WebDriver with required options.
2. **Navigate to Match Day Page:** Loads the specified Sofascore match day page.
3. **Extract Match Details:**
   - Clicks on each match cell to load detailed information.
   - Extracts the names of the home and away teams.
   - Handles scenarios where team names are unavailable or elements fail to load.
4. **Save Data to CSV:** Stores the extracted match data in a structured CSV format.
5. **Close WebDriver:** Ensures proper cleanup by closing the browser instance.

---

## Error Handling

- **Missing Elements:** If elements like team names or match cells are unavailable, the script handles the error, logs a message, and continues to the next match.
- **Navigation Errors:** The script navigates back to the match day page if an error occurs during data extraction.

---

## Limitations

- **Dynamic Website Changes:** If Sofascore updates its website structure or class names, the script may require modifications.
- **Static URL:** The target URL needs to be updated manually for different match days.
- **Page Load Delays:** Adjust sleep and timeout durations if the website takes longer to load.

---

## Future Improvements

- Add support for extracting additional match details (e.g., scores, match times).
- Implement dynamic URL generation based on user input for match day or league.
- Enhance performance using parallel processing for multiple matches.

---

## Disclaimer

This script is intended for educational purposes only. Ensure compliance with Sofascore's terms of service before using it for scraping data. Use responsibly and at your own risk.
