import subprocess
import pyautogui
from time import sleep
from math import nan
import pandas as pd
from datetime import datetime
pyautogui.PAUSE = 2.5

has_signed_in = False

# program assumes no passcode
def sign_in(meetingid, pswd=''):
    #Opens up the zoom app
    #change the path specific to your computer

    #If on windows use below line for opening zoom
    #subprocess.call('C:\\myprogram.exe')

    #If on mac / Linux use below line for opening zoom
    subprocess.call(r'C:\Users\Leo Zhang\AppData\Roaming\Zoom\bin\Zoom.exe')

    sleep(5)

    #clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    # sleep(5)
    # print('writing meeting id')

    # Type the meeting ID
    # meeting_id_btn =  pyautogui.locateCenterOnScreen('meeting_id_button.png')
    meeting_id_btn =  pyautogui.locateCenterOnScreen('meeting_id_button.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meetingid)

    # Disables both the camera and the mic
    media_btn = pyautogui.locateAllOnScreen('media_btn.png')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        sleep(1.5)

    # Hits the join button
    join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    has_signed_in = True

    # sleep(5)

    #Types the password and hits enter
    # try:
    #     meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    #     pyautogui.moveTo(meeting_pswd_btn)
    #     pyautogui.click()
    #     pyautogui.write(pswd)
    #     pyautogui.press('enter')
    # except Exception:
    #     pswd = ''

# Reading the file
# df = pd.read_csv('timings.csv')


# while not has_signed_in:

#     # checking of the current time exists in our csv file
#     # per while loop iteration
#     now = datetime.now().strftime("%H:%M")
#     # print(now)
#     if datetime.now().hour == 0:
#         now = '12:'+ now[3:]
#     if now in str(df['timings']):
#        row = df.loc[df['timings'] == now]
#        m_id = str(row.iloc[0,1])
#     #    print('m_id: {}'.format(m_id))
#        m_pswd = str(row.iloc[0,2])
#     #    print('m_pswd: {}'.format(m_pswd))
#     #    print(m_pswd == nan)

    #    sign_in(m_id, '')
    #    sleep(30)
    #    print('signed in')


# COT 5405
# sign_in('95328856968')

# # CAP 5610
# sign_in('97574442477')

# # CDA 5106
# sign_in('99116126834', 'CDA5106')

# COP 4520
# sign_in('95528809821')
