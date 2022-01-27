from selenium import webdriver
import json

#for this part to work you need to have the mozzila geckodrivers downloaded which can be found on their github
#Once downloaded you need to move the file to the same folder that has the python exe 
#if on macos you need to do the following things 
'''
    control-click on the geckodriver binary but keep the mouse button/touch pad pressed...
    remove finger from control key and press on option key...
    you will see the menu change...
    then select the "open" menu item with the mouse/touchpad and it will open in the terminal.
    close the terminal and you are done. You have given macOS permission to run that binary.
    Note: this works for all binaries Catalina rejects so this works for chromedriver for Chrome as well

'''
#assings webdriver.firefox to driver. This Allows you to pick which browser you would like to use with selenium 
driver = webdriver.Firefox() 

#Urlf of wordle 
url='https://www.powerlanguage.co.uk/wordle/'

#Tells the driver to get the content of wordle
driver.get(url)

#JavaScript code that is injected into the website so that we can pull the local storage attributes that gets cached when visiting the site 
script="return localStorage;"

#calling the execute_script funtion so we can inject javascript into the website and saves output to results 
result = driver.execute_script(script)

#because of how the data is retrieved python struggles to parse throught it. We use json.loads and tells it to select the gameState key
solution = json.loads(result["gameState"])

#Now when we do print we tell it to print the output of solutions and specifictly the value of the solution key
print(solution["solution"])

