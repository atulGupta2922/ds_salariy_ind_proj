from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import sys
import os

def get_jobs(num_jobs, verbose):
    # keyword = "data science"
    # num_jobs = 5
    # verbose = True
    """Gathers jobs as a dataframe, scraped from Glassdoor"""

    # Initializing the webdriver
    options = webdriver.ChromeOptions()

    # Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    # options.add_argument('headless')

    # Change the path to where chromedriver is in your home folder.

    driver = webdriver.Chrome()
    driver.set_window_size(1120, 1000)

    url = 'https://www.glassdoor.co.in/Job/india-data-science-jobs-SRCH_IL.0,5_IN115_KO6,18.htm?minRating=2.00'
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  # If true, should be still looking for new jobs.

    #     # Let the page load. Change this number based on your internet speed.
    #     # Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(4)

    #     # Test for the "Sign Up" prompt and get rid of it.
        try:
            # driver.find_element_by_class_name("selected").click()
            driver.find_element(By.CLASS_NAME, "jobCard").click()
        except ElementClickInterceptedException as exc:
            print('Error: ', exc.msg)
            pass

        time.sleep(0.1)

        try:
            driver.find_element(
                By.CSS_SELECTOR, "div.gdUserLogin button"
            ).click()  # clicking to the X.
        except NoSuchElementException as exc:
            print('Error: ', exc.msg)
            pass

    #     # Going through each job in this page
        job_buttons = driver.find_elements(
            By.CLASS_NAME, "jobCard"
        )  # jl for Job Listing. These are the buttons we're going to click.
        for job_button in job_buttons:

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            job_button.click()  # You might
            time.sleep(1)
            collected_successfully = False
            while not collected_successfully:
                try:
                    company_name = driver.find_element(
                        By.XPATH, '//div[@data-test="employerName"]'
                    ).text
                    location = driver.find_element(
                        By.XPATH, '//div[@data-test="location"]'
                    ).text
                    job_title = driver.find_element(
                        By.XPATH, '//div[@data-test="jobTitle"]'
                    ).text
                    job_description = driver.find_element(
                        By.XPATH, '//div[@class="jobDescriptionContent desc"]'
                    ).text
                    collected_successfully = True
                except Exception as e:
                    e_type, e_object, e_traceback = sys.exc_info()
                    e_filename = os.path.split(
                        e_traceback.tb_frame.f_code.co_filename
                    )[1]
                    e_message = str(e)
                    e_line_number = e_traceback.tb_lineno
                    print(f'exception type: {e_type}')
                    print(f'exception filename: {e_filename}')
                    print(f'exception line number: {e_line_number}')
                    print(f'exception message: {e_message}')
                    time.sleep(5)
            
            # jobs.append(
            #     {
            #         "Job Title": job_title,
            #         "Job Description": job_description,
            #         "Company Name": company_name,
            #         "Location": location
            #     }
            # )
            # print(jobs)
            try:
                salary_estimate = driver.find_element(
                    By.XPATH, './/span[@data-test="detailSalary"]'
                ).text
            except NoSuchElementException:
                salary_estimate = -1  # You need to set a "not found value. It's important."

            try:
                rating = driver.find_element(By.XPATH, './/span[@data-test="detailRating"]').text
            except NoSuchElementException:
                rating = -1  # You need to set a "not found value. It's important."

            # Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Job Description: {}".format(job_description[:500]))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

    #         # Going to the Company tab...
    #         # clicking on this:
    #         # <div class="tab" data-tab-type="overview"><span>Company</span></div>
    #         try:
    #             driver.find_element(
    #                 By.XPATH, './/div[@class="tab" and @data-tab-type="overview"]'
    #             ).click()

    #             try:
    #                 # <div class="infoEntity">
    #                 #    <label>Headquarters</label>
    #                 #    <span class="value">San Francisco, CA</span>
    #                 # </div>
    #                 headquarters = driver.find_element(
    #                     By.XPATH,
    #                     './/div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*',
    #                 ).text
    #             except NoSuchElementException:
    #                 headquarters = -1

            try:
                size = driver.find_element(
                    By.XPATH,
                    './/div[@id="EmpBasicInfo"]//span[text()="Size"]//following-sibling::*',
                ).text
            except NoSuchElementException:
                size = -1

            try:
                founded = driver.find_element(
                    By.XPATH,
                    '//div[@id="EmpBasicInfo"]//span[text()="Founded"]//following-sibling::*',
                ).text
            except NoSuchElementException:
                founded = -1

            try:
                type_of_ownership = driver.find_element(
                    By.XPATH,
                    './/div[@id="EmpBasicInfo"]//span[text()="Type"]//following-sibling::*',
                ).text
            except NoSuchElementException:
                type_of_ownership = -1

            try:
                industry = driver.find_element(
                    By.XPATH,
                    './/div[@id="EmpBasicInfo"]//span[text()="Industry"]//following-sibling::*',
                ).text
            except NoSuchElementException:
                industry = -1

            try:
                sector = driver.find_element(
                    By.XPATH,
                    './/div[@id="EmpBasicInfo"]//span[text()="Sector"]//following-sibling::*',
                ).text
            except NoSuchElementException:
                sector = -1

            try:
                revenue = driver.find_element(
                    By.XPATH,
                    './/div[@id="EmpBasicInfo"]//span[text()="Revenue"]//following-sibling::*',
                ).text
            except NoSuchElementException:
                revenue = -1

            try:
                competitors = driver.find_element(
                    By.XPATH,
                    './/div[@id="EmpBasicInfo"]//span[text()="Competitors"]//following-sibling::*',
                ).text
            except NoSuchElementException:
                competitors = -1

            if verbose:
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("Competitors: {}".format(competitors))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append(
                {
                    "Job Title": job_title,
                    "Salary Estimate": salary_estimate,
                    "Job Description": job_description,
                    "Rating": rating,
                    "Company Name": company_name,
                    "Location": location,
                    "Size": size,
                    "Founded": founded,
                    "Type of ownership": type_of_ownership,
                    "Industry": industry,
                    "Sector": sector,
                    "Revenue": revenue,
                    "Competitors": competitors,
                }
            )
            # add job to jobs

        # Clicking on the "next page" button
        try:
            driver.find_element(By.XPATH, './/button[@data-test="pagination-next"]').click()
        except NoSuchElementException:
            print(
                "Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(
                    num_jobs, len(jobs)
                )
            )
            break
    return pd.DataFrame(jobs)

dataset = get_jobs(1000, False)
dataset.to_csv('glassdoor_ds_jobs.csv', index=False)
# return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.
