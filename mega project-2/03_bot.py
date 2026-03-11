import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key="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")
 
def is_last_message_from_sender(chat_log, sender_name="aryan"):

    messages = chat_log.strip().split("/2026]")[-1]

    if sender_name in messages:
        return True
    return False

# Step-1: WhatsApp focus
pyautogui.click (1413, 1054)
time.sleep(1)

while True:



# Step-2: Select chat
 pyautogui.moveTo( 1419 ,152)
 pyautogui.dragTo(1429 ,931, duration=0.5, button='left')

# Step-3: Copy chat
 pyautogui.hotkey('ctrl', 'c')
 time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
 pyautogui.click(1432, 931)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
 chat_history = pyperclip.paste()
 if is_last_message_from_sender(chat_history):

   print(chat_history)

 print(is_last_message_from_sender(chat_history))
 
 completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named aryan who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this (text massage only): "},
            {"role": "user", "content": chat_history}
        ]
        )

 response = completion.choices[0].message.content
 pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
 pyautogui.click(1717, 969)
 time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
 pyautogui.hotkey('ctrl', 'v')
 time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
 pyautogui.press('enter')