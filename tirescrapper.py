from selenium import webdriver

driver = webdriver.Chrome("/Users/josh/Documents/chromedriver")
driver.get("http://www.bridgestonetire.com/catalog")
tires = driver.find_elements_by_class_name("tire")

for tire in tires:
	sub_brand = tire.find_element_by_css_selector(".tire-heading__subbrand").text
	model_name = tire.find_element_by_xpath(".//span[@class='tire-heading__model']").text
	price = tire.find_element_by_xpath(".//span[@class='tire-price__dollar']").text
	print(model_name)
	print("Price: " + price)
	print("---------------")

