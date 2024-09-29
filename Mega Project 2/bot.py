import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
  api_key="<Your Key Here>",
)

def is_last_message_from_sender(chat_log, sender_name="Riad Sir"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False
    
# Step 1: Click on the chrome icon at coordinates (827, 750)
pyautogui.click(827, 750)
time.sleep(1)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)

    # Step 2: Click at (897, 664)
    pyautogui.click(897, 664)
    time.sleep(1)

    # Step 3: Drag the mouse from (889, 186) to (1349, 664) to select the text
    pyautogui.moveTo(889, 186)
    pyautogui.dragTo(1349, 664, duration=2.0, button='left')  # Drag for 2 seconds

    # Step 4: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 2 seconds to ensure the copy command is completed

    # Step 5: Click at coordinates (498, 262)
    pyautogui.click(498, 262)
    time.sleep(1)  # Wait for 1 second to ensure the click is registered

    # Step 6: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named MD. Shamir Hossain who speaks Hindi as well as English. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Riad Sir: "},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 7: Paste the generated text from OpenAI
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 8: Press Enter
        pyautogui.press('enter')

