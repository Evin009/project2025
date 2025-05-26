from pyaudio import *
import wave

# import shutil
# shutil.copy("sample.wav", "/Users/yourname/Google Drive/ColabAudio/sample.wav")


#creating audio object 
audio = PyAudio()

#opening recording strem
stream = audio.open(format=paInt16, channels=1,rate = 44100, input=True,frames_per_buffer=1024)

#list of frames which stores audio data/frames
frames = []

# User prompting
print('Recording press Enter...')
input()


print('Recording in progress.... Ctrl+C to stop')
try:
    while True:
        data = stream.read(1024,exception_on_overflow=False)
        frames.append(data)
except KeyboardInterrupt:
    print('\nRecording Stopped...')
    

stream.stop_stream()
stream.close()
audio.terminate()

wf = wave.open('Sample.wav', 'wb')
wf.setnchannels(1)
wf.setsampwidth(audio.get_sample_size(paInt16))
wf.setframerate(44100)
wf.writeframes(b''.join(frames))
wf.close()
