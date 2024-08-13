#name of file: script1.py

import webbrowser  # Imports the webbrowser module to open URLs in the default web browser.
import sys  # Imports the sys module to access command-line arguments and interact with the Python runtime environment.
import logging  # Imports the logging module to enable logging of events, such as opening URLs or encountering errors.

# URL sets dictionary: Each key (e.g., 'school', 'work', 'personal') corresponds to a list of URLs.
URLS = {
    "school": [
        "https://saprd.my.uh.edu/psp/saprd/?cmd=login&languageCd=ENG", 
        "https://canvas.uh.edu/"
    ],
    "work": [
        "https://www.overleaf.com/project/65a09ab5636602908427c0d1", 
        "https://github.com/ArsalJafri", 
        "https://chatgpt.com/?model=auto"
    ],
    "personal": [
        "https://www.youtube.com/", 
        "https://v2.scrimba.com/the-ai-engineer-path-c02v", 
        "https://www.netflix.com/login"
    ],
    "code-help": [
        "https://www.geeksforgeeks.org/",
        "https://react.dev/",
    ],
    "data-structures-teach": [
        "https://teachyourselfcs.com/#algorithms",
        "https://runestone.academy/ns/books/published/pythonds3/Introduction/GettingStartedwithData.html"
        "https://www.hellointerview.com/learn/code?utm_source=reddit&utm_medium=social&utm_campaign=code-launch"
    ],
    "cosc 2436": [
        "https://canvas.uh.edu/courses/12613"
    ],
}

# Default set name: Used if the user doesn't provide a specific set name as a command-line argument.
DEFAULT_SET = "personal"

# Set up logging: Logs are written to 'web_opener.log' with messages formatted to include timestamps.
logging.basicConfig(filename='web_opener.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to open all URLs in a given list.
def open_webpages(urls):
    for url in urls:
        try:
            # Print and log each URL as it's opened.
            print(f"Opening {url}")
            webbrowser.open(url)
            logging.info(f"Opened {url}")
        except Exception as e:
            # If opening the URL fails, print and log the error.
            print(f"Failed to open {url}: {e}")
            logging.error(f"Failed to open {url}: {e}")

# Main block: Executes only if the script is run directly (not imported as a module).
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If the user provided arguments, iterate through them to open multiple sets.
        for set_name in sys.argv[1:]:
            if set_name == "--help":
                # Print usage instructions if the user asks for help.
                print("Usage: python script.py [set_name]\nAvailable sets: school, work, personal")
            elif set_name in URLS:
                # If the set name exists in the URLS dictionary, open the associated URLs.
                urls = URLS[set_name]
                open_webpages(urls)
            else: 
                # If the set name doesn't exist, notify the user.
                print(f"No URL set found for '{set_name}'")
    else:
        # If no arguments are provided, open the default set of URLs.
        print(f"No set name provided, opening default set '{DEFAULT_SET}'.")
        set_name = DEFAULT_SET
        urls = URLS[set_name]
        open_webpages(urls)

