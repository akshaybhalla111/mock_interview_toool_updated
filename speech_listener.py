import wave
import pyaudio
import numpy as np
from tempfile import NamedTemporaryFile
from faster_whisper import WhisperModel
from config import AUDIO_INPUT

whisper_model = WhisperModel("base", compute_type="int8")

RATE = 16000
CHANNELS = 1
CHUNK = 1024
SILENCE_THRESHOLD = 500
MAX_SILENT_CHUNKS = int(RATE / CHUNK * 1)

def get_input_device_index(pyaudio_instance, keyword):
    for i in range(pyaudio_instance.get_device_count()):
        info = pyaudio_instance.get_device_info_by_index(i)
        if keyword.lower() in info['name'].lower() and info['maxInputChannels'] > 0:
            print(f"🎧 Using input device: {info['name']}")
            return i
    print(f"⚠️ No device with keyword '{keyword}' found. Using default.")
    return None

def record_until_silence():
    pa = pyaudio.PyAudio()
    device_keyword = "Stereo Mix" if AUDIO_INPUT == "stereo_mix" else "microphone"
    input_index = get_input_device_index(pa, device_keyword)

    stream = pa.open(format=pyaudio.paInt16,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     input_device_index=input_index,
                     frames_per_buffer=CHUNK)

    print(f"🎙️ Listening from: {device_keyword}...")

    frames = []
    silent_chunks = 0
    recording = False

    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)
        amplitude = np.frombuffer(data, np.int16)
        if np.abs(amplitude).mean() > SILENCE_THRESHOLD:
            recording = True
            silent_chunks = 0
        elif recording:
            silent_chunks += 1
            if silent_chunks > MAX_SILENT_CHUNKS:
                break

    stream.stop_stream()
    stream.close()
    pa.terminate()

    with NamedTemporaryFile(delete=False, suffix=".wav") as tf:
        with wave.open(tf.name, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(pa.get_sample_size(pyaudio.paInt16))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
        return tf.name

def listen_to_speech():
    audio_file = record_until_silence()
    segments, _ = whisper_model.transcribe(audio_file)
    text = "".join(seg.text for seg in segments)
    print(f"Heard: {text}")
    return text.strip()
