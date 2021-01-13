def exec():
    import time
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    test_driver = webdriver.Chrome('/Users/mukti/chromedriver')
    test_driver.get('https://discord.com/channels/790894657512538123/790897093166366741')

    time.sleep(3)

    email = 'Discord email'
    gmail = test_driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input')
    gmail.send_keys(email)


    psw = 'Discord Password'
    passs = test_driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
    passs.send_keys(psw)


    login = test_driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
    login.click()

    time.sleep(60)
    i = 0
    while i == 0:
        message = 'pls beg'
        text_box = test_driver.find_element_by_css_selector('#app-mount > div.app-1q1i1E > div > div.layers-3iHuyZ.layers-3q14ss > div > div > div > div > div.chat-3bRxxu > div > main > form > div > div > div > div > div.textArea-12jD-V.textAreaSlate-1ZzRVj.slateContainer-3Qkn2x > div.markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP > div')
        text_box.send_keys(message)
        test_driver.find_element_by_css_selector("#app-mount > div.app-1q1i1E > div > div.layers-3iHuyZ.layers-3q14ss > div > div > div > div > div.chat-3bRxxu > div > main > form > div > div > div > div > div.textArea-12jD-V.textAreaSlate-1ZzRVj.slateContainer-3Qkn2x > div.markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP > div").send_keys(Keys.RETURN)
        test_driver.find_element_by_css_selector("#app-mount > div.app-1q1i1E > div > div.layers-3iHuyZ.layers-3q14ss > div > div > div > div > div.chat-3bRxxu > div > main > form > div > div > div > div > div.textArea-12jD-V.textAreaSlate-1ZzRVj.slateContainer-3Qkn2x > div.markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP > div").send_keys(Keys.RETURN)
        time.sleep(46)
