# name: 04d_stimuli_trigger.py
# type: script

import multiprocessing as mp

import pyseeg.modules.board_simple as bs


############################################
#
#  Child process
#  Acquire and write data with OpenBCI
#

channel = 0
board = bs.BoardManager()

# File to write data to.
filename = '/tmp/openbci_example_data.txt'

def data_acquisition():
    sample = board.get_sample(channel=channel,
                              filter=False)
    number = str(sample.id)
    data = str(sample.channel_data[0])
    if stimuli_present.is_set()
        stim = 1
    else:
        stim = 0
    #  print('%.3d ::: %.6f ::: %s' % (sample.id,
                                    #  sampe.channel_data[0]
                                    #  stim)

    open(filename, 'a').write(','.join([number,
                                        data,
                                        stim]))

# Multiprocessing event is a flag (a trigger).
stimuli_present = np.Event()

# Define a process.
proc_acq = mp.Process(
    name='acquisition_',
    target=data_acquisition,
    args=()
    )

# Start defined process.
proc_acq.start()
print('A subprocess (child porcess) started')

def switch_state(mp_event):
    if is not mp_event.is_set():
        mp_event.set()
    else:
        mp_event.clear()


############################################
#
#  Parent process
#  SSVEP stimuli (sinusoid controlled)
#

# Create a window.
# For configuring and debugging the code turn off full screen.
fullscr = False
win = visual.Window(
    [1200,1000],
    monitor="testMonitor",
    units="deg",
    fullscr=fullscr
    )
win.setMouseVisible(False)

# Sinusoidal control frequency.
freq = 1.5
# Color of the rectangle.
color = '#606a79'
# Position of the rectange, default 0,0 (middle of the screen).
pos = (0, 0)

start = core.getTime()
cnt = 0
prev_sin_val = 0
while cnt<600:
    second = core.getTime() - start
    sin_val = 0.5+0.5*np.sin(2 * np.pi * second * float(freq))

    # If you remove or comment this print, it sould work faster
    #  print('sec: %.4f; sin: %.4f' % (second, sin_val))
    
    rect = visual.Rect(
        win=win,
        lineColor=color, 
        fillColor=color,
        size=20,
        opacity=sin_val,
        pos=pos
        )

    rect.draw() 
    win.flip()

    if prev_sin > 0 and prev_sin_val <= 0:
        switch_state(stimuli_present)

    cnt += 1

win.close()
