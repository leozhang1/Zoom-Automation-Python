import subprocess
import pyautogui
from time import sleep
from math import nan
import pandas as pd
import sys
from datetime import datetime, date
from enum import IntEnum, unique
pyautogui.PAUSE = 2.5

has_signed_in = False

@unique
class WeekDays(IntEnum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4


def sign_in(meetingid, pswd=''):
    # Opens up the zoom app
    # change the path specific to your computer

    # If on windows use below line for opening zoom
    # subprocess.call('C:\\myprogram.exe')

    # If on mac / Linux use below line for opening zoom
    subprocess.call(r'C:\Users\Leo Zhang\AppData\Roaming\Zoom\bin\Zoom.exe')

    sleep(5)

    # clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    # sleep(5)
    # print('writing meeting id')

    # Type the meeting ID
    # meeting_id_btn =  pyautogui.locateCenterOnScreen('meeting_id_button.png')
    meeting_id_btn = pyautogui.locateCenterOnScreen('meeting_id_button.png')
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

    # Types the password (if there is one) and hits enter
    if len(pswd) > 0:
        meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_pswd.png')
        pyautogui.moveTo(meeting_pswd_btn)
        pyautogui.click()
        pyautogui.write(pswd)
        pyautogui.press('enter')

    global has_signed_in
    has_signed_in = True


# pass in the proper meeting id based on week day
def validate_signin(meeting_id, pswd='') -> None:
    sign_in(str(meeting_id), str(pswd))
    sleep(30)
    print('signed in')


# Reading the file
df = pd.read_csv(r'timings.csv')
# print(df.loc[4]['timings'])
# print(df.loc[4]['meetingid'])

# df.head() gets the first n rows, with n=5 as default
# loc slicing is inclusive, iloc is not
# loc uses label names as index values and iloc uses integers
# df.iloc[x] gets the xth row (vertical display)
# df.iloc[[x]] gets the xth row (horizontal display)
# df.iat[3, 0] similar to iloc but I think it's faster, but only limited to getting one value though
# df.loc[x] gets the xth row
# df['x'] gets all the rows at column named 'x'
# len(df.columns) gets total number of columns
# len(df.index) gets total number of rows

# tuesdays and thursdays
# print(df.loc[0]['meetingid']) # cot 5405
# print(df.loc[2]['meetingid']) # cda 5106

# mondays and wednesdays
# print(df.loc[1]['meetingid']) # machine learning
# print(df.loc[3]['meetingid'])
# print(df.shape)


# toggle the meeting id based on weekday
while not has_signed_in:

    # checking of the current time exists in our csv file
    # per while loop iteration
    now = datetime.now().strftime("%H:%M")
    # print(now)

    if (date.today().weekday() == WeekDays.Monday or date.today().weekday() == WeekDays.Wednesday):
        # cap 5610
        if now in df.loc[1]['timings']:
            validate_signin(df.loc[1]['meetingid'])

        # cop 4520
        elif now in df.loc[3]['timings']:
            validate_signin(df.loc[3]['meetingid'])

    elif date.today().weekday() == WeekDays.Tuesday or date.today().weekday() == WeekDays.Thursday:
        # cot 5405
        if now in df.loc[0]['timings']:
            validate_signin(df.loc[0]['meetingid'])

        # CDA 5106
        elif now in df.loc[2]['timings']:
            print('signing in with meeting id: {}'.format(df.loc[2]['meetingid']))
            validate_signin(df.loc[2]['meetingid'], df.loc[2]['meetingpswd'])

    elif date.today().weekday() == WeekDays.Friday:

        if now in df.loc[4]['timings']:
            validate_signin(df.loc[4]['meetingid'])




# COT 5405
# sign_in('95328856968')

# # CAP 5610
# sign_in('97574442477')

# # CDA 5106
# sign_in('99116126834', 'CDA5106')

# COP 4520
# sign_in('95528809821')

# now = datetime.now().strftime("%H:%M")
#     # print(now)
#     if datetime.now().hour == 0:
#         now = '12:'+ now[3:]

#     if now in str(df['timings']):

#         row = df.loc[df['timings'] == now]
#         m_id = str(row.iloc[0,1])
#         m_pswd = str(row.iloc[0,2])


#         sign_in(m_id, '')
#         sleep(30)
#         print('signed in')
