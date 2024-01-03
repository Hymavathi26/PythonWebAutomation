from selenium import webdriver
#chrome - Chrome Options
#firefox - Firefox options
#Edge - Ede options


def test_open_login():
    chrome_options = webdriver.ChromeOptions()
    #give some extra arguments or extentions or anything to chrome
    #chrome options - Chrome with extentions, window size, proxy,JS disable

    extension_path = "Downloads/addblockerfile.crx"  #path for the file
    chrome_options.add_extension(extension_path)

    chrome_options.add_argument("--start-maximized)

    driver=webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/")
    driver.maximize_window()
    print(driver.title)