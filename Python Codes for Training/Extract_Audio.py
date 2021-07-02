
import glob
img_id = []
for infile in sorted(glob.glob('/home/user01/data_ssd/Abbas/ETH/Sing/*.wav')):
    img_id.append(infile)
    
from pydub import AudioSegment
for i in range(500):
    name='song'+str(i)
    path="/home/user01/data_ssd/Abbas/ETH/DataSet/singing/"+name+".wav"
    t1 = 0 * 1000 #Works in milliseconds
    t2 = 2 * 1000
    newAudio = AudioSegment.from_wav(img_id[i])
    newAudio = newAudio[t1:t2]
    newAudio.export(path, format="wav") #Exports to a wav file in the current path.


from pydub import AudioSegment
for i in range(500):
    name='song'+str(i)
    path="/home/user01/data_ssd/Abbas/ETH/DataSet/silence/"+name+".wav"
    t1 = 2 * 1000 #Works in milliseconds
    t2 = 4 * 1000
    newAudio = AudioSegment.from_wav('silence_2.wav')
    newAudio = newAudio[t1:t2]
    newAudio.export(path, format="wav") #Exports to a wav file in the current path.


import glob
img_id = []
for infile in sorted(glob.glob('/home/user01/data_ssd/Abbas/ETH/SKP/*.mp3')):
    img_id.append(infile)
    
    
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
for i in range(500):
    name='speak'+str(i+500)
    path="/home/user01/data_ssd/Abbas/ETH/"+name+".mp3"
    ffmpeg_extract_subclip(img_id[i], 
                       6, 8, 
                       targetname=path)





