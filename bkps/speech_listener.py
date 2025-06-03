# speech_listener.py
#import os
#import time
#import pyaudio
#import wave
#from faster_whisper import WhisperModel
#
## Config
#AUDIO_FILE = "temp.wav"
#MODEL_SIZE = "base"  # can also be 'small', 'medium', 'large'
#
#model = WhisperModel(MODEL_SIZE, compute_type="int8")
#
#def record_audio(duration=5, filename=AUDIO_FILE):
#    RATE = 16000
#    CHUNK = 1024
#    FORMAT = pyaudio.paInt16
#    CHANNELS = 1
#
#    audio = pyaudio.PyAudio()
#    stream = audio.open(format=FORMAT, channels=CHANNELS,
#                        rate=RATE, input=True, frames_per_buffer=CHUNK)
#
#    print("🎙️ Listening...")
#    frames = []
#    for _ in range(0, int(RATE / CHUNK * duration)):
#        data = stream.read(CHUNK)
#        frames.append(data)
#
#    print("🔊 Recording done.")
#    stream.stop_stream()
#    stream.close()
#    audio.terminate()
#
#    with wave.open(filename, 'wb') as wf:
#        wf.setnchannels(CHANNELS)
#        wf.setsampwidth(audio.get_sample_size(FORMAT))
#        wf.setframerate(RATE)
#        wf.writeframes(b''.join(frames))
#
#def listen_to_speech():
#    record_audio()
#    segments, _ = model.transcribe(AUDIO_FILE)
#    text = " ".join([seg.text for seg in segments])
#    return text.strip()



import wave
import pyaudio
import numpy as np
from tempfile import NamedTemporaryFile
from faster_whisper import WhisperModel

whisper_model = WhisperModel("base", compute_type="int8")

RATE = 16000
CHANNELS = 1
CHUNK = 1024
SILENCE_THRESHOLD = 500
MAX_SILENT_CHUNKS = int(RATE / CHUNK * 2)

def record_until_silence():
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16, channels=CHANNELS,
                     rate=RATE, input=True,
                     frames_per_buffer=CHUNK)
    print("🎙️ Listening for question...")

    frames = []
    silent_chunks = 0
    recording = False
    max_chunks = int(RATE / CHUNK * 10)

    for _ in range(max_chunks):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)
        amplitude = np.frombuffer(data, np.int16)
        avg_amp = np.abs(amplitude).mean()

        if avg_amp > SILENCE_THRESHOLD:
            recording = True
            silent_chunks = 0
        elif recording:
            silent_chunks += 1
            if silent_chunks > MAX_SILENT_CHUNKS:
                break

    stream.stop_stream()
    stream.close()
    pa.terminate()

    if not recording:
        print("⚠️ No speech detected.")
        return None

    with NamedTemporaryFile(delete=False, suffix=".wav") as tf:
        wf = wave.open(tf.name, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(pa.get_sample_size(pyaudio.paInt16))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        return tf.name

def listen_to_speech():
    audio_file = record_until_silence()
    if not audio_file:
        return ""
    segments, _ = whisper_model.transcribe(audio_file)
    text = "".join(seg.text for seg in segments)
    print(f"Heard: {text}")
    return text.strip()
