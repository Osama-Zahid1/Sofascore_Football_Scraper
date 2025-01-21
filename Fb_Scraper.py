import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Navigate to the Sofascore match day page
driver.get('https://www.sofascore.com/football/2024-10-05')

# Wait for the page to load
time.sleep(5)

# Find all match cells to click on
match_cells = driver.find_elements(By.CLASS_NAME, 'cBIkhT')

# Initialize an empty list to store match data
match_data = []

# Loop through each match cell and gather data
for match_cell in match_cells:
    match_cell.click()  # Click on the match to get details
    time.sleep(3)  # Allow time for the content to load

    # Wait for the teams to load
    try:
        teams = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'bnpRyo'))
        )
    except Exception as e:
        print(f"Error while waiting for teams to load: {e}")
        driver.back()  # Go back to the previous page
        continue

    # Print team elements to debug
    for team in teams:
        print(team.text)

    # Make sure there are enough teams to avoid IndexError
    if len(teams) < 2:
        print("Not enough teams found!")
        driver.back()  # Go back to the previous page
        continue

    # Extract team names
    try:
        home_team = teams[0].text  # Home team name
        away_team = teams[1].text  # Away team name
    except Exception as e:
        print(f"Error while extracting team names: {e}")
        driver.back()  # Go back to the previous page
        continue

    # Add extracted data to match_data list
    match_data.append({
        'Home Team': home_team,
        'Away Team': away_team,
        # You can extract additional data here and add to the dictionary
    })

    # Navigate back to the matches page
    driver.back()
    time.sleep(2)  # Wait for the matches page to load again

# Convert match data to DataFrame and save to CSV
df = pd.DataFrame(match_data)
df.to_csv('match_data.csv', index=False)

# Close the driver after finishing
driver.quit()
