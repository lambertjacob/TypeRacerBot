#imports
from selenium import webdriver
import random
import time


def loadSite():
    
    #define url
    url = "https://play.typeracer.com"

    #open url in chrome and wait 2 seconds to load screen
    web = webdriver.Chrome()
    web.get(url)

    time.sleep(2)
    
    #login 
    login(web)

    #return the web value to be used in main function
    return web


def login(web):
    
    username = "jacobot"
    password = "Techandcoding2021"

    #have the bot sign in to the fields on the website 
    signinPage = web.find_element_by_xpath("//*[@id=\"userInfo\"]/div/div[2]/div[1]/div[2]/a[2]")
    signinPage.click()

    time.sleep(1)

    usernameInput = web.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/input")
    usernameInput.send_keys(username)

    time.sleep(.5)

    passwordInput = web.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/input")
    passwordInput.send_keys(password)

    signinButton = web.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/button")
    signinButton.click()

    time.sleep(.5)



def online():
    
    web = loadSite()

    #click button "enter typing race"
    play = web.find_element_by_xpath('//*[@id="gwt-uid-1"]/a')
    play.click()

    #allows wpm input
    speed = float(input("Enter the time between each word (roughly):\n"))

    #finds the chunk of text
    text = web.find_element_by_xpath("//*[@id=\"gwt-uid-21\"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div")
    #divided into spans so need to get each one
    parts = text.find_elements_by_tag_name('span')
    
    #number of spans varies, so account for both choices
    if len(parts) == 2:
        #include space to seperate first word from second
        wordsAll = parts[0].text+ " " + parts[1].text
    else:    
        wordsAll = parts[0].text +  parts[1].text + " " + parts[2].text

    #print(wordsAll)
    
    #make a list of the words
    words = wordsAll.split(" ")

    print(words)  
    #time.sleep(3)      
    
    #iterate through each word
    for word in words:
       
        #need a space after each word
        string = word + " "
        
        #find the input field and then type in the current word
        field = web.find_element_by_class_name('txtInput')
        field.send_keys(string)

        #to make sure that its not same time between each word like a bot would
        timechange = 1
        multiplier = random.uniform(0.01, 1)
        timechange *= multiplier

        #to monitor progress
        print("Typed = " + string + "   Timechange = " + str(timechange))

        #need to wait a bit so not detected as a robot with random addition of time 
        time.sleep(speed + timechange)

    print("Race over")
    time.sleep(100)


    
    
    
def main():
    #get the url and then start the game
    gamemode = input("How would you like to play?\n Online [1]\n")
    if gamemode == "1": online()


if __name__ == "__main__":
    main()