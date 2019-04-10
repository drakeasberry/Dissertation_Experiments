#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.5),
    on Tue Apr  9 22:23:06 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.5'
expName = 'blp'  # from the Builder filename that created this script
expInfo = {'idioma': ['', 'español', 'inglés'], '08_Idioma preferida (Preferred language):': ['', 'español', 'inglés'], '09_Participante (Participant):': 'part000', '05_País de nacimiento (Birth country):': ['', 'México', 'Estados Unidos'], '03_Edad (Age):': '', '07_Nivel más alto de formación académica (Highest level of formal education):': ['', 'Menos de la escuela secundaria', 'Escuela Secundaria', 'Un poco de universidad', 'Universidad (diplomatura, licenciatura)', 'Un poco de escuela graduada', 'Máster', 'Doctorado'], '04_Sexo (Gender):': ['', 'Hombre', 'Mujer'], '02_Apellido (Last name):': '', '01_Nombre (First name):': '', '06_Lugar de residencia (Place of residence):': ['', 'Tucson', 'Hermosillo']}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['09_Participante (Participant):'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/drakeasberry/github/Dissertation/Dissertation_Experiments/basicLangProfile/blp_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
tmp = expInfo['08_Idioma preferida (Preferred language):']
lang = tmp[0]

if 'e' == lang:
    preferLang = 'spanish'
    section = 'sectionEsp'
    questionText = 'questionTextEsp'
    language = 'languageEsp'
    instructions = 'Nos gustaría pedir su ayuda para contestar a las siguientes preguntas sobre su historial lingüístico, uso, actitudes y competencia. Esta encuesta ha sido creada con el apoyo del "Center for Open Educational Resources and Language Learning" de la Universidad de Texas en Austin para poder tener un mayor conocimiento sobre los perfiles de hablantes bilingües independientemente de sus diversos orígenes y en diferentes contextos. La encuesta contiene 19 preguntas y le llevará menos de 10 minutos para completar. Esto no es una prueba, por tanto no hay respuestas correctas ni incorrectas. Por favor conteste cada pregunta y responda con sinceridad, ya que solamente así se podrá garantizar el éxito de esta investigación. Muchas gracias por su ayuda.\n\nPresione el botón "blanco" para continuar.'
    langHist = 'Historial lingüístico\n\nEn esta sección, nos gustaría que contestara algunas preguntas sobre su historial lingüístico marcando la casilla apropiada.\n\nPresione el botón "blanco" para continuar.'
    langUse = 'Uso de lenguas\n\nEn esta sección, nos gustaría que contestara algunas preguntas sobre su uso de lenguas marcando la casilla apropiada. El uso total de todas las preguntas en cada pregunta debe llegar al 100%.\n\nPresione el botón "blanco" para continuar.'
    langProf = 'Competencia\n\nEn esta sección, nos gustaría que considerara su competencia de lengua marcando la casilla de 0 a 6.\n\nPresione el botón "blanco" para continuar.'
    langAtt = 'Actitudes\n\nEn esta sección, nos gustaría que contestara a las siguientes afirmaciones sobre actitudes lingüísticas marcando las casillas de 0 a 6.\n\nPresione el botón "blanco" para continuar.'
    labHist1 = 'Desde el Nacimiento,20+'
    #labUse
    #labProf
    #labAtt
elif 'i' == lang:
    preferLang = 'english'
    section = 'sectionEng'
    questionText = 'questionTextEng'
    language = 'languageEng'
    instructions = 'We would like to ask you to help us by answering the following questions concerning your language history, use, attitudes, and proficiency. This survey was created with support from the Center for Open Educational Resources and Language Learning at the University of Texas at Austin to better understand the profiles of bilingual speakers in diverse settings with diverse backgrounds. The survey consists of 19 questions and will take less than 10 minutes to complete. This is not a test, so there are no right or wrong answers. Please answer every question and give your answers sincerely. Thank you very much for your help.\n\nPress the "white" button to continue'
    langHist = 'Language history\n\nIn this section, we would like you to answer some factual questions about your language history by placing a check in the appropriate box.\n\nPress the "white" button to begin.'
    langUse = 'Language use\n\nIn this section, we would like you to answer some questions about your language use by placing a check in the appropriate box. Total use for all languages in a given question should equal 100%.\n\nPress the "white" button to begin.'
    langProf = 'Language proficiency\n\nIn this section, we would like you to rate your language proficiency by giving marks from 0 to 6.\n\nPress the "white" button to begin.'
    langAtt = 'Language attitudes\n\nIn this section, we would like you to respond to statements about language attitudes by giving marks from 0-6.\n\nPress the spacebar to begin.'
    labHist1 = 'Since birth,20+'
else:
    instructions = 'Por favor, hable con el investigador.\n\nPlease talk to the experimenter.'

text_instructions = visual.TextStim(win=win, name='text_instructions',
    text=instructions,
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "lang_hist_ins"
lang_hist_insClock = core.Clock()
text_lang_his_ins = visual.TextStim(win=win, name='text_lang_his_ins',
    text=langHist,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "language_history"
language_historyClock = core.Clock()
text_section_lang_hist = visual.TextStim(win=win, name='text_section_lang_hist',
    text='default text',
    font='Arial',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_lang_hist_question = visual.TextStim(win=win, name='text_lang_hist_question',
    text='default text',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_lang_hist_lang = visual.TextStim(win=win, name='text_lang_hist_lang',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_lang_hist_qnum = visual.TextStim(win=win, name='text_lang_hist_qnum',
    text='default text',
    font='Arial',
    pos=(-0.9, 0.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rating_lang_hist = visual.RatingScale(win=win, name='rating_lang_hist', marker='triangle', size=1.5, pos=[0.0, -0.3], low=0, high=20, labels=['$labHist1'], scale='', markerStart='10')

# Initialize components for Routine "language_history_2"
language_history_2Clock = core.Clock()
text_section_lang_hist_2 = visual.TextStim(win=win, name='text_section_lang_hist_2',
    text='default text',
    font='Arial',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_lang_hist_question_2 = visual.TextStim(win=win, name='text_lang_hist_question_2',
    text='default text',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_lang_hist_lang_2 = visual.TextStim(win=win, name='text_lang_hist_lang_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_lang_hist_qnum_2 = visual.TextStim(win=win, name='text_lang_hist_qnum_2',
    text='default text',
    font='Arial',
    pos=(-0.9, 0.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rating_lang_hist_2 = visual.RatingScale(win=win, name='rating_lang_hist_2', marker='triangle', size=1.5, pos=[0.0, -0.3], low=0, high=20, labels=['0', ' 10', ' 20'], scale='', markerStart='10')

# Initialize components for Routine "language_history_3"
language_history_3Clock = core.Clock()
text_section_lang_hist_3 = visual.TextStim(win=win, name='text_section_lang_hist_3',
    text='default text',
    font='Arial',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_lang_hist_question_3 = visual.TextStim(win=win, name='text_lang_hist_question_3',
    text='default text',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_lang_hist_lang_3 = visual.TextStim(win=win, name='text_lang_hist_lang_3',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_lang_hist_qnum_3 = visual.TextStim(win=win, name='text_lang_hist_qnum_3',
    text='default text',
    font='Arial',
    pos=(-0.9, 0.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rating_lang_hist_3 = visual.RatingScale(win=win, name='rating_lang_hist_3', marker='triangle', size=1.5, pos=[0.0, -0.3], low=0, high=20, labels=['0', ' 10', ' 20+'], scale='', markerStart='10')

# Initialize components for Routine "lang_use_ins"
lang_use_insClock = core.Clock()
text_lang_use_ins = visual.TextStim(win=win, name='text_lang_use_ins',
    text=langUse,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "language_use"
language_useClock = core.Clock()
text_section_lang_use = visual.TextStim(win=win, name='text_section_lang_use',
    text='default text',
    font='Arial',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_lang_use_question = visual.TextStim(win=win, name='text_lang_use_question',
    text='default text',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_lang_use_lang = visual.TextStim(win=win, name='text_lang_use_lang',
    text='default text',
    font='Arial',
    pos=(0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_lang_use_qnum = visual.TextStim(win=win, name='text_lang_use_qnum',
    text='default text',
    font='Arial',
    pos=(-0.9, 0.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rating_lang_use = visual.RatingScale(win=win, name='rating_lang_use', marker='triangle', size=1.5, pos=[0.0, -0.1], choices=['0', '10', '20', '40', '50', '60', '70', '80', '90', '100'], tickHeight=-1, markerStart='50')

# Initialize components for Routine "lang_prof_ins"
lang_prof_insClock = core.Clock()
text_lang_prof_ins = visual.TextStim(win=win, name='text_lang_prof_ins',
    text=langProf,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "language_proficiency"
language_proficiencyClock = core.Clock()
text_section_lang_prof = visual.TextStim(win=win, name='text_section_lang_prof',
    text='default text',
    font='Arial',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_lang_prof_question = visual.TextStim(win=win, name='text_lang_prof_question',
    text='default text',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_lang_prof_lang = visual.TextStim(win=win, name='text_lang_prof_lang',
    text='default text',
    font='Arial',
    pos=(0.0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_lang_prof_qnum = visual.TextStim(win=win, name='text_lang_prof_qnum',
    text='default text',
    font='Arial',
    pos=(-0.9, 0.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rating_lang_prof = visual.RatingScale(win=win, name='rating_lang_prof', marker='triangle', size=1.5, pos=[0.0, -0.1], choices=['0', '1', '2', '3', '4', '5', '6'], tickHeight=-1, markerStart='3')

# Initialize components for Routine "lang_att_ins"
lang_att_insClock = core.Clock()
text_lang_att_ins = visual.TextStim(win=win, name='text_lang_att_ins',
    text=langAtt,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "language_attitudes"
language_attitudesClock = core.Clock()
text_lang_att_section = visual.TextStim(win=win, name='text_lang_att_section',
    text='default text',
    font='Arial',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_lang_att_ques = visual.TextStim(win=win, name='text_lang_att_ques',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_lang_att_qnum = visual.TextStim(win=win, name='text_lang_att_qnum',
    text='default text',
    font='Arial',
    pos=(-0.9, 0.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rating_lang_att = visual.RatingScale(win=win, name='rating_lang_att', marker='triangle', size=1.5, pos=[0.0, 0.0], choices=['0', '1', '2', '3', '4', '5', '6'], tickHeight=-1, markerStart='3')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

key_resp_instructions = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [text_instructions, key_resp_instructions]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *text_instructions* updates
    if t >= 0.0 and text_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions.tStart = t
        text_instructions.frameNStart = frameN  # exact frame index
        text_instructions.setAutoDraw(True)
    
    # *key_resp_instructions* updates
    if t >= 0.0 and key_resp_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_instructions.tStart = t
        key_resp_instructions.frameNStart = frameN  # exact frame index
        key_resp_instructions.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_instructions.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "lang_hist_ins"-------
t = 0
lang_hist_insClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_lang_hist = event.BuilderKeyResponse()
# keep track of which components have finished
lang_hist_insComponents = [text_lang_his_ins, key_resp_lang_hist]
for thisComponent in lang_hist_insComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "lang_hist_ins"-------
while continueRoutine:
    # get current time
    t = lang_hist_insClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_lang_his_ins* updates
    if t >= 0.0 and text_lang_his_ins.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_lang_his_ins.tStart = t
        text_lang_his_ins.frameNStart = frameN  # exact frame index
        text_lang_his_ins.setAutoDraw(True)
    
    # *key_resp_lang_hist* updates
    if t >= 0.0 and key_resp_lang_hist.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_lang_hist.tStart = t
        key_resp_lang_hist.frameNStart = frameN  # exact frame index
        key_resp_lang_hist.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_lang_hist.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in lang_hist_insComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "lang_hist_ins"-------
for thisComponent in lang_hist_insComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "lang_hist_ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_hist_1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_file/sp_en_trials.csv', selection='0'),
    seed=None, name='trials_hist_1')
thisExp.addLoop(trials_hist_1)  # add the loop to the experiment
thisTrials_hist_1 = trials_hist_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_hist_1.rgb)
if thisTrials_hist_1 != None:
    for paramName in thisTrials_hist_1:
        exec('{} = thisTrials_hist_1[paramName]'.format(paramName))

for thisTrials_hist_1 in trials_hist_1:
    currentLoop = trials_hist_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_hist_1.rgb)
    if thisTrials_hist_1 != None:
        for paramName in thisTrials_hist_1:
            exec('{} = thisTrials_hist_1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "language_history"-------
    t = 0
    language_historyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_section_lang_hist.setText(eval(section)
)
    text_lang_hist_question.setText(eval(questionText))
    text_lang_hist_lang.setColor(color, colorSpace='rgb')
    text_lang_hist_lang.setText(eval(language))
    text_lang_hist_qnum.setText(questionNum)
    rating_lang_hist.reset()
    # keep track of which components have finished
    language_historyComponents = [text_section_lang_hist, text_lang_hist_question, text_lang_hist_lang, text_lang_hist_qnum, rating_lang_hist]
    for thisComponent in language_historyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "language_history"-------
    while continueRoutine:
        # get current time
        t = language_historyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_section_lang_hist* updates
        if t >= 0.0 and text_section_lang_hist.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_section_lang_hist.tStart = t
            text_section_lang_hist.frameNStart = frameN  # exact frame index
            text_section_lang_hist.setAutoDraw(True)
        
        # *text_lang_hist_question* updates
        if t >= 0.0 and text_lang_hist_question.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_hist_question.tStart = t
            text_lang_hist_question.frameNStart = frameN  # exact frame index
            text_lang_hist_question.setAutoDraw(True)
        
        # *text_lang_hist_lang* updates
        if t >= 0.0 and text_lang_hist_lang.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_hist_lang.tStart = t
            text_lang_hist_lang.frameNStart = frameN  # exact frame index
            text_lang_hist_lang.setAutoDraw(True)
        
        # *text_lang_hist_qnum* updates
        if t >= 0.0 and text_lang_hist_qnum.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_hist_qnum.tStart = t
            text_lang_hist_qnum.frameNStart = frameN  # exact frame index
            text_lang_hist_qnum.setAutoDraw(True)
        # *rating_lang_hist* updates
        if t >= 0.0 and rating_lang_hist.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_lang_hist.tStart = t
            rating_lang_hist.frameNStart = frameN  # exact frame index
            rating_lang_hist.setAutoDraw(True)
        continueRoutine &= rating_lang_hist.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in language_historyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "language_history"-------
    for thisComponent in language_historyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_hist_1 (TrialHandler)
    trials_hist_1.addData('rating_lang_hist.response', rating_lang_hist.getRating())
    trials_hist_1.addData('rating_lang_hist.rt', rating_lang_hist.getRT())
    # the Routine "language_history" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_hist_1'


# set up handler to look after randomisation of conditions etc
trials_hist_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_file/sp_en_trials.csv', selection='1'),
    seed=None, name='trials_hist_2')
thisExp.addLoop(trials_hist_2)  # add the loop to the experiment
thisTrials_hist_2 = trials_hist_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_hist_2.rgb)
if thisTrials_hist_2 != None:
    for paramName in thisTrials_hist_2:
        exec('{} = thisTrials_hist_2[paramName]'.format(paramName))

for thisTrials_hist_2 in trials_hist_2:
    currentLoop = trials_hist_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_hist_2.rgb)
    if thisTrials_hist_2 != None:
        for paramName in thisTrials_hist_2:
            exec('{} = thisTrials_hist_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "language_history_2"-------
    t = 0
    language_history_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_section_lang_hist_2.setText(eval(section)
)
    text_lang_hist_question_2.setText(eval(questionText))
    text_lang_hist_lang_2.setColor(color, colorSpace='rgb')
    text_lang_hist_lang_2.setText(eval(language))
    text_lang_hist_qnum_2.setText(questionNum)
    rating_lang_hist_2.reset()
    # keep track of which components have finished
    language_history_2Components = [text_section_lang_hist_2, text_lang_hist_question_2, text_lang_hist_lang_2, text_lang_hist_qnum_2, rating_lang_hist_2]
    for thisComponent in language_history_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "language_history_2"-------
    while continueRoutine:
        # get current time
        t = language_history_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_section_lang_hist_2* updates
        if t >= 0.0 and text_section_lang_hist_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_section_lang_hist_2.tStart = t
            text_section_lang_hist_2.frameNStart = frameN  # exact frame index
            text_section_lang_hist_2.setAutoDraw(True)
        
        # *text_lang_hist_question_2* updates
        if t >= 0.0 and text_lang_hist_question_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_hist_question_2.tStart = t
            text_lang_hist_question_2.frameNStart = frameN  # exact frame index
            text_lang_hist_question_2.setAutoDraw(True)
        
        # *text_lang_hist_lang_2* updates
        if t >= 0.0 and text_lang_hist_lang_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_hist_lang_2.tStart = t
            text_lang_hist_lang_2.frameNStart = frameN  # exact frame index
            text_lang_hist_lang_2.setAutoDraw(True)
        
        # *text_lang_hist_qnum_2* updates
        if t >= 0.0 and text_lang_hist_qnum_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_hist_qnum_2.tStart = t
            text_lang_hist_qnum_2.frameNStart = frameN  # exact frame index
            text_lang_hist_qnum_2.setAutoDraw(True)
        # *rating_lang_hist_2* updates
        if t >= 0.0 and rating_lang_hist_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_lang_hist_2.tStart = t
            rating_lang_hist_2.frameNStart = frameN  # exact frame index
            rating_lang_hist_2.setAutoDraw(True)
        continueRoutine &= rating_lang_hist_2.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in language_history_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "language_history_2"-------
    for thisComponent in language_history_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_hist_2 (TrialHandler)
    trials_hist_2.addData('rating_lang_hist_2.response', rating_lang_hist_2.getRating())
    trials_hist_2.addData('rating_lang_hist_2.rt', rating_lang_hist_2.getRT())
    # the Routine "language_history_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_hist_2'


# set up handler to look after randomisation of conditions etc
trials_hist_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_file/sp_en_trials.csv', selection='2:12'),
    seed=None, name='trials_hist_3')
thisExp.addLoop(trials_hist_3)  # add the loop to the experiment
thisTrials_hist_3 = trials_hist_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_hist_3.rgb)
if thisTrials_hist_3 != None:
    for paramName in thisTrials_hist_3:
        exec('{} = thisTrials_hist_3[paramName]'.format(paramName))

for thisTrials_hist_3 in trials_hist_3:
    currentLoop = trials_hist_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_hist_3.rgb)
    if thisTrials_hist_3 != None:
        for paramName in thisTrials_hist_3:
            exec('{} = thisTrials_hist_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "language_history_3"-------
    t = 0
    language_history_3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_section_lang_hist_3.setText(eval(section)
)
    text_lang_hist_question_3.setText(eval(questionText))
    text_lang_hist_lang_3.setColor(color, colorSpace='rgb')
    text_lang_hist_lang_3.setText(eval(language))
    text_lang_hist_qnum_3.setText(questionNum)
    rating_lang_hist_3.reset()
    # keep track of which components have finished
    language_history_3Components = [text_section_lang_hist_3, text_lang_hist_question_3, text_lang_hist_lang_3, text_lang_hist_qnum_3, rating_lang_hist_3]
    for thisComponent in language_history_3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "language_history_3"-------
    while continueRoutine:
        # get current time
        t = language_history_3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_section_lang_hist_3* updates
        if t >= 0.0 and text_section_lang_hist_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_section_lang_hist_3.tStart = t
            text_section_lang_hist_3.frameNStart = frameN  # exact frame index
            text_section_lang_hist_3.setAutoDraw(True)
        
        # *text_lang_hist_question_3* updates
        if t >= 0.0 and text_lang_hist_question_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_hist_question_3.tStart = t
            text_lang_hist_question_3.frameNStart = frameN  # exact frame index
            text_lang_hist_question_3.setAutoDraw(True)
        
        # *text_lang_hist_lang_3* updates
        if t >= 0.0 and text_lang_hist_lang_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_hist_lang_3.tStart = t
            text_lang_hist_lang_3.frameNStart = frameN  # exact frame index
            text_lang_hist_lang_3.setAutoDraw(True)
        
        # *text_lang_hist_qnum_3* updates
        if t >= 0.0 and text_lang_hist_qnum_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_hist_qnum_3.tStart = t
            text_lang_hist_qnum_3.frameNStart = frameN  # exact frame index
            text_lang_hist_qnum_3.setAutoDraw(True)
        # *rating_lang_hist_3* updates
        if t >= 0.0 and rating_lang_hist_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_lang_hist_3.tStart = t
            rating_lang_hist_3.frameNStart = frameN  # exact frame index
            rating_lang_hist_3.setAutoDraw(True)
        continueRoutine &= rating_lang_hist_3.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in language_history_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "language_history_3"-------
    for thisComponent in language_history_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_hist_3 (TrialHandler)
    trials_hist_3.addData('rating_lang_hist_3.response', rating_lang_hist_3.getRating())
    trials_hist_3.addData('rating_lang_hist_3.rt', rating_lang_hist_3.getRT())
    # the Routine "language_history_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_hist_3'


# ------Prepare to start Routine "lang_use_ins"-------
t = 0
lang_use_insClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_lang_use = event.BuilderKeyResponse()
# keep track of which components have finished
lang_use_insComponents = [text_lang_use_ins, key_resp_lang_use]
for thisComponent in lang_use_insComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "lang_use_ins"-------
while continueRoutine:
    # get current time
    t = lang_use_insClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_lang_use_ins* updates
    if t >= 0.0 and text_lang_use_ins.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_lang_use_ins.tStart = t
        text_lang_use_ins.frameNStart = frameN  # exact frame index
        text_lang_use_ins.setAutoDraw(True)
    
    # *key_resp_lang_use* updates
    if t >= 0.0 and key_resp_lang_use.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_lang_use.tStart = t
        key_resp_lang_use.frameNStart = frameN  # exact frame index
        key_resp_lang_use.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_lang_use.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in lang_use_insComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "lang_use_ins"-------
for thisComponent in lang_use_insComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "lang_use_ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_use = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_file/sp_en_trials.csv', selection='12:27'),
    seed=None, name='trials_use')
thisExp.addLoop(trials_use)  # add the loop to the experiment
thisTrials_use = trials_use.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_use.rgb)
if thisTrials_use != None:
    for paramName in thisTrials_use:
        exec('{} = thisTrials_use[paramName]'.format(paramName))

for thisTrials_use in trials_use:
    currentLoop = trials_use
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_use.rgb)
    if thisTrials_use != None:
        for paramName in thisTrials_use:
            exec('{} = thisTrials_use[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "language_use"-------
    t = 0
    language_useClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_section_lang_use.setText(eval(section))
    text_lang_use_question.setText(eval(questionText))
    text_lang_use_lang.setColor(color, colorSpace='rgb')
    text_lang_use_lang.setText(eval(language))
    text_lang_use_qnum.setText(questionNum)
    rating_lang_use.reset()
    # keep track of which components have finished
    language_useComponents = [text_section_lang_use, text_lang_use_question, text_lang_use_lang, text_lang_use_qnum, rating_lang_use]
    for thisComponent in language_useComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "language_use"-------
    while continueRoutine:
        # get current time
        t = language_useClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_section_lang_use* updates
        if t >= 0.0 and text_section_lang_use.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_section_lang_use.tStart = t
            text_section_lang_use.frameNStart = frameN  # exact frame index
            text_section_lang_use.setAutoDraw(True)
        
        # *text_lang_use_question* updates
        if t >= 0.0 and text_lang_use_question.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_use_question.tStart = t
            text_lang_use_question.frameNStart = frameN  # exact frame index
            text_lang_use_question.setAutoDraw(True)
        
        # *text_lang_use_lang* updates
        if t >= 0.0 and text_lang_use_lang.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_use_lang.tStart = t
            text_lang_use_lang.frameNStart = frameN  # exact frame index
            text_lang_use_lang.setAutoDraw(True)
        
        # *text_lang_use_qnum* updates
        if t >= 0.0 and text_lang_use_qnum.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_use_qnum.tStart = t
            text_lang_use_qnum.frameNStart = frameN  # exact frame index
            text_lang_use_qnum.setAutoDraw(True)
        # *rating_lang_use* updates
        if t >= 0.0 and rating_lang_use.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_lang_use.tStart = t
            rating_lang_use.frameNStart = frameN  # exact frame index
            rating_lang_use.setAutoDraw(True)
        continueRoutine &= rating_lang_use.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in language_useComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "language_use"-------
    for thisComponent in language_useComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_use (TrialHandler)
    trials_use.addData('rating_lang_use.response', rating_lang_use.getRating())
    trials_use.addData('rating_lang_use.rt', rating_lang_use.getRT())
    # the Routine "language_use" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_use'


# ------Prepare to start Routine "lang_prof_ins"-------
t = 0
lang_prof_insClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_lang_prof_ins = event.BuilderKeyResponse()
# keep track of which components have finished
lang_prof_insComponents = [text_lang_prof_ins, key_resp_lang_prof_ins]
for thisComponent in lang_prof_insComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "lang_prof_ins"-------
while continueRoutine:
    # get current time
    t = lang_prof_insClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_lang_prof_ins* updates
    if t >= 0.0 and text_lang_prof_ins.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_lang_prof_ins.tStart = t
        text_lang_prof_ins.frameNStart = frameN  # exact frame index
        text_lang_prof_ins.setAutoDraw(True)
    
    # *key_resp_lang_prof_ins* updates
    if t >= 0.0 and key_resp_lang_prof_ins.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_lang_prof_ins.tStart = t
        key_resp_lang_prof_ins.frameNStart = frameN  # exact frame index
        key_resp_lang_prof_ins.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_lang_prof_ins.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in lang_prof_insComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "lang_prof_ins"-------
for thisComponent in lang_prof_insComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "lang_prof_ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_prof = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_file/sp_en_trials.csv', selection='27:35'),
    seed=None, name='trials_prof')
thisExp.addLoop(trials_prof)  # add the loop to the experiment
thisTrials_prof = trials_prof.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_prof.rgb)
if thisTrials_prof != None:
    for paramName in thisTrials_prof:
        exec('{} = thisTrials_prof[paramName]'.format(paramName))

for thisTrials_prof in trials_prof:
    currentLoop = trials_prof
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_prof.rgb)
    if thisTrials_prof != None:
        for paramName in thisTrials_prof:
            exec('{} = thisTrials_prof[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "language_proficiency"-------
    t = 0
    language_proficiencyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_section_lang_prof.setText(eval(section))
    text_lang_prof_question.setText(eval(questionText))
    text_lang_prof_lang.setColor(color, colorSpace='rgb')
    text_lang_prof_lang.setText(eval(language))
    text_lang_prof_qnum.setText(questionNum)
    rating_lang_prof.reset()
    # keep track of which components have finished
    language_proficiencyComponents = [text_section_lang_prof, text_lang_prof_question, text_lang_prof_lang, text_lang_prof_qnum, rating_lang_prof]
    for thisComponent in language_proficiencyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "language_proficiency"-------
    while continueRoutine:
        # get current time
        t = language_proficiencyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_section_lang_prof* updates
        if t >= 0.0 and text_section_lang_prof.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_section_lang_prof.tStart = t
            text_section_lang_prof.frameNStart = frameN  # exact frame index
            text_section_lang_prof.setAutoDraw(True)
        
        # *text_lang_prof_question* updates
        if t >= 0.0 and text_lang_prof_question.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_prof_question.tStart = t
            text_lang_prof_question.frameNStart = frameN  # exact frame index
            text_lang_prof_question.setAutoDraw(True)
        
        # *text_lang_prof_lang* updates
        if t >= 0.0 and text_lang_prof_lang.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_prof_lang.tStart = t
            text_lang_prof_lang.frameNStart = frameN  # exact frame index
            text_lang_prof_lang.setAutoDraw(True)
        
        # *text_lang_prof_qnum* updates
        if t >= 0.0 and text_lang_prof_qnum.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_prof_qnum.tStart = t
            text_lang_prof_qnum.frameNStart = frameN  # exact frame index
            text_lang_prof_qnum.setAutoDraw(True)
        # *rating_lang_prof* updates
        if t >= 0.0 and rating_lang_prof.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_lang_prof.tStart = t
            rating_lang_prof.frameNStart = frameN  # exact frame index
            rating_lang_prof.setAutoDraw(True)
        continueRoutine &= rating_lang_prof.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in language_proficiencyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "language_proficiency"-------
    for thisComponent in language_proficiencyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_prof (TrialHandler)
    trials_prof.addData('rating_lang_prof.response', rating_lang_prof.getRating())
    trials_prof.addData('rating_lang_prof.rt', rating_lang_prof.getRT())
    # the Routine "language_proficiency" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_prof'


# ------Prepare to start Routine "lang_att_ins"-------
t = 0
lang_att_insClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_lang_att_ins = event.BuilderKeyResponse()
# keep track of which components have finished
lang_att_insComponents = [text_lang_att_ins, key_resp_lang_att_ins]
for thisComponent in lang_att_insComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "lang_att_ins"-------
while continueRoutine:
    # get current time
    t = lang_att_insClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_lang_att_ins* updates
    if t >= 0.0 and text_lang_att_ins.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_lang_att_ins.tStart = t
        text_lang_att_ins.frameNStart = frameN  # exact frame index
        text_lang_att_ins.setAutoDraw(True)
    
    # *key_resp_lang_att_ins* updates
    if t >= 0.0 and key_resp_lang_att_ins.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_lang_att_ins.tStart = t
        key_resp_lang_att_ins.frameNStart = frameN  # exact frame index
        key_resp_lang_att_ins.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_lang_att_ins.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in lang_att_insComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "lang_att_ins"-------
for thisComponent in lang_att_insComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "lang_att_ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_att = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_file/sp_en_trials.csv', selection='35:43'),
    seed=None, name='trials_att')
thisExp.addLoop(trials_att)  # add the loop to the experiment
thisTrials_att = trials_att.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_att.rgb)
if thisTrials_att != None:
    for paramName in thisTrials_att:
        exec('{} = thisTrials_att[paramName]'.format(paramName))

for thisTrials_att in trials_att:
    currentLoop = trials_att
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_att.rgb)
    if thisTrials_att != None:
        for paramName in thisTrials_att:
            exec('{} = thisTrials_att[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "language_attitudes"-------
    t = 0
    language_attitudesClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_lang_att_section.setText(eval(section))
    text_lang_att_ques.setText(eval(questionText))
    text_lang_att_qnum.setText(questionNum)
    rating_lang_att.reset()
    # keep track of which components have finished
    language_attitudesComponents = [text_lang_att_section, text_lang_att_ques, text_lang_att_qnum, rating_lang_att]
    for thisComponent in language_attitudesComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "language_attitudes"-------
    while continueRoutine:
        # get current time
        t = language_attitudesClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_lang_att_section* updates
        if t >= 0.0 and text_lang_att_section.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_att_section.tStart = t
            text_lang_att_section.frameNStart = frameN  # exact frame index
            text_lang_att_section.setAutoDraw(True)
        
        # *text_lang_att_ques* updates
        if t >= 0.0 and text_lang_att_ques.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_att_ques.tStart = t
            text_lang_att_ques.frameNStart = frameN  # exact frame index
            text_lang_att_ques.setAutoDraw(True)
        
        # *text_lang_att_qnum* updates
        if t >= 0.0 and text_lang_att_qnum.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_lang_att_qnum.tStart = t
            text_lang_att_qnum.frameNStart = frameN  # exact frame index
            text_lang_att_qnum.setAutoDraw(True)
        # *rating_lang_att* updates
        if t >= 0.0 and rating_lang_att.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_lang_att.tStart = t
            rating_lang_att.frameNStart = frameN  # exact frame index
            rating_lang_att.setAutoDraw(True)
        continueRoutine &= rating_lang_att.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in language_attitudesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "language_attitudes"-------
    for thisComponent in language_attitudesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_att (TrialHandler)
    trials_att.addData('rating_lang_att.response', rating_lang_att.getRating())
    trials_att.addData('rating_lang_att.rt', rating_lang_att.getRT())
    # the Routine "language_attitudes" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_att'


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
