#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Wed Aug 26 09:46:28 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'sternberg'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '02'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/ethan/Documents/GitHub/Learn-PsychoPy/Labs/Sternberg/sternberg_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "practInstruct"
practInstructClock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text='In this experiment you will be presented with a sequence of between 1 and 6 randomly ordered numbers.\n\nFollowing a short delay you will then be presented with a single number and you will have to decide whether this new number was a member of the sequence.\n\nRespond with the keys;\n - LEFT CURSOR if the number was NOT in the sequence\n - RIGHT CURSOR if the number WAS in the sequence\n\nThere will be a number of practice trials in which you will be given feedback.  Try to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
OK1 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
presentSet = visual.TextStim(win=win, name='presentSet',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
presentTarget = visual.TextStim(win=win, name='presentTarget',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#msg variable just needs some value at start
msg=''
feedback_2 = visual.TextStim(win=win, name='feedback_2',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "mainInstruct"
mainInstructClock = core.Clock()
instr2 = visual.TextStim(win=win, name='instr2',
    text='OK, ready to start the main experiment?\n\nRemember:\n - LEFT CURSOR for NOT in the sequence\n - RIGHT CURSOR for IN the sequence\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
OK2 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
presentSet = visual.TextStim(win=win, name='presentSet',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
presentTarget = visual.TextStim(win=win, name='presentTarget',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "practInstruct"-------
continueRoutine = True
# update component parameters for each repeat
OK1.keys = []
OK1.rt = []
_OK1_allKeys = []
# keep track of which components have finished
practInstructComponents = [instr1, OK1]
for thisComponent in practInstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practInstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practInstruct"-------
while continueRoutine:
    # get current time
    t = practInstructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practInstructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1.frameNStart = frameN  # exact frame index
        instr1.tStart = t  # local t and not account for scr refresh
        instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
        instr1.setAutoDraw(True)
    
    # *OK1* updates
    waitOnFlip = False
    if OK1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OK1.frameNStart = frameN  # exact frame index
        OK1.tStart = t  # local t and not account for scr refresh
        OK1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OK1, 'tStartRefresh')  # time at next scr refresh
        OK1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(OK1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(OK1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if OK1.status == STARTED and not waitOnFlip:
        theseKeys = OK1.getKeys(keyList=None, waitRelease=False)
        _OK1_allKeys.extend(theseKeys)
        if len(_OK1_allKeys):
            OK1.keys = _OK1_allKeys[-1].name  # just the last key pressed
            OK1.rt = _OK1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practInstruct"-------
for thisComponent in practInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr1.started', instr1.tStartRefresh)
thisExp.addData('instr1.stopped', instr1.tStopRefresh)
# check responses
if OK1.keys in ['', [], None]:  # No response was made
    OK1.keys = None
thisExp.addData('OK1.keys',OK1.keys)
if OK1.keys != None:  # we had a response
    thisExp.addData('OK1.rt', OK1.rt)
thisExp.addData('OK1.started', OK1.tStartRefresh)
thisExp.addData('OK1.stopped', OK1.tStopRefresh)
thisExp.nextEntry()
# the Routine "practInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pracTrials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pracTrials.xlsx'),
    seed=None, name='pracTrials')
thisExp.addLoop(pracTrials)  # add the loop to the experiment
thisPracTrial = pracTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracTrial.rgb)
if thisPracTrial != None:
    for paramName in thisPracTrial:
        exec('{} = thisPracTrial[paramName]'.format(paramName))

for thisPracTrial in pracTrials:
    currentLoop = pracTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracTrial.rgb)
    if thisPracTrial != None:
        for paramName in thisPracTrial:
            exec('{} = thisPracTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    presentSet.setText(numberSet)
    presentTarget.setText(target)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixation, presentSet, presentTarget, resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *presentSet* updates
        if presentSet.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
            # keep track of start time/frame for later
            presentSet.frameNStart = frameN  # exact frame index
            presentSet.tStart = t  # local t and not account for scr refresh
            presentSet.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presentSet, 'tStartRefresh')  # time at next scr refresh
            presentSet.setAutoDraw(True)
        if presentSet.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > presentSet.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                presentSet.tStop = t  # not accounting for scr refresh
                presentSet.frameNStop = frameN  # exact frame index
                win.timeOnFlip(presentSet, 'tStopRefresh')  # time at next scr refresh
                presentSet.setAutoDraw(False)
        
        # *presentTarget* updates
        if presentTarget.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
            # keep track of start time/frame for later
            presentTarget.frameNStart = frameN  # exact frame index
            presentTarget.tStart = t  # local t and not account for scr refresh
            presentTarget.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presentTarget, 'tStartRefresh')  # time at next scr refresh
            presentTarget.setAutoDraw(True)
        if presentTarget.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > presentTarget.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                presentTarget.tStop = t  # not accounting for scr refresh
                presentTarget.frameNStop = frameN  # exact frame index
                win.timeOnFlip(presentTarget, 'tStopRefresh')  # time at next scr refresh
                presentTarget.setAutoDraw(False)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                resp.rt = _resp_allKeys[-1].rt
                # was this correct?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pracTrials.addData('fixation.started', fixation.tStartRefresh)
    pracTrials.addData('fixation.stopped', fixation.tStopRefresh)
    pracTrials.addData('presentSet.started', presentSet.tStartRefresh)
    pracTrials.addData('presentSet.stopped', presentSet.tStopRefresh)
    pracTrials.addData('presentTarget.started', presentTarget.tStartRefresh)
    pracTrials.addData('presentTarget.stopped', presentTarget.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for pracTrials (TrialHandler)
    pracTrials.addData('resp.keys',resp.keys)
    pracTrials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        pracTrials.addData('resp.rt', resp.rt)
    pracTrials.addData('resp.started', resp.tStartRefresh)
    pracTrials.addData('resp.stopped', resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if resp.corr:#stored on last run routine
      msg="Correct! RT=%.3f" %(resp.rt)
    else:
      msg="Oops! That was wrong"
    feedback_2.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedback_2]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_2* updates
        if feedback_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_2.frameNStart = frameN  # exact frame index
            feedback_2.tStart = t  # local t and not account for scr refresh
            feedback_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_2, 'tStartRefresh')  # time at next scr refresh
            feedback_2.setAutoDraw(True)
        if feedback_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback_2.tStop = t  # not accounting for scr refresh
                feedback_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_2, 'tStopRefresh')  # time at next scr refresh
                feedback_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pracTrials.addData('feedback_2.started', feedback_2.tStartRefresh)
    pracTrials.addData('feedback_2.stopped', feedback_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'pracTrials'


# ------Prepare to start Routine "mainInstruct"-------
continueRoutine = True
# update component parameters for each repeat
OK2.keys = []
OK2.rt = []
_OK2_allKeys = []
# keep track of which components have finished
mainInstructComponents = [instr2, OK2]
for thisComponent in mainInstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
mainInstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "mainInstruct"-------
while continueRoutine:
    # get current time
    t = mainInstructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=mainInstructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2* updates
    if instr2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr2.frameNStart = frameN  # exact frame index
        instr2.tStart = t  # local t and not account for scr refresh
        instr2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr2, 'tStartRefresh')  # time at next scr refresh
        instr2.setAutoDraw(True)
    
    # *OK2* updates
    waitOnFlip = False
    if OK2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OK2.frameNStart = frameN  # exact frame index
        OK2.tStart = t  # local t and not account for scr refresh
        OK2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OK2, 'tStartRefresh')  # time at next scr refresh
        OK2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(OK2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(OK2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if OK2.status == STARTED and not waitOnFlip:
        theseKeys = OK2.getKeys(keyList=None, waitRelease=False)
        _OK2_allKeys.extend(theseKeys)
        if len(_OK2_allKeys):
            OK2.keys = _OK2_allKeys[-1].name  # just the last key pressed
            OK2.rt = _OK2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mainInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mainInstruct"-------
for thisComponent in mainInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr2.started', instr2.tStartRefresh)
thisExp.addData('instr2.stopped', instr2.tStopRefresh)
# check responses
if OK2.keys in ['', [], None]:  # No response was made
    OK2.keys = None
thisExp.addData('OK2.keys',OK2.keys)
if OK2.keys != None:  # we had a response
    thisExp.addData('OK2.rt', OK2.rt)
thisExp.addData('OK2.started', OK2.tStartRefresh)
thisExp.addData('OK2.stopped', OK2.tStopRefresh)
thisExp.nextEntry()
# the Routine "mainInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mainTrials.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    presentSet.setText(numberSet)
    presentTarget.setText(target)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixation, presentSet, presentTarget, resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *presentSet* updates
        if presentSet.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
            # keep track of start time/frame for later
            presentSet.frameNStart = frameN  # exact frame index
            presentSet.tStart = t  # local t and not account for scr refresh
            presentSet.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presentSet, 'tStartRefresh')  # time at next scr refresh
            presentSet.setAutoDraw(True)
        if presentSet.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > presentSet.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                presentSet.tStop = t  # not accounting for scr refresh
                presentSet.frameNStop = frameN  # exact frame index
                win.timeOnFlip(presentSet, 'tStopRefresh')  # time at next scr refresh
                presentSet.setAutoDraw(False)
        
        # *presentTarget* updates
        if presentTarget.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
            # keep track of start time/frame for later
            presentTarget.frameNStart = frameN  # exact frame index
            presentTarget.tStart = t  # local t and not account for scr refresh
            presentTarget.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presentTarget, 'tStartRefresh')  # time at next scr refresh
            presentTarget.setAutoDraw(True)
        if presentTarget.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > presentTarget.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                presentTarget.tStop = t  # not accounting for scr refresh
                presentTarget.frameNStop = frameN  # exact frame index
                win.timeOnFlip(presentTarget, 'tStopRefresh')  # time at next scr refresh
                presentTarget.setAutoDraw(False)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                resp.rt = _resp_allKeys[-1].rt
                # was this correct?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixation.started', fixation.tStartRefresh)
    trials.addData('fixation.stopped', fixation.tStopRefresh)
    trials.addData('presentSet.started', presentSet.tStartRefresh)
    trials.addData('presentSet.stopped', presentSet.tStopRefresh)
    trials.addData('presentTarget.started', presentTarget.tStartRefresh)
    trials.addData('presentTarget.stopped', presentTarget.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp.keys',resp.keys)
    trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    trials.addData('resp.started', resp.tStartRefresh)
    trials.addData('resp.stopped', resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
