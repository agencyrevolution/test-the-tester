# Author: Minh Nguyen
# Created Date: Aug 29, 2018
# Description: To store all elements' locators on Home/Accounts screen

Accounts_button_with_account = '//header[text()="<account>"]/following-sibling::div//span[text()="<button>"]'
Accounts_show_more = '//div[@class="remaining-link"]'
Accounts_link_text = '//div[text()="<text>"]'

Accounts_Upcoming_Renewals_Filter_title = '//h3[text()="Accounts with upcoming renewals"]'
Accounts_Upcoming_Renewals_Filter_days = '//*[text()="Accounts with upcoming renewals"]/following-sibling::div[1]//span[3]'
Accounts_Upcoming_Renewals_Filter_carrier = ''
Accounts_Upcoming_Renewals_Filter_policies = ''
Accounts_Upcoming_Renewals_days = '//input[@type="number"]'


Accounts_send = '//button[contains(., "SEND")]'
Accounts_Send_send_one_email = '//div[text()="Send one email"]/following-sibling::div//button'

Accounts_Message_name = '//div[contains(@class, "naming")]//input'
Accounts_Message_Naming_continue = '//div[contains(@class, "naming")]//button[.="Continue"]'
Accounts_Message_Filter_Audience_continue = '//div[contains(@class, "filter-audience")]//button[.="Continue"]'
Accounts_Message_Preview_continue = '//div[contains(@class, "preview")]//button[.="Continue"]'

Accounts_Message_Library_button_with_card_name = '//div[contains(@class,"card")][contains(., "<card_name>")]//span[text()="<button_name>"]'
