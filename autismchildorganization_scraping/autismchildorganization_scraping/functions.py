#For Getting Random String
from django.utils.crypto import get_random_string

# Used for Timezone / Datetime
from django.utils import timezone
from datetime import datetime
from datetime import datetime, date, timedelta

from urllib.parse import urlparse
from bs4 import BeautifulSoup

import string
import random
import constants
import datetime
import os
import re
import time
import requests


#Used for  Path (File Handling, Folders)
from pathlib import Path

def current_date():

    current_date=date.today()
    return current_date

def current_date_time():

    current_date_time=format(datetime.datetime.now(),constants.datetime_format)
    return current_date_time

def display_date_time(date_text):
    req_format = constants.datetime_format

    dt=format(date_text,req_format)
    return dt


def find_str(full, sub):
    index = 0
    sub_index = 0
    position = -1
    for ch_i,ch_f in enumerate(full) :
        if ch_f.lower() != sub[sub_index].lower():
            position = -1
            sub_index = 0
        if ch_f.lower() == sub[sub_index].lower():
            if sub_index == 0 :
                position = ch_i

            if (len(sub) - 1) <= sub_index :
                break
            else:
                sub_index += 1

    return position

#=========================================== Error Logs ===========================================
BASE_DIR=BASE_DIR = Path(__file__).resolve().parent
log_dir_path=os.path.join(BASE_DIR,'log/error_logs')

def write_log_file(sel_text):
    log_file_name=str(current_date()) + '.log'
    log_file_path=os.path.join(log_dir_path,log_file_name)
    sel_file = log_file_path

    if sel_file is not None:
        

        file=open(sel_file,"a+")
       
            
        if sel_text is not None:
            file.write('\n')
            file.write(sel_text)
            file.close()
    return True
#=========================================== Error Logs ===========================================

def get_website_url(sel_url):
    if sel_url is not None:
        website_url=""
        try:
            website_response = requests.get(sel_url,timeout=10)
            if website_response.status_code==200:
                time.sleep(15)
                website_url_parse=urlparse(website_response.url).scheme+"://"+urlparse(website_response.url).netloc
                website_url_parse_response=requests.get(website_url_parse)
                if website_url_parse_response.status_code==200: 
                    website_url=website_url_parse_response.url[:-1] if website_url_parse_response.url[-1] == '/' else website_url_parse_response.url
                else:
                    website_url=""
            else:
                website_url=""
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            website_url=""
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            website_url=""
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            website_url=""
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt) 
            website_url=""
    else:
        website_url=""
    return website_url

def get_scrape_urls(sel_website):
    if sel_website is not None:
        scrape_urls = {}
        required_pages=["about","contact"]
        required_pages.append(sel_website)
        
        # scrape_urls.append(sel_website)
        try:
            sel_website_reqs = requests.get(sel_website,timeout=10)
            if sel_website_reqs.status_code==200:
                time.sleep(15)
                soup = BeautifulSoup(sel_website_reqs.text, 'html.parser')
                for link in soup.find_all('a'):
                    inside_link=str(link.get('href'))

                    if sel_website in str(link.get('href')).lower():
                        if sel_website not in scrape_urls:
                            scrape_urls[sel_website]=sel_website
                        if 'about' in str(link.get('href')).lower():
                            print(str(link.get('href')))
                            if str(link.get('href')).lower() not in scrape_urls:
                                scrape_urls[str(link.get('href')).lower()]=str(link.get('href')).lower()
                        if 'contact' in str(link.get('href')).lower():
                            print(str(link.get('href')))
                            if str(link.get('href')).lower() not in scrape_urls:
                                scrape_urls[str(link.get('href')).lower()]=str(link.get('href')).lower()
                        


                    
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            scrape_urls = {}
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            scrape_urls = {}
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)     
            scrape_urls = {}
        
            

    else:
        scrape_urls = {}
    return scrape_urls

def get_email_address_from_urls(sel_urls):
    if sel_urls is not None:
        emails={}
        email_address=""
        # test_urls=[]
        # test_urls.append("https://www.northpark-dental.com/")
        # Create email id regular expression
        email_regex = re.compile(r'''(
                                [a-zA-Z0-9._%+-]+
                                @
                                [a-zA-Z0-9.-]+
                                (\.[a-zA-Z]{2,4}))''', re.VERBOSE)
        if len(sel_urls)>=1:

            for url in sel_urls:
                print("Crawling URL %s" % url)
                try:
                    page_data = requests.get(url)
                    time.sleep(10)
                except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                    continue

                url_domain=urlparse(page_data.url).netloc.replace("www.", "")
                domain_check = ["gmail","hotmail","outlook","yahoo"]
                domain_check.append(url_domain)

                # Convert byte data to a string
                page_html = str(page_data.content) 
                for groups in email_regex.findall(page_html):
                    contact_email=str(groups[0]).lower()
                    for i in domain_check:
                        if i in contact_email:
                            if contact_email not in email_address:
                                emails[contact_email]=str(contact_email).strip()
                        # else:
                        #     if contact_email not in email_address:
                        #         emails[contact_email]=str(contact_email).strip()
                        #     break
                            
                            

            if len(emails)>=1:
                emails=list(emails.keys())
                email_address=",".join(emails)
            else:
                email_address=""
        else:
            email_address=""
    else:
        email_address=""
    
    return email_address