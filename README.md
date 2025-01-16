# Autism Child Organization in Pakistan Web Scraping Project

## Project Overview
This project is designed to scrape information about organizations in Pakistan that provide support and services for children with autism. The data collected will be used to create a centralized and accessible resource to help families and caregivers.

## Features
- Scrape organization names, contact information, services provided, and location details.
- Store the scraped data in a structured format (e.g., CSV, JSON, or database).
- Option to filter organizations based on specific services or regions.
- Error handling to ensure robust and reliable scraping.

## Tech Stack
- **Programming Language**: Python
- **Libraries/Frameworks**:
  - Selenium: For dynamic content scraping and browser automation.
  - Scrapy: For efficient web crawling and scraping.
  - Beautiful Soup: For HTML parsing.
  - Requests: To fetch web pages.
  - Pandas: For data manipulation and storage.
  - SQLite: For database storage (optional).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/atifusmanhashim/autismchildorganization_scraping.git
   cd autism-org-scraping
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Update the `config.json` file with the necessary URLs and scraping parameters.
2. Choose the desired scraping method:
   - For dynamic content using Selenium, update and run `selenium_scraper.py`:
     ```bash
     python selenium_scraper.py
     ```
   - For efficient crawling using Scrapy, navigate to the Scrapy project directory and run:
     ```bash
     scrapy crawl autism_org
     ```
3. The output data will be saved in the `output/` directory as a CSV file or in the configured database.

## Project Structure
```
.
|-- config.json          # Configuration file for URLs and parameters
|-- selenium_scraper.py  # Selenium-based scraping script
|-- scrapy_project/      # Scrapy project directory
|-- requirements.txt     # List of dependencies
|-- output/              # Directory for scraped data
|-- README.md            # Project documentation
```

## Contribution Guidelines
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a feature description"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
Special thanks to organizations and volunteers who provide support to children with autism and their families in Pakistan.
