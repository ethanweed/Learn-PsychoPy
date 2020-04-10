﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Fri Apr 10 09:26:52 2020
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
expName = 'pseudohomsA'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/ethan/Documents/GitHub/Learn-PsychoPy/fork of C81MPR_new/for lecturers/Lab4_pseudohomophones/experiment/pseudohomsA_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text="OK, ready for the real thing?\n\nPress 'up' or 'down' keys to indicate which is the real word\n\nPress an key to begin",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mainTrialsStart = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
upperStim = visual.TextStim(win=win, name='upperStim',
    text='default text',
    font='Arial',
    units='norm', pos=[0, +0.2], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
lowerStim = visual.TextStim(win=win, name='lowerStim',
    text='default text',
    font='Arial',
    pos=[0, -0.2], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
upperStim = visual.TextStim(win=win, name='upperStim',
    text='default text',
    font='Arial',
    units='norm', pos=[0, +0.2], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
lowerStim = visual.TextStim(win=win, name='lowerStim',
    text='default text',
    font='Arial',
    pos=[0, -0.2], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
mainTrialsStart.keys = []
mainTrialsStart.rt = []
_mainTrialsStart_allKeys = []
# keep track of which components have finished
instrComponents = [instructions, mainTrialsStart]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *mainTrialsStart* updates
    waitOnFlip = False
    if mainTrialsStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mainTrialsStart.frameNStart = frameN  # exact frame index
        mainTrialsStart.tStart = t  # local t and not account for scr refresh
        mainTrialsStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mainTrialsStart, 'tStartRefresh')  # time at next scr refresh
        mainTrialsStart.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(mainTrialsStart.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(mainTrialsStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if mainTrialsStart.status == STARTED and not waitOnFlip:
        theseKeys = mainTrialsStart.getKeys(keyList=None, waitRelease=False)
        _mainTrialsStart_allKeys.extend(theseKeys)
        if len(_mainTrialsStart_allKeys):
            mainTrialsStart.keys = _mainTrialsStart_allKeys[-1].name  # just the last key pressed
            mainTrialsStart.rt = _mainTrialsStart_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
# check responses
if mainTrialsStart.keys in ['', [], None]:  # No response was made
    mainTrialsStart.keys = None
thisExp.addData('mainTrialsStart.keys',mainTrialsStart.keys)
if mainTrialsStart.keys != None:  # we had a response
    thisExp.addData('mainTrialsStart.rt', mainTrialsStart.rt)
thisExp.addData('mainTrialsStart.started', mainTrialsStart.tStartRefresh)
thisExp.addData('mainTrialsStart.stopped', mainTrialsStart.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
training = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trainingA.xlsx'),
    seed=None, name='training')
thisExp.addLoop(training)  # add the loop to the experiment
thisTraining = training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
if thisTraining != None:
    for paramName in thisTraining:
        exec('{} = thisTraining[paramName]'.format(paramName))

for thisTraining in training:
    currentLoop = training
    # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
    if thisTraining != None:
        for paramName in thisTraining:
            exec('{} = thisTraining[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    upperStim.setText(upperWord)
    lowerStim.setText(lowerWord)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixation, upperStim, lowerStim, key_resp]
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
    while continueRoutine and routineTimer.getTime() > 0:
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
            if tThisFlipGlobal > fixation.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *upperStim* updates
        if upperStim.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            upperStim.frameNStart = frameN  # exact frame index
            upperStim.tStart = t  # local t and not account for scr refresh
            upperStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperStim, 'tStartRefresh')  # time at next scr refresh
            upperStim.setAutoDraw(True)
        if upperStim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > upperStim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                upperStim.tStop = t  # not accounting for scr refresh
                upperStim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(upperStim, 'tStopRefresh')  # time at next scr refresh
                upperStim.setAutoDraw(False)
        
        # *lowerStim* updates
        if lowerStim.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            lowerStim.frameNStart = frameN  # exact frame index
            lowerStim.tStart = t  # local t and not account for scr refresh
            lowerStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lowerStim, 'tStartRefresh')  # time at next scr refresh
            lowerStim.setAutoDraw(True)
        if lowerStim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lowerStim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                lowerStim.tStop = t  # not accounting for scr refresh
                lowerStim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lowerStim, 'tStopRefresh')  # time at next scr refresh
                lowerStim.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['up', 'down'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
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
    training.addData('fixation.started', fixation.tStartRefresh)
    training.addData('fixation.stopped', fixation.tStopRefresh)
    training.addData('upperStim.started', upperStim.tStartRefresh)
    training.addData('upperStim.stopped', upperStim.tStopRefresh)
    training.addData('lowerStim.started', lowerStim.tStartRefresh)
    training.addData('lowerStim.stopped', lowerStim.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for training (TrialHandler)
    training.addData('key_resp.keys',key_resp.keys)
    training.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        training.addData('key_resp.rt', key_resp.rt)
    training.addData('key_resp.started', key_resp.tStartRefresh)
    training.addData('key_resp.stopped', key_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'training'

# get names of stimulus parameters
if training.trialList in ([], [None], None):
    params = []
else:
    params = training.trialList[0].keys()
# save data for this loop
training.saveAsExcel(filename + '.xlsx', sheetName='training',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
testing = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('testing.xlsx'),
    seed=None, name='testing')
thisExp.addLoop(testing)  # add the loop to the experiment
thisTesting = testing.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTesting.rgb)
if thisTesting != None:
    for paramName in thisTesting:
        exec('{} = thisTesting[paramName]'.format(paramName))

for thisTesting in testing:
    currentLoop = testing
    # abbreviate parameter names if possible (e.g. rgb = thisTesting.rgb)
    if thisTesting != None:
        for paramName in thisTesting:
            exec('{} = thisTesting[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    upperStim.setText(upperWord)
    lowerStim.setText(lowerWord)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixation, upperStim, lowerStim, key_resp]
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
    while continueRoutine and routineTimer.getTime() > 0:
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
            if tThisFlipGlobal > fixation.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *upperStim* updates
        if upperStim.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            upperStim.frameNStart = frameN  # exact frame index
            upperStim.tStart = t  # local t and not account for scr refresh
            upperStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperStim, 'tStartRefresh')  # time at next scr refresh
            upperStim.setAutoDraw(True)
        if upperStim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > upperStim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                upperStim.tStop = t  # not accounting for scr refresh
                upperStim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(upperStim, 'tStopRefresh')  # time at next scr refresh
                upperStim.setAutoDraw(False)
        
        # *lowerStim* updates
        if lowerStim.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            lowerStim.frameNStart = frameN  # exact frame index
            lowerStim.tStart = t  # local t and not account for scr refresh
            lowerStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lowerStim, 'tStartRefresh')  # time at next scr refresh
            lowerStim.setAutoDraw(True)
        if lowerStim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lowerStim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                lowerStim.tStop = t  # not accounting for scr refresh
                lowerStim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lowerStim, 'tStopRefresh')  # time at next scr refresh
                lowerStim.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['up', 'down'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
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
    testing.addData('fixation.started', fixation.tStartRefresh)
    testing.addData('fixation.stopped', fixation.tStopRefresh)
    testing.addData('upperStim.started', upperStim.tStartRefresh)
    testing.addData('upperStim.stopped', upperStim.tStopRefresh)
    testing.addData('lowerStim.started', lowerStim.tStartRefresh)
    testing.addData('lowerStim.stopped', lowerStim.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for testing (TrialHandler)
    testing.addData('key_resp.keys',key_resp.keys)
    testing.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        testing.addData('key_resp.rt', key_resp.rt)
    testing.addData('key_resp.started', key_resp.tStartRefresh)
    testing.addData('key_resp.stopped', key_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'testing'

# get names of stimulus parameters
if testing.trialList in ([], [None], None):
    params = []
else:
    params = testing.trialList[0].keys()
# save data for this loop
testing.saveAsExcel(filename + '.xlsx', sheetName='testing',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
