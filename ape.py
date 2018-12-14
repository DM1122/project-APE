import selenium
from selenium import webdriver
import time

import libs
from libs import emailib

voter_count = 3
link = 'https://janegoodall.ca/our-work/roots-and-shoots/ape-fund/vote/st-thomas-aquinas-sustainable-garden-initiative/'

driver = webdriver.Chrome('./webdrivers/chromedriver')
driver.set_page_load_timeout(10)
driver.set_window_size(800, 800)
driver.set_window_position(1200, 200)

print('Initiating APE')
driver.get(link)        # navigate to url
driver.find_element_by_id('open-voting').click()        # hit vote icon
time.sleep(1)

for i in range(1, voter_count+1):
    email = emailib.generate_address()
    print('#############################################')
    print('{} joins the battle! ({}/{})'.format(email, i, voter_count))

    driver.find_element_by_id('input_4_3').send_keys(email)     # type email
    time.sleep(1)
    driver.find_element_by_id('gform_submit_button_4').click()      # hit 'vote' button
    time.sleep(1)


    for j in range(1, 13):
        print('{} is voting... ({}/12)'.format(email, j))
        driver.refresh()
        time.sleep(1)

    driver.find_element_by_id('input_4_3').clear()
    time.sleep(1)

vote_count = voter_count * 12
print('Success! total votes gained:', vote_count)