#!/usr/bin/env python3

# DISCLAIMER: DISCLAIMER: The Application code scrpt and tool is intended to facilitate research, by authorised and approved parties, pursuant to the ideals of libertarian democracy in the UK, by Campaign Lab membership. Content subject-matter and results can be deemed sensitive and thus confidential. Therefore illicit and authorisation for any other use, outside these terms, is hereby not implied pursuant to requisite UK Data Protection legislation and the wider GDPR enactments within the EU.

# CODE REVISION: Ejimofor Nwoye, Newspeak House, London, England, @ 22/01/2025

# SCRIPT LIBRARIES:

import requests # To fetch HTML content from the URLs.
from bs4 import BeautifulSoup # To parse and extract data from the HTML.
import re # To use Regular Expressions for identifying policy interests, statements, and specific phrases.
import json # JSON Manipulation library.
import os # Operating System calls.

os.system("clear") 


# FUNCTIONS:

def scrape_theyworkforyou(): # To use Regular Expressions for identifying policy interests, statements, and specific phrases.
    url = "https://www.theyworkforyou.com/mps/"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    mp_data = []
    for mp in soup.select(".mp_list li a"):
        name = mp.text.strip()
        link = mp['href']
        mp_data.append({"name": name, "link": f"https://www.theyworkforyou.com{link}"})

    return mp_data

def scrape_parliament_uk(): # Extracts constituency names and links from the Parliament website.
    url = "https://members.parliament.uk/constituencies"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    constituency_data = []
    for constituency in soup.select(".card-title a"):
        name = constituency.text.strip()
        link = constituency['href']
        constituency_data.append({"constituency": name, "link": f"https://members.parliament.uk{link}"})

    return constituency_data

def extract_policy_interests(mp_pages): # Visits each MP's page to extract text content and search for specific patterns.
    policy_data = []

    for mp in mp_pages:
        try:
            response = requests.get(mp['link'])
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract text content from the MP's page
            text_content = soup.get_text(" ", strip=True)

            # Define regex patterns for policy interests and statements
            patterns = {
                "policy_interests": re.compile(r'policy interests:.*?(\w[\w\s,]*)', re.IGNORECASE),
                "statements": re.compile(r'statement:.*?(\w[\w\s,]*)', re.IGNORECASE),
                "phrases": re.compile(r'\b(IPP sentences|political views|standpoint)\b', re.IGNORECASE),
            }

            extracted_data = {"name": mp['name'], "link": mp['link']}
            for key, pattern in patterns.items():
                matches = pattern.findall(text_content)
                extracted_data[key] = matches

            policy_data.append(extracted_data)
        except Exception as e:
            print(f"Error processing {mp['name']}: {e}")

    return policy_data

def main():
    # Scrape data from the two websites
    theyworkforyou_data = scrape_theyworkforyou()
    parliament_uk_data = scrape_parliament_uk()

    # Combine MP data
    combined_data = theyworkforyou_data + parliament_uk_data

    # Extract policy interests, statements, and phrases
    policy_profiles = extract_policy_interests(combined_data)

    # Save results to a JSON file
    with open("ukmpprofile.json", "w", encoding="utf-8") as f:
        json.dump(policy_profiles, f, ensure_ascii=False, indent=4)

    print("Data successfully saved to ukmpprofile.json")

if __name__ == "__main__":
    main()

