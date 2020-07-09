import numpy as np
import pyaudio
import warnings
import keyboard
from pynput.mouse import Button, Controller

# Warnings
warnings.simplefilter("ignore", DeprecationWarning)

NOTE_MIN = 40       # E2
NOTE_MAX = 71       # B4
FSAMP = 22050       # Sampling frequency in Hz
FRAME_SIZE = 256   # samples per frame
FRAMES_PER_FFT = 32  # FFT takes average across how many frames?

######################################################################
# Derived quantities from constants above. Note that as
# SAMPLES_PER_FFT goes up, the frequency step size decreases (sof
# resolution increases); however, it will incur more delay to process
# new sounds.

SAMPLES_PER_FFT = FRAME_SIZE * FRAMES_PER_FFT
FREQ_STEP = float(FSAMP) / SAMPLES_PER_FFT

######################################################################
# For printing out notes

NOTE_NAMES = 'E F F# G G# A A# B C C# D D#'.split()


######################################################################
# These three functions are based upon this very useful webpage:
# https://newt.phys.unsw.edu.au/jw/notes.html

def freq_to_number(f):
    return 71 + 12 * np.log2(f / 493.88)


def number_to_freq(n):
    return 493.88 * 2.0**((n - 71) / 12.0)


def note_name(n):
    return NOTE_NAMES[n % NOTE_MIN % len(NOTE_NAMES)] + str(int(n / 12 - 1))

######################################################################
# Ok, ready to go now.

# Get min/max index within FFT of notes we care about.
# See docs for numpy.rfftfreq()


def note_to_fftbin(n):
    return number_to_freq(n) / FREQ_STEP


imin = max(0, int(np.floor(note_to_fftbin(NOTE_MIN - 1))))
imax = min(SAMPLES_PER_FFT, int(np.ceil(note_to_fftbin(NOTE_MAX + 1))))

# Allocate space to run an FFT.
buf = np.zeros(SAMPLES_PER_FFT, dtype=np.float32)
num_frames = 0

# Initialize audio
stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                channels=1,
                                rate=FSAMP,
                                input=True,
                                frames_per_buffer=FRAME_SIZE)

stream.start_stream()

# Create Hanning window function
window = 0.5 * (1 - np.cos(np.linspace(0, 2 * np.pi, SAMPLES_PER_FFT, False)))

# Print initial text
print('sampling at', FSAMP, 'Hz with max resolution of', FREQ_STEP, 'Hz')
print()

# As long as we are getting data:
while stream.is_active():

    # Shift the buffer down and new data in
    buf[:-FRAME_SIZE] = buf[FRAME_SIZE:]
    buf[-FRAME_SIZE:] = np.fromstring(stream.read(FRAME_SIZE), np.int16)

    # Run the FFT on the windowed buffer
    fft = np.fft.rfft(buf * window)

    # Get frequency of maximum response in range
    freq = (np.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP

    # Get note number and nearest note
    n = freq_to_number(freq)
    n0 = int(round(n))

    # Console output once we have a full buffer
    num_frames += 1

    # Debug
    # if num_frames >= FRAMES_PER_FFT:
    #     print('number {:7.2f} freq: {:7.2f} Hz     note: {:>3s} {:+.2f}'.format(n,
    #                                                                             freq, note_name(n0), n - n0))

    # Controller
    mouse = Controller()

    if n0 == 64:
        keyboard.press('W')
        print('E4 - W')

    if n0 == 67:
        mouse.move(-20, 0)
        print('G4 - Look Left')

    if n0 == 69:
        mouse.move(20, 0)
        print('A4 - Look Right')

    elif n0 == 44:
        keyboard.release('W')
