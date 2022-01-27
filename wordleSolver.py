from selenium import webdriver
import json


driver = webdriver.Firefox() 

url='https://www.powerlanguage.co.uk/wordle/'

driver.get(url)

script="return localStorage;"

result = driver.execute_script(script)

solution = json.loads(result["gameState"])

print(solution["solution"])
