import webbrowser
import time
import platform
from selenium import webdriver

def open_webpage(url):
    webbrowser.open(url)

def close_tab(url):
    if platform.system() == "Windows":
        driver = webdriver.Chrome()
    else:
        raise Exception("Unsupported operating system")

    driver.get(url)
    time.sleep(3)
    driver.close()

def main():
    while True:
        user_input = input("Enter a URL: ")
        if user_input.lower() == "exit":
            print("Exiting...")
            break


        open_webpage(user_input)


        time.sleep(3)

        close_tab(user_input)

if __name__ == "__main__":
    main()
