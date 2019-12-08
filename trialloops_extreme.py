#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging, event

# open a white full screen window
win = visual.Window(size =(1000, 600), fullscr=False, allowGUI=True, color='white', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
trialClock = core.Clock()
stimClock = core.Clock()

# Exit whenever 'escape' is pressed
def exit_experiment():
    print(response)
    win.close()
    core.quit()

event.globalKeys.add(key='escape', func=exit_experiment)



# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
# e.g. stim = ['1.jpg','2.jpg','3.jpg']
stimuli = pd.read_table('experiment.csv', sep=',')
stimuli = stimuli.sample(frac=1)
stimuli = stimuli.reset_index(drop=True)


response = pd.DataFrame(columns=['response','time','correct'])

# Other visual things

correctResponse = visual.TextStim(win, text = "Correct!", color = 'black')
wrongResponse = visual.TextStim(win, text = "Wrong", color = 'black')
instructionText = visual.TextStim(win, text = "If the colour of the word \
                                  that appears is a primary colour of the \
                                  artist's colour wheel (Red-Yellow-Blue), \
                                  press ‘y'. Otherwise, press 'n'",
                                  color='black')
background = visual.Rect(win, width=1.6, height=1.5, fillColor="grey")


background.draw()
instructionText.draw()
win.flip()
event.waitKeys()
# make your loop
for i in range(len(stimuli)):
    stimulus = visual.TextStim(win, text=stimuli['text'][i], color=stimuli['colour'][i])
    trialClock.reset()
    background.draw()
    win.flip()
    while trialClock.getTime() < 1:
        core.wait(0.001)
        
    stimClock.reset()
    while stimClock.getTime() < 0.05:
        background.draw()
        stimulus.draw()
        win.flip()
    background.draw()
    win.flip() 
    
    keyresponse = event.waitKeys(keyList = ['y', 'n'], timeStamped=stimClock)
    
    if keyresponse[0][0] == stimuli['cor_response'][i]:
        response = response.append({'response':keyresponse[0][0],'time':keyresponse[0][1],'correct':True}, ignore_index=True)
        background.draw()
        correctResponse.draw()
        win.flip()
        core.wait(2)
    else:
        response = response.append({'response':keyresponse[0][0],'time':keyresponse[0][1],'correct':False}, ignore_index=True)
        background.draw()
        wrongResponse.draw()
        win.flip()
        core.wait(2)

    # if you're recording responses, be sure to store your responses in a list
    # or DataFrame which also uses your iterater!


#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly
print(response)
core.wait(2)
win.close()
