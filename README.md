# MP-Website-Scrape-Semantics-Scanner: I BASIC Solution


CHALLENGE: Create a tool that uses the information acquired from scraping MP websites and allows campaigners to search for phrases or words. Though crude, this might allow campaigners to search for “IPP sentences” and immediately see those MPs who have mentioned that issue on their websites, for example.


DISCLAIMER: The Application code scrpt and tool is intended to facilitate research, by authorised and approved parties, pursuant to the ideals of libertarian democracy in the UK, by Campaign Lab membership. Content subject-matter and results can be deemed sensitive and thus confidential. Therefore illicit and authorisation for any other use, outside these terms, is hereby not implied pursuant to requisite UK Data Protection legislation and the wider GDPR enactments within the EU.


I BASIC Solution:


The applications Code script written in Python, is UNIX/LINUX & MacOS formatted and can be executed from the terminal CLI thus; [USER]$ chmod u+x ukmpprofile_json.py [ENTER], on any local computing environment with sufficient computing resource. This would generate the requisite 'ukmpprofile.json' file necessary, to be uploaded (or pasted) onto an Open Document Format compliant data Application document (like a 'Spreadsheet'), for manual manipulation at a basic level. Please refer to alternatives provided on the Microsoft WINDOWS Platform, for use on it's POWERSHELL terminal CLI, etc, in order to appropriately execute the Python Application code on that platform. Internet access is mandatory.


ADDITIONAL APPLICATION SCRIPT CODE NOTES:


The Python Applications script uses the `requests`, `BeautifulSoup`, and `re` libraries to scrape the specified URLs, extract the required information, and store the results in a JSON file.

### Explanation:

1. **Libraries**:
   - `requests`: To fetch HTML content from the URLs.
   - `BeautifulSoup`: To parse and extract data from the HTML.
   - `re`: To use Regular Expressions for identifying policy interests, statements, and specific phrases.

2. **Functions**:
   - `scrape_theyworkforyou()`: Extracts MP names and links from "They Work For You".
   - `scrape_parliament_uk()`: Extracts constituency names and links from the Parliament website.
   - `extract_policy_interests(mp_pages)`: Visits each MP's page to extract text content and search for specific patterns.

3. **Regex Patterns**:
   - Identifies keywords such as "policy interests", "statements", and specific phrases like "IPP sentences".

4. **Output**:
   - Combines and processes data into a structured JSON file: `ukmpprofile.json`.

### Requirements:
- Install dependencies: `pip install requests beautifulsoup4`.
- Ensure internet access to fetch data.


