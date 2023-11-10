import random
#1 Learned this method when doing assignment_03 using an ai tool
error_messages = [
    "You had one job, choose a number from 1 to 9!!",
    "Invalid choice. Please choose a number between 1 and 9.",
    "Try again. Pick a number from 1 to 9."
]

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
    return Choice1OpenTab(title, url)
#CH1
def Choice1OpenTab(title, url):
    #last opened tab used in many other functions, it is the last opened tab
    chrome_window.append({title: url})
    global last_opened_tab_index
    last_opened_tab_index = chrome_window.index({title: url})
    return

#CH1
def UrlVerifier():
    url_string_input = input("Website URL: ")
    if url_string_input[0:8] == "https://" or url_string_input[0:7] == "http://":
        print("Valid URL")
        return url_string_input
    else:
        print("The URL provided isn't valid,\n\t Try again.. ")
        return UrlVerifier()
def IndexVerifier():
    input_index = input("Choose Index: ")
    if input_index.isdigit():
        return int(input_index)
    elif input_index == "":
        return last_opened_tab_index
    else:
        return IndexVerifier()

def Choice2Prompt():
    for tab_index in range(1, len(chrome_window) + 1):
        print(f"{tab_index - 1}:{chrome_window[tab_index - 1]}")
    index = IndexVerifier()
    return Choice2CloseTab(index)

def Choice2CloseTab(index):
    #index -1 since the index of the choice2prompt is of range len(chrome_window + 1)
    #del/close the tab of the window
    del chrome_window[index]





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
    8.Import Tabs
    9. Exit    
    """)
    input_choice = InputChoiceVerifier()
    #loops until returning or breaking, learned using ai tool doing assignments
    while True:
        if input_choice == 9:
            break
        elif input_choice == 1:
            Choice1Prompt()
        #elif input_choice == 2:

#    def main():
        #ChoiceMenu()

#global variable to be used in and outside the functions
last_opened_tab_index = None
#predefinded set of tabs
chrome_window = [{"slack": "https://slack.com/"}, {"corsera": "https://corsera.org/"}]

print(f"before adding and closing{chrome_window}")
Choice1Prompt()
print(f"after adding, before closing{chrome_window}")
print(last_opened_tab_index)
Choice2Prompt()
print(f"after adding and closing{chrome_window}")






