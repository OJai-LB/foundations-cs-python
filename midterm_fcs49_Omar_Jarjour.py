import random
#the requests thingy learned from various youtube videos, download the libary via cmd pip requests install
import requests
#reference: https://stackoverflow.com/questions/66653796/save-json-file-to-specific-folder-with-python
import json


#1 Learned this method when doing assignment_03 using an ai tool
error_messages = [
    "You had one job, choose a number from 1 to 9!!",
    "Invalid choice. Please choose a number between 1 and 9.",
    "Try again. Pick a number from 1 to 9."
]

#ChoiceMenu
def InputChoiceVerifier():
    input_choice = input("Enter a choice number: ")
    if input_choice.isdigit() and 1 <= int(input_choice) <= 9:
        return int(input_choice)
    else:
        #1.1
        print(random.choice(error_messages))
        return InputChoiceVerifier()





#CH1

def Choice1Prompt():
    title = input("Website Title: ")
    url = UrlVerifier()
    return OpenTabChoice1(title, url)
#CH1

def OpenTabChoice1(title, url):
    #last opened tab used in many other functions, it is the last opened tab
    chrome_window.append({title: url})
    print("Tab Opened Successfully!")
    global last_opened_tab_index
    #.index method learnt from Corsera(Python3(UniversityOfMichigan))
    last_opened_tab_index = chrome_window.index({title: url})

#CH1
def UrlVerifier():
    url_string_input = input("Website URL: ")
    #reference of try except and the exception thingy: https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
    #but edited it abit
    try:
        response = requests.get(url_string_input)
        if 200 <= response.status_code < 300:
            return url_string_input
        else:
            print("The URL provided isn't valid,\n\t Try again.. ")
            return UrlVerifier()
    except requests.RequestException as e:
        print(f"Error accessing the URL: {e} \n\t Try again.. ")
        return UrlVerifier()







#CH2,3
def IndexVerifier():
    for tab_index in range(1, len(chrome_window) + 1):
        print(f"{tab_index - 1}:{chrome_window[tab_index - 1]}")
    input_index = input("Choose Index: ")
    if input_index.isdigit() and 0 <= int(input_index) <= (len(chrome_window)-1):
        return int(input_index)
    elif input_index == "":
        return last_opened_tab_index
    else:
        print("Invalid Index \n\t Try again..\n Choose Index:")
        return IndexVerifier()

#CH2
def Choice2Prompt():
    if len(chrome_window) == 0:
        print("The window has no tabs opened.")
        return
    index = IndexVerifier()
    return CloseTabChoice2(index)

#CH2
def CloseTabChoice2(index):
    #index -1 since the index of the choice2prompt is of range len(chrome_window + 1)
    #del/close the tab of the window
    del chrome_window[index]
    print(f"Tab {index} closed.")






#CH3
def Choice3Prompt():
    index = IndexVerifier()
    return SwitchTabChoice3(index)
#CH3
def SwitchTabChoice3(index):
    #getting the url of the tab, from the dict of index
    url = list(chrome_window[index].values())[0]
    response = requests.get(url)
    html = response.text
    print(html)







#CH4
def PrintTitlesChoice4():
    if len(chrome_window) == 0:
        print("No open tabs are available")
    for tab in chrome_window:
        if len(tab) == 1:
            print(list(tab.keys())[0])
        else:
            #technically speaking, the parent tab is the shortest one since the url is the base url
            #sorted method and lambda learned from Corsera Python3 course
            sorted_nested_list = (sorted(tab.items(), key=lambda item: item[1]))
            #prints the parent that has the smallest url
            print(sorted_nested_list[0][0])
            #prints the other tabs accordingly
            for nested in sorted_nested_list[1:]:
                print(f"\t{nested[0]}")







#Ch5
def Choice5Prompt():
    index = IndexVerifier()
    return NestTabChoice5(index)

#CH5
def NestTabChoice5(index):
    title = input("Nested Website title:")
    while True:
        if title in chrome_window[index]:
            print("The title already exists! \n\t Modify and Try again..")
            title = input("Nested Website title:")
        else:
            break
    url = UrlVerifier()
    while True:
        for nested_tab in chrome_window[index]:
            if chrome_window[index][nested_tab] == url:
                print("The URL entered is already added to a tab \n\t Modify and Try again..")
                url = UrlVerifier()
        break

    OpenNestedTabChoice5(index, title, url)

#CH5
#opens a new tab that is nested
def OpenNestedTabChoice5(index, title, url):
    #last opened tab used in many other functions, it is the last opened tab
    chrome_window[index].update({title: url})
    print("Tab Opened Successfully!")
    global last_opened_tab_index
    last_opened_tab_index = index









#CH6
def ClearTabsChoice6():
    if len(chrome_window) == 0:
        print("Tabs already cleared.")
        return
    chrome_window.clear()
    print("All tabs are cleared off the window!")







#CH7
#reference: https://stackoverflow.com/questions/66653796/save-json-file-to-specific-folder-with-python
def StoreInFileChoice7():
    directory = input("Enter the file path: ")
    with open(directory, "w+") as f:
        json.dump(chrome_window, f)
    print("Window of tabs stored successfully!!")





def LoadFromFileChoice8():
    directory = input("Enter the file path: ")
    with open(directory, "w+") as f:
        json.load(chrome_window, f)









def ChoiceMenu():
    print("""
    Greetings!!
    
    1. Open Tab
    2. Close Tab
    3. Switch Tab
    4. Display All Tabs
    5. Open Nested Tabs
    6. Clear All Tabs
    7. Save Tabs
    8. Import Tabs
    9. Exit    
    
    """)
    while True:
        input_choice = InputChoiceVerifier()
        #loops until returning or breaking, learned using ai tool doing assignments

        if input_choice == 9:
            break
        elif input_choice == 1:
            Choice1Prompt()
        elif input_choice == 2:
            Choice2Prompt()
        elif input_choice == 3:
            Choice3Prompt()
        elif input_choice == 4:
            PrintTitlesChoice4()
        elif input_choice == 5:
            Choice5Prompt()
        elif input_choice == 6:
            ClearTabsChoice6()
        elif input_choice == 7:
            StoreInFileChoice7()
        elif input_choice == 8:
            LoadFromFileChoice8()



#global variable to be used in and outside the functions.
#global and local knowlege from Corsera(Python3(UniversityOfMichigan))
last_opened_tab_index = None
#predefinded set of tabs
chrome_window = []

ChoiceMenu()




