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
<img width="500" alt="photo" src="https://github.com/user-attachments/assets/3b5b45b3-2ad3-428c-a81e-ac4825dc2bb3">

- Set up all the common and target fields.
- For those fields that does not appear often, the program will handle later.


### 4. Travel Each Page of the Repository
<img width="881" alt="photo" src="https://github.com/user-attachments/assets/808e230c-9d49-4494-b60f-30507f7ea433">

- Extract all the name and page url of each item.
- With `self.load_page(url)` function, once the scraper is stuck on loading a page for 10 seconds, a `TimeoutException` will be thrown.
  Once the error is catched, the scraper will log this error and call `self.load_page(url)` again, to reload the same webpage.  
  The recursive `self.load_page(url)` function avoids the bug where the scraper would get stuck loading the page and cannot exit.

  
### 5. Travel the Page of Each Item
<img width="500" alt="photo" src="https://github.com/user-attachments/assets/8783db0f-8f6e-42f8-bfe3-bad249ddea47">
<img width="500" alt="螢幕截圖 2024-07-31 上午6 07 51" src="https://github.com/user-attachments/assets/f3ae8e89-eaeb-4db2-8f62-38dee0cd7d36">


- Find out all the key-value div. 
- See what fields are shown in the page by checking the text.
- Cache the information and add it to the correspoding list mapped by the field text.
- Afterwards, add "NA" to the lists of fields which are not shown in the page.
- For those fields whcih are not our target, the program will report them as new attributes.

### 6. Data Export:
<img width="600" alt="photo" src="https://github.com/user-attachments/assets/a8ccbf2d-0329-46b9-9b3e-69a08eeddff1">

- The output_to_file method compiles the scraped data into a Pandas DataFrame and exports it to a specified CSV or Excel file.
## Terminal Output Sample



### Travel Each Page of the Repository

<img width="1047" alt="photo" src="https://github.com/user-attachments/assets/d37d68d4-80de-42a5-af38-1db893922723">

### Travel the Page of Each Item
<img width="1046" alt="photo" src="https://github.com/user-attachments/assets/0eaf4de6-6bd1-4626-af7c-67f53b3ca941">

### Capacity Check
<img width="380" alt="photo" src="https://github.com/user-attachments/assets/d30405b0-832a-4bbd-a224-579c6b1f3353">

## log file
You may also refer to the `scraper.log` file. 
<img width="1126" alt="photo" src="https://github.com/user-attachments/assets/fa731e78-56d4-4b74-8e91-97c1d3eb5a91">


- `script.log` stores all the errors when the scraper encounter a timeout while loading a page.
## Result 
Please refer to the `Result.xlsx`. You may find the information of all the startups on the cyberport repository there.
  
