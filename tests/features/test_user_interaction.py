from selenium .webdriver import Chrome

path="c:\\celinekaslin\\Downloads\\chromedriver_mac64.zip\\chromedriver"
driver = Chrome(executable_path=path)
driver.get("http://localhost:5000/introduction")

driver.maximise_window()
