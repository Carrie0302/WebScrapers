# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:47:28 2018
Test if IFLA still up and running
@author: carrie
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import datetime, os, re
from pyvirtualdisplay import Display

from Email import SendEmail


class IFLA_Test:
        '''This will call the IFLA website'''
        #Todays Date
        now = datetime.datetime.now()
        formatTime = now.strftime("%Y-%m-%d %H:%M")
        formatDate = now.strftime("%Y-%m-%d")
        formatHourMin = now.strftime("%H:%M")
        
        def callBrowser(self):
            ubuntu = False
            browser = ""
            if ubuntu:
                display = Display(visible=0, size=(1000, 1000))  
                display.start()
                
                path_to_chromedriver = "/usr/bin/chromedriver"
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--no-sandbox')
                browser = webdriver.Chrome(path_to_chromedriver, chrome_options=chrome_options)
            
            else:
                #If windows use the following
                path_to_chromedriver = r"C:\CMain\WebScrape_AutoTests\chromedriver_win32_233\chromedriver.exe"
                browser = webdriver.Chrome(executable_path = path_to_chromedriver )
            print("Browser")
            return browser
            
            
        def callIflaSite(self):
            #Open Intial Website with Selenium and Chrome
            browserSite = self.callBrowser()
            url = 'https://librarymap.ifla.org'
            browserSite.get(url)
            browser.find_element_by_xpath('//*[@name="ctl00$ContentPlaceHolder1$cboPageSize"]/option[contains(text(), "All")]').click()
            

           hyperlinks = browser.find_elements_by_css_selector("div.boxinside a")
           techResults = self.find_intial_links(hyperlinks)



if __name__ == '__main__':
    #EMAIL
    email_enabled = True
    linux = False
    emails = SendEmail()
    
    test = IFLA_Test()
    date = test.formatDate
    
    
    try:
        messnwithyou = 9/0
        
    except:
        print("Test on IFLA Website Unsuccesfull.")
        log = open("Error_Data.txt","a")
        log.write("Test on IFLA LIVE Website was Unsuccessull. Date: " + date + "\n")
        
        try:
            #Email if not successful
            subject = "IFLA Auto Testing, Web Scrapers Show Error on Website"
            body_text = "The LIVE ifla website seems to throw an error. The script running the test found an error on the site. Date: " + date + "\n"
            body_html = "<p>The LIVE ifla website seems to throw an error. The script running the test found an error on the site. Date: " + date + "\n</p>"    

            if linux:
                emails.send_email_linux( subject, body_text, body_html)
            else:
                emails.send_email( subject, body_text, body_html)
            print("Emailed unsuccessfull attempt alert")
        
        except:
            log = open("Error_Data.txt","a")
            log.write("Can not Email Alerts about unsuccesful test attempts. Location:IFLA_Test.py  Date: " + date + "\n")

            print("Can not email alert")
            
    
    