from selenium import webdriver
import time
import threading

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()



driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')

input('Scan your QR code and then press Enter to continue')

name = 'Mayank V2'
group_title = 'cheemsgang'

time.sleep(2)

lastMessage = None

def functionToSendMsg():

    try:
        global lastMessage
        groupEl = driver.find_element_by_xpath("//span[@class = '_1hI5g _1XH7x _1VzZY' and @title = '" + group_title +"']")
        groupEl.click()

        time.sleep(2)

        last_msg_author_list = driver.find_elements_by_css_selector('._19038._3cwQ7._1VzZY')
        if not last_msg_author_list:
            return
        last_msg_author = last_msg_author_list[-1].text
        for i in last_msg_author_list:
            print(i.text)
        # last_msg_author_unsaved = driver.find_elements_by_css_selector("._1o4HO")[-1].text
        print(last_msg_author)

        lastMessage = driver.find_element_by_css_selector('.focusable-list-item:last-child > div > div > div > div.copyable-text >  div > span > span').text
        print(lastMessage,'lastMessage')
        if (last_msg_author == name) and lastMessage != ('shatta rendi ' + name):
            try:
                driver.find_element_by_css_selector('.DuUXI').send_keys('shatta rendi ' + name)
                # driver.find_element_by_css_selector('._3qpzV').click()
                sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
                sendbutton.click()
                driver.find_element_by_css_selector('._1awRl.copyable-text.selectable-text:last-child').clear()
            except:
                    print('something went wrong')
    except:
        print('something went wrong again')

# setInterval(functionToSendMsg,0.1)

while True:
    functionToSendMsg()

# # group_mem_list = group_mem_str.split(',')

# # for member in group_mem_list:
# #     user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(member))
# #     user.click()


# # !make sure you open all contacts in group details before using this script



# driver.find_element_by_xpath("//div[@class = '_3XrHh']/span[@class = '_1wjpf _3NFp9 _3FXB1' and @title = '" + group_title +"']").click()

# time.sleep(2)

# try:
#     if driver.find_element_by_css_selector('._3Wg5_').size['width'] != 0:
#         driver.find_element_by_css_selector('._3Wg5_').click()
# except :
#     print('Group has less members')

# time.sleep(4)

# members = driver.find_elements_by_css_selector('._2EXPL._3xj48 ._1wjpf._3NFp9._3FXB1')

# group_mem_list = []

# for member in members:
#     group_mem_list.append(member.text)

# print(group_mem_list)
# group_mem_list.pop(0)


# for member in group_mem_list:
#     try:
#         driver.find_element_by_css_selector('._3F6QL._3xlwb ._2S1VP').send_keys(member)
#         time.sleep(1)
#         user = driver.find_element_by_xpath('//span[@title = "' + member + '" ]')
#         user.click()
#         driver.find_element_by_css_selector('._3F6QL._2WovP ._2S1VP').send_keys(msg)
#         sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
#         sendbutton.click()
#         driver.find_element_by_css_selector('._3F6QL._3xlwb ._2S1VP').clear()
#     except:
#         driver.find_element_by_css_selector('._3F6QL._3xlwb ._2S1VP').clear()
#         continue
    
input('Scan your QR code and then press Enter to continue')

driver.quit()