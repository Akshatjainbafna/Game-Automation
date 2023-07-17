from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options



# Setting up driver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")  # Run in headless mode, i.e, to run in background without opening the browser as we need to authenticate (can be done either scanning QR or using number) & click the checkbox in confirm box(Can't click using selenium, have to be done manually) in the whatsapp
chrome_options.add_experimental_option("prefs", {
    "acceptInsecureCerts": True
})
# initial setup
driver = webdriver.Chrome(options=chrome_options)



# implicit wait, on all searches
driver.implicitly_wait(30)

# explicit wait, only on certain searches
wait = WebDriverWait(driver, 10)
# To be used to make wait for specific conditions, such as visibility of an element, element to be clickable, element to contain specific text, etc.
# wait.until(EC.visibility_of_element_located((By.ID, "my-element")))

action = ActionChains(driver)

# Initialize App

app = Flask(__name__)
CORS(app)


# Middlewares


# Endpoints

@app.route('/play-typing-racing-game', methods=['GET'])
def play_typing_racing_game():

    driver.get('https://onlinetyping.org/typing-games/typing-racing-game/')

    try:
        input_field = driver.find_element(By.ID, 'typebox')
        while True:
            element = driver.find_element(By.CLASS_NAME, 'current-word').text
            input_field.send_keys(element + Keys.SPACE)
    except:
        print('Well Played!')

    return make_response('DONE', 200)

@app.route('/play-typing-ninja-game', methods=['GET'])
def play_typing_ninja_game():
    driver.get('https://onlinetyping.org/typing-games/typing-ninja-master/')

    try:
        start_button = driver.find_element(By.CLASS_NAME, 'tn-start')
        start_button.click()
        body = driver.find_element(By.TAG_NAME, 'body')
        while True:
            letter = driver.find_elements(By.CLASS_NAME, 'tn-key')
            for i in letter:
                body.send_keys(i.text)
    except:
        print('Well Played!')

    return make_response('DONE', 200)


if __name__ == "__main__":
    app.run(debug=True, port=5003)