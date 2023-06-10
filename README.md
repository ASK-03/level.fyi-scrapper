# Level.fyi Scraper

Level.fyi Scraper is a command-line tool built with Python that enables user to scrape salary data from the popular website [Levels.fyi](https://www.levels.fyi/?compare=Accenture,Tata%20Consultancy%20Services,Infosys&track=Software%20Engineer#). It provides users with accurate insights and services to compare salaries and make informed career decisions.

## Purpose

The purpose of this tool is to empower professionals by providing them with the most up-to-date and reliable salary information available on Levels.fyi. By scraping the website, Level.fyi Scraper collects comprehensive salary data currently for freshers joining in India. Users can leverage this data to gain a better understanding of salary ranges, negotiate job offers, and make informed career choices.

## Features

- **Salary Scraping**: Level.fyi Scraper fetches salary data from Levels.fyi, ensuring that users have access to accurate and current information.
- **Company-Specific Data**: Users can input the name of the company they are interested in to retrieve the median salary for freshers with 0 years of experience in India specifically for that company.
- **Command-Line Interface (CLI)**: The CLI enables users to interact with Level.fyi Scraper efficiently by simply providing the name of the company they want salary data for.
- **Data Export**: Users have the option to save the scraped salary data to a file using the `--save` option. The data can be exported in JSON format. for further analysis or integration with other tools.

## Dependencies
- **Python3**: Ensure that you have Python 3 installed on your system. You can download and install Python 3 from the official Python website: https://www.python.org.
- **pip**: pip is the package installer for Python. It is usually installed by default when you install Python. However, make sure you have pip installed and it is up to date. You can check the version of pip by running the following command:
```
pip --version
```
- **Selenium**: You can install it using pip by running the following command
  ```
  pip install selenium
  ```
- **Chromium Drivers**: Make sure you have the appropriate Chromium drivers installed and configured. These drivers are required for Selenium to interact with the Chromium browser. Refer to the Selenium documentation for instructions on installing and setting up Chromium drivers based on your operating system.

## Installation
To install and use Level.fyi scraper, follow the steps given below:
- Fork the Level.fyi Scraper repository by clicking the "Fork" button at the top right corner of the repository page. This will create a copy of the repository under your GitHub account.
- Clone the forked repository to your local machine:
```
git clone https://github.com/{YOUR-USERNAME}/level.fyi-scrapper.git
```
- Navigate to the project directory:
```
cd level.fyi-scraper
```
- Install the necessary Python packages by running the following command:
```
pip install -r requirements.txt
```
## How to use?
To use Level.fyi Scraper, follow these steps:
- Make sure you have completed the installation steps mentioned above.
- Open a terminal or command prompt and navigate to the project directory.
- Run the scraper by executing the following command:
```
python3 scrapper.py
```
The above command will run the scraper with default settings with company name as amazon and printing the ouput in the terminal.
However, user can input the company name and output saving preference in the above command itself.
```
python3 scrapper.py --company google --save True
```
The above command will scrape the data for google and save the extracted data into a json file in the same directory as the project.

## Contributions
Contributions to Level.fyi Scraper are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

## Future Work
There are several potential enhancements and features that can be considered for Level.fyi Scraper in the future. Some of these include:
- Dynamic Installation of Chrome Webdrivers: Enhance the installation process by automatically detecting and installing the required Chrome webdrivers if they are not found in the project directory. This would simplify the setup process for users.
- Additional Salary Statistics: Expand the scraped salary information by providing additional statistics such as mean, mode, maximum salary, and minimum salary. This would give users a more comprehensive understanding of the salary distribution for the specified company and criteria.
- More Filters and Parameters: Extend the tool's functionality by incorporating more filters and parameters. For example, allow users to specify years of experience, demographics, work experience, or other relevant factors to obtain more specific and tailored salary data.
- Support for Other Fields: Currently, Level.fyi Scraper focuses on retrieving salary data for freshers with 0 years of experience in India. Future improvements could include support for scraping data for other fields available on Levels.fyi, such as different job positions, industries, or geographical locations.

## Contact Me
In case you have any queries or questions, please feel free to contact me on [mail](mailto:abhisheksinghk@iitbhilai.ac.in).

Happy Scraping!!
