import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import pandas as pd
import os

class Startup():

    def __init__(self, name = "", year = "", website = "", sector = ""):



        self.name = name
        self.year = year
        self.website = website
        self.sector = sector
        pass


class StartupRepo():

    def __init__(self, url:str):
        options = webdriver.ChromeOptions()
        # options.add_argument('--start-maximized')  # Open browser in maximized mode
        options.add_argument('--disable-extensions')  # Disable extensions
        self.driver = webdriver.Chrome(options= options)

        # Data from scraping the database
        self.url = url
        self.pages = []
        
        ## Startup Information
        # Contest Details
        self.contest_years = []
        self.awards = []

        # Company Details 
        self.names = []
        self.intake_months = []
        self.intake_years = []
        self.websites = []
        self.status = []

        # Business Details
        self.sectors=[]

        # Mapping the target columns 
        self.table = {
            "contest-year" : self.contest_years,
            "Award" : self.awards,
            "Intake Month" : self.intake_months,
            "Intake Year" : self.intake_years,
            "Website": self.websites,
            "Cyberport Community Status":self.status ,
            "Technology Sector": self.sectors
            
        }
        
        
    def capacity_check(self) -> int:
        """
        Checks the capacity of the object by verifying that the lengths of all columns in 'table' match 
        the number of elements in 'names'. Also prints the capacity check details.

        Returns:
        int: Returns 1 if all columns have the same length as 'names', otherwise returns 0.
        """

        def capitalize_words(s):
            words = s.split()
            capitalized_words = [word.capitalize() for word in words]
            return ' '.join(capitalized_words)
        
        print("### Capacity Check ###")
        tmp = len(self.names)
        print("Company Names: "+ str(tmp))
        for name, col in self.table.items():

            name = capitalize_words(name)

            print(name +": "+ str(len(col)))
            if tmp != len(col):
                return 0
            
        return 1
    
    def capacity(self) -> int:
        """
        Returns the capacity of the object, defined as the number of elements in the 'names' attribute.

        Returns:
        int: The number of elements in the 'names' list.
        """
        # self.capacity_check()
        return len(self.names)

    def info(self) -> None:
        """
        Prints the existing information stored in the 'table' attribute.
        """
        print("### Existing Information ###")
        print("Company Names: ")
        print(self.names)
        for col, data in self.table.items():
            print(col+ ": ")
            print(data)

        
        
    def search(self, page_number: int ) -> None:
        """
        Searches through a specified number of pages on a website, extracting company names and URLs.

        Parameters:
        page_number (int): The number of pages to search through.

        This method appends product names to the 'names' list and product URLs to the 'pages' list.
        """
        
        try:
            for i in range(1,page_number+1):

                # Visit each page of the database
          
                url = self.url + str(i)
                self.driver.get(url)          
                self.driver.implicitly_wait(2)                
                
                # current_url = self.driver.current_url
                # if '#' in current_url:
                #     self.driver.execute_script(f"window.location.href = '{url}'")
            
                ## Find Names
                elements = self.driver.find_elements(By.CLASS_NAME, "product-item-link")
                for elem in elements:
                    self.names.append(elem.text)

                ## Find URLs 
                elements = self.driver.find_elements(By.CLASS_NAME, "product-item-actions")

                # Loop through each element and get its inner HTML content
                for elem in elements:
                    target = elem.find_element(By.CSS_SELECTOR, 'a')
                    self.pages.append(target.get_attribute("href"))

                self.driver.implicitly_wait(2)
                self.driver.get("https://www.google.com/")
        
        # Quit the web driver eventhough an error occurs
        finally:
            # self.driver.quit()
            pass



    def  travel_each_page(self) -> None :
        """
        Visits each page in the 'pages' list, scrapes data based on specified CSS selectors, and 
        updates the 'table' dictionary with the scraped data.
        """

        date_pattern = r'^\d{4}$|^\d{4}-\d{2}$|^\d{4}-\d{2}-\d{2}$'

        for i in range(self.capacity()):
            print("Company Name: "+ self.names[i]+ " | Item No. "+ str(i+1))
            url = self.pages[i]
            self.driver.get(url)

            # Find out the list of parent div
            elements = self.driver.find_elements(By.CSS_SELECTOR, "div.row.field-entry")

            for element in elements:

                # Reach to the label and value div
                label_div =  element.find_element(By.CSS_SELECTOR, "div.field-label.col-md-4")
                value_div = element.find_element(By.CSS_SELECTOR, "div.field-value.col-md-8")

                # If the label is stored in our table, append the value to the corresponding list
                if label_div.text in self.table:
                    self.table[label_div.text].append(value_div.text)
                    print("Cached ", label_div.text, value_div.text)
                
                # Otherwise, tell there is a new column
                else :
                    print("New attribute found: ", label_div.text, value_div.text)

            # print(list(self.table.values()))

            # If some columns dont show in a page, add "NA" on the corresponding list.
            for col in list(self.table.values()):
                
                if col is not self.pages and len(col) != i + 1:
                    col.append("NA")

            print("Done")

        

    def output_to_file(self, arrays: list[list], column_names: list[str], filename: str) -> None:
        """
        Exports data to a CSV or Excel file.

        Parameters:
        arrays (List[List]): A list of lists, where each inner list contains column data.
        column_names (List[str]): A list of strings representing the column names.
        filename (str): The name of the file to save the data to. Should end with .csv or .xlsx.

        Raises:
        ValueError: If the number of arrays does not match the number of column names.
        ValueError: If the file format is not supported.
        """

        if len(arrays) != len(column_names):
            raise ValueError("The number of arrays and the number of column names must be the same")

        data = {column_names[i]: arrays[i] for i in range(len(arrays))}
        df = pd.DataFrame(data)
        
        # Find out the directory path of the current file
        directory = os.path.dirname(os.path.abspath(__file__))

        
        # See if the target file type is xlsx or csv
        if filename.endswith('.csv'):
            df.to_csv(directory + "/"+filename, index=False)
        elif filename.endswith('.xlsx'):
            df.to_excel(directory+ "/"+ filename, index=False)
        else:
            raise ValueError("Unsupported file format. Use either .csv or .xlsx")
        

    def run(self) -> None :
        """
        Runs the whole web scraping process.
        """
        self.search(page_number= 2)
        self.travel_each_page()
        self.driver.close()
        self.info()
        target_column_names =  ["Intake Year", "Intake Month", "Cyberport Community Status", "Technology Sector","Website" ]
        self.output_to_file([self.names] + [self.table[col]for col in target_column_names], ["Company Names"] + target_column_names,"Result.xlsx" )
        
        if self.capacity_check():
            print("The totoal number of records is " + str(self.capacity()) +" .")
            print("Web-scraping runs Successfully! ")
   
        else:
            raise ValueError("Error. The number of records in each column is not the same.")
            
        

if __name__ == '__main__':

    url = "https://istartup.hk/en/startups/profile#sort=name&sortdir=asc&page="
    SR = StartupRepo(url = url)
    SR.run()





