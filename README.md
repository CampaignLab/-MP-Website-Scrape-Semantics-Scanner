# -MP-Website-Scrape-Semantics-Scanner
CHALLENGE: Create a tool that uses the information acquired from scraping MP websites and allows campaigners to search for phrases or words. Though crude, this might allow campaigners to search for “IPP sentences” and immediately see those MPs who have mentioned that issue on their websites, for example.

I BASIC Solution:

DISCLAIMER: The Application code & tool is intended to facilitate research, by approved parties, pursuant to the ideals of libertarian democracy in the UK, by Campaign Lab membership. Content subject-matter and result can be deemed sensitive and thus confidential. Therefore authorisation for any other use, outside these terms, is hereby not implied pursuant to requisite UK Data Protection legislation.

The Applications Code block written in Python, is UNIX/LINUX & MacOS formatted and can be executed thus; [user]$ chmod u+x ukmpprofile_json.py [enter], on any local computing environment with sufficient computing resource. This would generate the requisite 'ukmpprofile.json' file necessary, to be uploaded (or pasted) onto an Open  Document compliant data sheet, for manual manipulation at a basic level. Please refer to alternatives provided on the Microsoft WINDOWS Platform, for use on it's POWERSHELL scripting tool, etc, in order to appropriately execute the Python Application code.

ADDITIONAL COMMENTRY SCRIPT CODE NOTES:

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


