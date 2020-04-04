#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This experiment was created using PsychoPy2 Experiment Builder
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce (2007) Journal of Neuroscience Methods 162:8-1
  Peirce (2009) Frontiers in Neuroinformatics, 2: 10"""

from numpy import * #many different maths functions
from numpy.random import * #maths randomisation functions
import os #handy system and path functions
from psychopy import core, data, event, visual, gui
import psychopy.log #import like this so it doesn't interfere with numpy.log

#store info about the experiment
expName='None'#from the Builder filename that created this script
expInfo={'participant':'', 'session':'005', 'gender':'', 'age':''}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')#if this fails (e.g. permissions) we will get error
filename= 'data/%s_%s' %(expInfo['participant'], expInfo['date'])
logFile=open(filename+'.log', 'w')
psychopy.log.console.setLevel(psychopy.log.WARNING)#this outputs to the screen, not a file

#setup the Window
win = visual.Window(size=[2560, 1440], fullscr=True, screen=0, allowGUI=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')

#Initialise components for routine:instructions
instructionsClock=core.Clock()
instrText=visual.TextStim(win=win, ori=0,
    text=u"In this experiment you need to respond by pressing;\n  LEFT cursor when the letter is NORMAL\n  RIGHT cursor when it's MIRRORED\n\nPlease respond as quickly and accurately as you can\n\nPress any key to start\n",
    pos=[0, 0], height=0.1,
    color=u'white', colorSpace=u'rgb')

#set up handler to look after randomisation of trials etc
trials=data.TrialHandler(nReps=2.0, method=u'random', extraInfo=expInfo, 
    trialList=data.importTrialList('trialtypes.xlsx'))
thisTrial=trials.trialList[0]#so we can initialise stimuli with some values
#abbrieviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial!=None:
    for paramName in thisTrial.keys():
        exec(paramName+'=thisTrial.'+paramName)

#Initialise components for routine:trial
trialClock=core.Clock()
fixation=visual.TextStim(win=win, ori=0,
    text='+',
    pos=[0, 0], height=0.1,
    color='white', colorSpace='rgb')
target=visual.PatchStim(win=win, tex=image, mask=u'none',
    ori=orientation, pos=[0, 0], size=[400,400], sf=None, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb',
    texRes=128, units=u'pix', interpolate=False)
#create our own class to store info from keyboard
class KeyResponse:
    def __init__(self):
        self.keys=[]#the key(s) pressed
        self.corr=0#was the resp correct this trial? (0=no, 1=yes)
        self.rt=None#response time
        self.clock=None#we'll use this to measure the rt

#Initialise components for routine:goodbye
goodbyeClock=core.Clock()
thanksText=visual.TextStim(win=win, ori=0,
    text='Thanks and goodbye to you!\n',
    pos=[0, 0], height=0.1,
    color='white', colorSpace='rgb')

#update component parameters for each repeat

#run the trial
continueInstructions=True
t=0; instructionsClock.reset()
while continueInstructions and (t<1000000.0000):
    #get current time
    t=instructionsClock.getTime()
    
    #update/draw components on each frame
    if (0.0 <= t):
        instrText.draw()
    if (0.0 <= t):
        theseKeys = event.getKeys()
        if len(theseKeys)>0:#at least one key was pressed
            #abort routine on response
            continueInstructions=False
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    event.clearEvents()#so that it doesn't get clogged with other events
    #refresh the screen
    win.flip()

#end of this routine (e.g. trial)

for thisTrial in trials:
    #abbrieviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial!=None:
        for paramName in thisTrial.keys():
            exec(paramName+'=thisTrial.'+paramName)
    
    #update component parameters for each repeat
    target.setTex(image)
    target.setOri(orientation)
    resp = KeyResponse()#create an object of type KeyResponse
    
    #run the trial
    continueTrial=True
    t=0; trialClock.reset()
    while continueTrial and (t<2.5000):
        #get current time
        t=trialClock.getTime()
        
        #update/draw components on each frame
        if (0.0<= t < (0.0+0.5)):
            fixation.draw()
        if (1.0<= t < (1.0+1.5)):
            target.draw()
        if (1.0<= t < (1.0+1.5)):
            if resp.clock==None: #if we don't have one we've just started
                resp.clock=core.Clock()#create one (now t=0)
            theseKeys = event.getKeys(keyList=u'["left","right"]')
            if len(theseKeys)>0:#at least one key was pressed
                resp.keys=theseKeys[-1]#just the last key pressed
                resp.rt = resp.clock.getTime()
                #was this 'correct'?
                if (resp.keys==str(corrAns)): resp.corr=1
                else: resp.corr=0
                #abort routine on response
                continueTrial=False
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]): core.quit()
        event.clearEvents()#so that it doesn't get clogged with other events
        #refresh the screen
        win.flip()
    
    #end of this routine (e.g. trial)
    if len(resp.keys)>0:#we had a response
        trials.addData('resp.keys',resp.keys)
        trials.addData('resp.corr',resp.corr)
        trials.addData('resp.rt',resp.rt)

#completed 2.0 repeats of 'trials' repeats

trials.saveAsPickle(filename+'trials')
trials.saveAsExcel(filename+'.xlsx', sheetName='trials',
    stimOut=['image', 'orientation', 'mirrored', 'corrAns', ],
    dataOut=['n','all_mean','all_std', 'all_raw'])
psychopy.log.info('saved data to '+filename+'.dlm')

#update component parameters for each repeat

#run the trial
continueGoodbye=True
t=0; goodbyeClock.reset()
while continueGoodbye and (t<1000000.0000):
    #get current time
    t=goodbyeClock.getTime()
    
    #update/draw components on each frame
    if (0.0 <= t):
        thanksText.draw()
    if (0.0 <= t):
        theseKeys = event.getKeys()
        if len(theseKeys)>0:#at least one key was pressed
            #abort routine on response
            continueGoodbye=False
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    event.clearEvents()#so that it doesn't get clogged with other events
    #refresh the screen
    win.flip()

#end of this routine (e.g. trial)
logFile.close()
win.close()
core.quit()
