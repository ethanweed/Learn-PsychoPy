#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.62.00), November 02, 2011, at 17:33
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""
import numpy as np  # whole numpy lib is available, pre-pend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os #handy system and path functions
from psychopy import core, data, event, visual, gui
import psychopy.log #import like this so it doesn't interfere with numpy.log
from psychopy.constants import *

#store info about the experiment session
expName='None'#from the Builder filename that created this script
expInfo={'participant':'', 'session':02}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile=psychopy.log.LogFile(filename+'.log', level=psychopy.log.WARNING)
psychopy.log.console.setLevel(psychopy.log.WARNING)#this outputs to the screen, not a file

#setup the Window
win = visual.Window(size=(1680, 1050), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb')

#Initialise components for routine:practInstruct
practInstructClock=core.Clock()
instr1=visual.TextStim(win=win, ori=0, name='instr1',
    text='In this experiment you will be presented with a sequence of between 1 and 6 randomly ordered numbers.\n\nFollowing a short delay you will then be presented with a single number and you will have to decide whether this new number was a member of the sequence.\n\nRespond with the keys;\n - LEFT CURSOR if the number was NOT in the sequence\n - RIGHT CURSOR if the number WAS in the sequence\n\nThere will be a number of practice trials in which you will be given feedback.  Try to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.',
    font='Arial',
    pos=[0, 0], height=0.05,wrapWidth=None,
    color=[1,1,1], colorSpace='rgb', opacity=1)

#Initialise components for routine:trial
trialClock=core.Clock()
fixation=visual.TextStim(win=win, ori=0, name='fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.05,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1)
presentSet=visual.TextStim(win=win, ori=0, name='presentSet',
    text='nonsense',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1)
presentTarget=visual.TextStim(win=win, ori=0, name='presentTarget',
    text='nonsense',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1)

#Initialise components for routine:feedback
feedbackClock=core.Clock()
#msg variable just needs some value at start
msg=''
feedback_2=visual.TextStim(win=win, ori=0, name='feedback_2',
    text='nonsense',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color=[1,1,1], colorSpace='rgb', opacity=1)

#Initialise components for routine:mainInstruct
mainInstructClock=core.Clock()
instr2=visual.TextStim(win=win, ori=0, name='instr2',
    text='OK, ready to start the main experiment?\n\nRemember:\n - LEFT CURSOR for NOT in the sequence\n - RIGHT CURSOR for IN the sequence\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.',
    font='Arial',
    pos=[0, 0], height=0.05,wrapWidth=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1)

#Initialise components for routine:trial
trialClock=core.Clock()
fixation=visual.TextStim(win=win, ori=0, name='fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.05,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1)
presentSet=visual.TextStim(win=win, ori=0, name='presentSet',
    text='nonsense',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1)
presentTarget=visual.TextStim(win=win, ori=0, name='presentTarget',
    text='nonsense',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1)

#Start of routine practInstruct
t=0; practInstructClock.reset()
frameN=-1

#update component parameters for each repeat
OK1 = event.BuilderKeyResponse() #create an object of type KeyResponse
OK1.status=NOT_STARTED
#keep track of which have finished
practInstructComponents=[]#to keep track of which have finished
practInstructComponents.append(instr1)
practInstructComponents.append(OK1)
for thisComponent in practInstructComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#start the Routine
continueRoutine=True
while continueRoutine:
    #get current time
    t=practInstructClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*instr1* updates
    if t>=0.0 and instr1.status==NOT_STARTED:
        #keep track of start time/frame for later
        instr1.tStart=t#underestimates by a little under one frame
        instr1.frameNStart=frameN#exact frame index
        instr1.setAutoDraw(True)
    
    #*OK1* updates
    if t>=0.0 and OK1.status==NOT_STARTED:
        #keep track of start time/frame for later
        OK1.tStart=t#underestimates by a little under one frame
        OK1.frameNStart=frameN#exact frame index
        OK1.status=STARTED
        #keyboard checking is just starting
        OK1.clock.reset() # now t=0
        event.clearEvents()
    if OK1.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys()
        if len(theseKeys)>0:#at least one key was pressed
            OK1.keys=theseKeys[-1]#just the last key pressed
            OK1.rt = OK1.clock.getTime()
            #abort routine on response
            continueRoutine=False
    
    #check if all components have finished
    if not continueRoutine:
        break # lets a component forceEndRoutine
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in practInstructComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#end of routine practInstruct
for thisComponent in practInstructComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)

#set up handler to look after randomisation of conditions etc
pracTrials=data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath='/Users/jwp/Dropbox/newPracs/PsychoPy_pracs_2011v1/for students/Lab2_Sternberg/sternberg/sternberg.psyexp',
    trialList=data.importConditions(u'pracTrials.xlsx'))
thisPracTrial=pracTrials.trialList[0]#so we can initialise stimuli with some values
#abbreviate parameter names if possible (e.g. rgb=thisPracTrial.rgb)
if thisPracTrial!=None:
    for paramName in thisPracTrial.keys():
        exec(paramName+'=thisPracTrial.'+paramName)

for thisPracTrial in pracTrials:
    currentLoop = pracTrials
    #abbrieviate parameter names if possible (e.g. rgb=thisPracTrial.rgb)
    if thisPracTrial!=None:
        for paramName in thisPracTrial.keys():
            exec(paramName+'=thisPracTrial.'+paramName)
    
    #Start of routine trial
    t=0; trialClock.reset()
    frameN=-1
    
    #update component parameters for each repeat
    presentSet.setText(numberSet)
    presentTarget.setText(target)
    resp = event.BuilderKeyResponse() #create an object of type KeyResponse
    resp.status=NOT_STARTED
    #keep track of which have finished
    trialComponents=[]#to keep track of which have finished
    trialComponents.append(fixation)
    trialComponents.append(presentSet)
    trialComponents.append(presentTarget)
    trialComponents.append(resp)
    for thisComponent in trialComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #start the Routine
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=trialClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        #*fixation* updates
        if t>=0.0 and fixation.status==NOT_STARTED:
            #keep track of start time/frame for later
            fixation.tStart=t#underestimates by a little under one frame
            fixation.frameNStart=frameN#exact frame index
            fixation.setAutoDraw(True)
        elif fixation.status==STARTED and t>=(0.0+1.0):
            fixation.setAutoDraw(False)
        
        #*presentSet* updates
        if t>=1.2 and presentSet.status==NOT_STARTED:
            #keep track of start time/frame for later
            presentSet.tStart=t#underestimates by a little under one frame
            presentSet.frameNStart=frameN#exact frame index
            presentSet.setAutoDraw(True)
        elif presentSet.status==STARTED and t>=(1.2+1.5):
            presentSet.setAutoDraw(False)
        
        #*presentTarget* updates
        if t>=4.7 and presentTarget.status==NOT_STARTED:
            #keep track of start time/frame for later
            presentTarget.tStart=t#underestimates by a little under one frame
            presentTarget.frameNStart=frameN#exact frame index
            presentTarget.setAutoDraw(True)
        elif presentTarget.status==STARTED and t>=(4.7+2):
            presentTarget.setAutoDraw(False)
        
        #*resp* updates
        if t>=4.7 and resp.status==NOT_STARTED:
            #keep track of start time/frame for later
            resp.tStart=t#underestimates by a little under one frame
            resp.frameNStart=frameN#exact frame index
            resp.status=STARTED
            #keyboard checking is just starting
            resp.clock.reset() # now t=0
            event.clearEvents()
        if resp.status==STARTED:#only update if being drawn
            theseKeys = event.getKeys(keyList=['left', 'right'])
            if len(theseKeys)>0:#at least one key was pressed
                resp.keys=theseKeys[-1]#just the last key pressed
                resp.rt = resp.clock.getTime()
                #was this 'correct'?
                if (resp.keys==str(corrAns)): resp.corr=1
                else: resp.corr=0
                #abort routine on response
                continueRoutine=False
        
        #check if all components have finished
        if not continueRoutine:
            break # lets a component forceEndRoutine
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]): core.quit()
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #end of routine trial
    for thisComponent in trialComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    #check responses
    if len(resp.keys)==0: #No response was made
       resp.keys=None
       #was no response the correct answer?!
       if str(corrAns).lower()=='none':resp.corr=1 #correct non-response
       else: resp.corr=0 #failed to respond (incorrectly)
    #store data for pracTrials (TrialHandler)
    pracTrials.addData('resp.keys',resp.keys)
    pracTrials.addData('resp.corr',resp.corr)
    if resp.keys != None:#we had a response
        pracTrials.addData('resp.rt',resp.rt)
    
    #Start of routine feedback
    t=0; feedbackClock.reset()
    frameN=-1
    
    #update component parameters for each repeat
    if resp.corr:#stored on last run routine
      msg="Correct! RT=%.3f" %(resp.rt)
    else:
      msg="Oops! That was wrong"
    feedback_2.setText(msg)
    #keep track of which have finished
    feedbackComponents=[]#to keep track of which have finished
    feedbackComponents.append(feedback_2)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #start the Routine
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=feedbackClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        
        #*feedback_2* updates
        if t>=0.0 and feedback_2.status==NOT_STARTED:
            #keep track of start time/frame for later
            feedback_2.tStart=t#underestimates by a little under one frame
            feedback_2.frameNStart=frameN#exact frame index
            feedback_2.setAutoDraw(True)
        elif feedback_2.status==STARTED and t>=(0.0+1.0):
            feedback_2.setAutoDraw(False)
        
        #check if all components have finished
        if not continueRoutine:
            break # lets a component forceEndRoutine
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]): core.quit()
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #end of routine feedback
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    

#completed 1.0 repeats of 'pracTrials'

pracTrials.saveAsPickle(filename+'pracTrials')
pracTrials.saveAsExcel(filename+'.xlsx', sheetName='pracTrials',
    stimOut=pracTrials.trialList[0].keys(),
    dataOut=['n','all_mean','all_std', 'all_raw'])

#Start of routine mainInstruct
t=0; mainInstructClock.reset()
frameN=-1

#update component parameters for each repeat
OK2 = event.BuilderKeyResponse() #create an object of type KeyResponse
OK2.status=NOT_STARTED
#keep track of which have finished
mainInstructComponents=[]#to keep track of which have finished
mainInstructComponents.append(instr2)
mainInstructComponents.append(OK2)
for thisComponent in mainInstructComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#start the Routine
continueRoutine=True
while continueRoutine:
    #get current time
    t=mainInstructClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*instr2* updates
    if t>=0.0 and instr2.status==NOT_STARTED:
        #keep track of start time/frame for later
        instr2.tStart=t#underestimates by a little under one frame
        instr2.frameNStart=frameN#exact frame index
        instr2.setAutoDraw(True)
    
    #*OK2* updates
    if t>=0.0 and OK2.status==NOT_STARTED:
        #keep track of start time/frame for later
        OK2.tStart=t#underestimates by a little under one frame
        OK2.frameNStart=frameN#exact frame index
        OK2.status=STARTED
        #keyboard checking is just starting
        OK2.clock.reset() # now t=0
        event.clearEvents()
    if OK2.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys()
        if len(theseKeys)>0:#at least one key was pressed
            OK2.keys=theseKeys[-1]#just the last key pressed
            OK2.rt = OK2.clock.getTime()
            #abort routine on response
            continueRoutine=False
    
    #check if all components have finished
    if not continueRoutine:
        break # lets a component forceEndRoutine
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in mainInstructComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#end of routine mainInstruct
for thisComponent in mainInstructComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)

#set up handler to look after randomisation of conditions etc
trials=data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath='/Users/jwp/Dropbox/newPracs/PsychoPy_pracs_2011v1/for students/Lab2_Sternberg/sternberg/sternberg.psyexp',
    trialList=data.importConditions(u'mainTrials.xlsx'))
thisTrial=trials.trialList[0]#so we can initialise stimuli with some values
#abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial!=None:
    for paramName in thisTrial.keys():
        exec(paramName+'=thisTrial.'+paramName)

for thisTrial in trials:
    currentLoop = trials
    #abbrieviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial!=None:
        for paramName in thisTrial.keys():
            exec(paramName+'=thisTrial.'+paramName)
    
    #Start of routine trial
    t=0; trialClock.reset()
    frameN=-1
    
    #update component parameters for each repeat
    presentSet.setText(numberSet)
    presentTarget.setText(target)
    resp = event.BuilderKeyResponse() #create an object of type KeyResponse
    resp.status=NOT_STARTED
    #keep track of which have finished
    trialComponents=[]#to keep track of which have finished
    trialComponents.append(fixation)
    trialComponents.append(presentSet)
    trialComponents.append(presentTarget)
    trialComponents.append(resp)
    for thisComponent in trialComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #start the Routine
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=trialClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        #*fixation* updates
        if t>=0.0 and fixation.status==NOT_STARTED:
            #keep track of start time/frame for later
            fixation.tStart=t#underestimates by a little under one frame
            fixation.frameNStart=frameN#exact frame index
            fixation.setAutoDraw(True)
        elif fixation.status==STARTED and t>=(0.0+1.0):
            fixation.setAutoDraw(False)
        
        #*presentSet* updates
        if t>=1.2 and presentSet.status==NOT_STARTED:
            #keep track of start time/frame for later
            presentSet.tStart=t#underestimates by a little under one frame
            presentSet.frameNStart=frameN#exact frame index
            presentSet.setAutoDraw(True)
        elif presentSet.status==STARTED and t>=(1.2+1.5):
            presentSet.setAutoDraw(False)
        
        #*presentTarget* updates
        if t>=4.7 and presentTarget.status==NOT_STARTED:
            #keep track of start time/frame for later
            presentTarget.tStart=t#underestimates by a little under one frame
            presentTarget.frameNStart=frameN#exact frame index
            presentTarget.setAutoDraw(True)
        elif presentTarget.status==STARTED and t>=(4.7+2):
            presentTarget.setAutoDraw(False)
        
        #*resp* updates
        if t>=4.7 and resp.status==NOT_STARTED:
            #keep track of start time/frame for later
            resp.tStart=t#underestimates by a little under one frame
            resp.frameNStart=frameN#exact frame index
            resp.status=STARTED
            #keyboard checking is just starting
            resp.clock.reset() # now t=0
            event.clearEvents()
        if resp.status==STARTED:#only update if being drawn
            theseKeys = event.getKeys(keyList=['left', 'right'])
            if len(theseKeys)>0:#at least one key was pressed
                resp.keys=theseKeys[-1]#just the last key pressed
                resp.rt = resp.clock.getTime()
                #was this 'correct'?
                if (resp.keys==str(corrAns)): resp.corr=1
                else: resp.corr=0
                #abort routine on response
                continueRoutine=False
        
        #check if all components have finished
        if not continueRoutine:
            break # lets a component forceEndRoutine
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]): core.quit()
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #end of routine trial
    for thisComponent in trialComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    #check responses
    if len(resp.keys)==0: #No response was made
       resp.keys=None
       #was no response the correct answer?!
       if str(corrAns).lower()=='none':resp.corr=1 #correct non-response
       else: resp.corr=0 #failed to respond (incorrectly)
    #store data for trials (TrialHandler)
    trials.addData('resp.keys',resp.keys)
    trials.addData('resp.corr',resp.corr)
    if resp.keys != None:#we had a response
        trials.addData('resp.rt',resp.rt)

#completed 1.0 repeats of 'trials'

trials.saveAsPickle(filename+'trials')
trials.saveAsExcel(filename+'.xlsx', sheetName='trials',
    stimOut=trials.trialList[0].keys(),
    dataOut=['n','all_mean','all_std', 'all_raw'])


#Shutting down:
win.close()
core.quit()
