#!/usr/bin/python3
#Countdown-timer.pyw
version = 0.4

#############################################################
# This monstrosity was created by crash_horror (373vFS_Crash)
# and comes without warranty of any kind,
# read the license at the bottom.
# (https://github.com/crash-horror)
#############################################################

# displaytruetime = str(time.strftime("%H:%M", time.localtime(time.time() + durr)))

# elitetime = time.strftime("%H:%M", time.localtime())

import sys
import time
import pygame
from pygame.locals import *

# some colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
silver = (192, 192, 192)
gray = (128, 128, 128)
darkgray = (20, 20, 20)
verydarkgray = (10, 10, 10)
maroon = (128, 0, 0)
olive = (128, 128, 0)
orange = (255, 165, 0)
green = (0, 128, 0)
purple = (128, 0, 128)
teal = (0, 128, 128)
navy = (0, 0, 128)
ground = (84, 53, 10)
sky = (0, 76, 255)

pygame.init()

fpsTime = pygame.time.Clock()
fps = 60
bg = black
dispWidth = 500
dispHeight = 300


def switch_start_button_state(_astate):
    if _astate[0] == "START":
        return ["RUNNING", orange]
    elif _astate[0] == "RUNNING":
        return ["RESET", red]
    elif _astate[0] == "RESET":
        return ["START", green]


def switch_alarm_state(_astate):
    if _astate[0] == "ON":
        return ["OFF", darkgray]
    elif _astate[0] == "OFF":
        return ["ON", maroon]


def switch_gmt_state(_astate):
    return not _astate


def runMainLoop():
    durr = 600
    state = ["START", green]
    alarmstate = ["OFF", darkgray]
    howfull = 105
    isitlocaltime = True

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # start button and gmt button press
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                alarm.stop()
                pos = pygame.mouse.get_pos()
                if startbuttonRECT.collidepoint(pos):
                    state = switch_start_button_state(state)
                    click1.play()
                    if state[0] == "RUNNING":
                        now = time.time()
                        future = now + durr
                if clockRECT.collidepoint(pos):
                    click1.play()
                    isitlocaltime = switch_gmt_state(isitlocaltime)

        # alarm button press
                if alarmRECT.collidepoint(pos):
                    click3.play()
                    alarmstate = switch_alarm_state(alarmstate)

        # mousewheel UP
            if state[0] != "RUNNING":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                    pos = pygame.mouse.get_pos()
                    if minuteRECT.collidepoint(pos):
                        durr += 60
                    if secondRECT.collidepoint(pos):
                        durr += 1

        # mousewheel DOWN
            if state[0] != "RUNNING":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                    pos = pygame.mouse.get_pos()
                    if minuteRECT.collidepoint(pos):
                        durr -= 60
                    if secondRECT.collidepoint(pos):
                        durr -= 1

    # cap duration to positive
        if durr < 0:
            durr = 0

    # calculate state
        if state[0] == "START":
            if isitlocaltime:
                displaytruetime = str(time.strftime("%H:%M", time.localtime(time.time() + durr)))
            else:
                displaytruetime = str(time.strftime("%H:%M", time.gmtime(time.time() + durr)))
            displaytime = str(time.strftime("%M:%S", time.gmtime(durr)))
            displayhour = str(time.strftime("%H", time.gmtime(durr)))
            howfull = 100
        elif state[0] == "RUNNING":
            dt = future - time.time()
        # calculate alarm state
            howfull = int(100 * dt  / durr)
            if dt < 00.1:
                if alarmstate[0] == "OFF":
                    alarm.play(loops = 3)
                else:
                    alarm.play(loops = -1)
                state = ["RESET", red]
            if isitlocaltime:
                displaytruetime = str(time.strftime("%H:%M", time.localtime(future)))
            else:
                displaytruetime = str(time.strftime("%H:%M", time.gmtime(future)))
            displaytime = str(time.strftime("%M:%S", time.gmtime(dt)))
            displayhour = str(time.strftime("%H", time.gmtime(dt)))
        elif state[0] == "RESET":
            if isitlocaltime:
                displaytruetime = str(time.strftime("%H:%M", time.localtime(future)))
            else:
                displaytruetime = str(time.strftime("%H:%M", time.gmtime(future)))
            displaytime = str(time.strftime("%M:%S", time.gmtime(dt)))
            displayhour = str(time.strftime("%H", time.gmtime(dt)))

    # start drawing stuff
        setDisplay.fill(bg)

    # draw dummy rects for mousewheel editing
        minuteRECT = pygame.draw.rect(setDisplay, black, ((100, 0), (170, 150)))
        secondRECT = pygame.draw.rect(setDisplay, black, ((305, 0), (245, 150)))

    # draw dummy rect for elite clock switching
        clockRECT = pygame.draw.rect(setDisplay, black, ((140, 230), (500, 300)))

    # elite clock
        if isitlocaltime:
            elitetime = time.strftime("%H:%M", time.localtime())
        else:
            elitetime = time.strftime("%H:%M", time.gmtime())
        elitetimeTXT = largeboldfont.render(elitetime, True, darkgray)
        setDisplay.blit(elitetimeTXT, (375, 235))

    # draw start button
        startbuttonRECT = pygame.draw.rect(setDisplay, darkgray, ((140, 170), (220, 60)))
        startbuttonTXT = largeboldfont.render(state[0], True, state[1])
        setDisplay.blit(startbuttonTXT, (250 - startbuttonTXT.get_width() // 2, 170))

    # draw alarm button
        alarmRECT = pygame.draw.rect(setDisplay, alarmstate[1], ((375, 170), (110, 60)))
        setDisplay.blit(alarm1TXT, (430 - alarm1TXT.get_width() // 2, 170))
        setDisplay.blit(alarm2TXT, (430 - alarm2TXT.get_width() // 2, 195))

    # draw timer
        clockfaceTXT = hugefont.render(displaytime, True, gray)
        setDisplay.blit(clockfaceTXT, (100, -10))

    # draw hours
        hourTXT = largeboldfont.render(displayhour + ":", True, gray)
        setDisplay.blit(hourTXT, (30, 95))

    # draw 10min reset
        truetimeRECT = pygame.draw.rect(setDisplay, darkgray, ((140, 245), (220, 40)))
        truetimeTXT = infofont.render(displaytruetime, True, gray)
        setDisplay.blit(truetimeTXT, (250 - truetimeTXT.get_width() // 2, 250))

    # draw graphic
        graphbackRECT = pygame.draw.rect(setDisplay, darkgray, ((15, 170), (110, 115)))
        graphfrontRECT = pygame.draw.rect(setDisplay, maroon, ((20, 175), (100, 105)))
        graphmaskRECT = pygame.draw.rect(setDisplay, darkgray, ((20, 175), (100, howfull)))
        percentstring = str(100 - howfull) + "%"
        percentTXT = infofont.render(percentstring, True, black)
        setDisplay.blit(percentTXT, (70 - percentTXT.get_width() // 2, 210))

    # draw gmt indicator
        if not isitlocaltime:
            setDisplay.blit(gmtTXT, (15, 15))

    # update display
        pygame.display.flip()
        fpsTime.tick(fps)


# setup
pygame.display.set_caption('Countdown Timer v' + str(version))
setDisplay = pygame.display.set_mode((dispWidth, dispHeight))
# setDisplay = pygame.display.set_mode((dispWidth, dispHeight), pygame.NOFRAME)

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# audio
alarm = pygame.mixer.Sound("alarm.wav")
click1 = pygame.mixer.Sound("click1.wav")
click2 = pygame.mixer.Sound("click2.wav")
click3 = pygame.mixer.Sound("click3.wav")

# fonts
hugefont = pygame.font.SysFont("tahoma", 150)
largeboldfont = pygame.font.SysFont("tahoma", 45)
infofont = pygame.font.SysFont("tahoma", 25)
# labelfont = pygame.font.SysFont("tahoma", 15)


# text
# tenminTXT = infofont.render("10:00", True, gray)
alarm1TXT = infofont.render("ALARM", True, black)
alarm2TXT = infofont.render("REPEAT", True, black)
gmtTXT = infofont.render("GMT", True, (50, 50, 50))


# run the thing
runMainLoop()





# notes
# -------------------------------------------------------
"""

"""


# license
# -------------------------------------------------------
"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
"""