# WebScraping_Cyberport_Startups

## Introduction
The Cyberport Startup Repository Scraper is a Python and Selenium based web scraping project designed to automate the extraction of startup information from the Cyberport Startup Repository website. This tool navigates through multiple pages of the website, extracts relevant data fields, and compiles them into a structured format for further analysis or reporting. The scraped data is then exported to a CSV or Excel file for easy access and manipulation.

## Approach
### 1. Basic Viewing on the Repository
<img width="1000" alt="photo" src="https://github.com/user-attachments/assets/31ea8584-8854-4c24-9d14-db56b29fb58b">
<img width="1000" alt="photo" src="https://github.com/user-attachments/assets/5a373994-5dd4-40bf-afb8-0da9619a917d">

- Items are placed in the grey background area on the right.
- 6 items are shown in each page.
- 236 pages in total
- 
### 2. Page for Each Item 
<img width="1281" alt="photo 2024-07-31 上午2 03 06" src="https://github.com/user-attachments/assets/c2d3e06f-6d0d-40d5-bf2f-3446110bd6d2">

**Columns:**
- Contest-year
- Award
- Intake Month
- Intake Year
- Website
- Cyberport Community Status
- Technology Sector

### 3. Set Up All Target Columns
<img width="700" alt="photo" src="https://github.com/user-attachments/assets/0526a1c7-f66b-48e3-be5f-eb1601ee299a">

- Set up all the common and target fields.
- For those fields that does not appear often, the program will handle later.


### 4. Travel Each Page of the Database
<img width="804" alt="photo" src="https://github.com/user-attachments/assets/0eeed669-7601-4d71-b548-1ab19b84c2a8">

- Extract all the name and page url of each item.

  
### 5. Travel the Page of Each Item
<img width="500" alt="photo" src="https://github.com/user-attachments/assets/8783db0f-8f6e-42f8-bfe3-bad249ddea47">
<img width="500" alt="photo" src="https://github.com/user-attachments/assets/8f868a2b-e345-46ce-a665-ed47ea921f7d">

- Find out all the key-value div. 
- See what fields are shown in the page by checking the text.
- Cache the information and add it to the correspoding list mapped by the field text.
- Afterwards, add "NA" to the lists of fields which are not shown in the page.
- For those fields whcih are not our target, the program will report them as new attributes.

### 6. Data Export:
<img width="800" alt="螢幕截圖 2024-07-31 上午2 30 32" src="https://github.com/user-attachments/assets/a8ccbf2d-0329-46b9-9b3e-69a08eeddff1">

- The output_to_file method compiles the scraped data into a Pandas DataFrame and exports it to a specified CSV or Excel file.
  
