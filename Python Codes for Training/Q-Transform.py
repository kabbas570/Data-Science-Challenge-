import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
#import stanford_mir; stanford_mir.init()
#x, sr = librosa.load('sile.mp3')


### Silence ###
x, sr = librosa.load('/home/user01/data_ssd/Abbas/ETH/DataSet/silence/shorter_audio.mp3')
fmin = librosa.midi_to_hz(36)
C = librosa.cqt(x, sr=sr, fmin=fmin, n_bins=72)
logC = librosa.amplitude_to_db(abs(C))
plt.figure()
librosa.display.specshow(logC, sr=sr, fmin=fmin, cmap='coolwarm')
for i in range(500):
    plt.savefig('DATASET/SILENCE/img'+ str(i)+'.png')


### SInging ####
    
import glob
img_id = []
for infile in sorted(glob.glob('/home/user01/data_ssd/Abbas/ETH/DataSet/singing/*.wav')):
    img_id.append(infile)
    
for i in range(500):
    x, sr = librosa.load(img_id[i])
    fmin = librosa.midi_to_hz(36)
    C = librosa.cqt(x, sr=sr, fmin=fmin, n_bins=72)
    logC = librosa.amplitude_to_db(abs(C))
    plt.figure()
    librosa.display.specshow(logC, sr=sr, fmin=fmin, cmap='coolwarm')
    plt.savefig('DATASET/SINGING/img'+ str(i)+'.png')
    
### Speaking ######
    
import glob
img_id1 = []
for infile in sorted(glob.glob('/home/user01/data_ssd/Abbas/ETH/DataSet/speaking/*.mp3')):
    img_id1.append(infile)
    
for i in range(500):
    x, sr = librosa.load(img_id1[i])
    fmin = librosa.midi_to_hz(36)
    C = librosa.cqt(x, sr=sr, fmin=fmin, n_bins=72)
    logC = librosa.amplitude_to_db(abs(C))
    plt.figure()
    librosa.display.specshow(logC, sr=sr, fmin=fmin, cmap='coolwarm')
    plt.savefig('DATASET/SPEAKING/img'+ str(i)+'.png')