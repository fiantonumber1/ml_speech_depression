from mutagen.wave import WAVE
from pydub import AudioSegment
import glob
import os
import matplotlib.pyplot as plt
import librosa
import numpy as np
import librosa.display


# Using ffmpeg for noise removal


# function to convert the infoation into
# some readable format
def audio_duration(length):
        hours = length // 3600  # calculate in hours
        length %= 3600
        mins = length // 60  # calculate in minutes
        length %= 60
        seconds = length  # calculate in seconds

        return hours, mins, seconds  # returns the duration

def running_progam(pemotongan_waktu):
    loopingke = 0
    waktu = 0
    zero = []
    loops=-1
    y = 0
    path = "E:\Capstone_Project\Folder_Datasheet\Depression"
    files = os.listdir(path)

    for filename in glob.glob(os.path.join(path, '*.wav')):
        try:
            zero.append(filename[48:51])
            loops+=1
        except:
            print("")
    print(loops)
    for i in zero:
        AUDIO_FILE_1 = "E:\Capstone_Project\Folder_Datasheet\Depression\\{}_AUDIO.wav".format(i)
        # load data
        # rate, data = wavfile.read(AUDIO_FILE_1)
        # perform noise reduction
        # reduced_noise = nr.reduce_noise(y=data, sr=rate)
        # wavfile.write(AUDIO_FILE_1, rate, reduced_noise)
        # Create a WAVE object
        # Specify the directory address of your wavpack file
        # "alarm.wav" is the name of the audiofile
        audio = WAVE(AUDIO_FILE_1)

        # contains all the metadata about the wavpack file
        audio_info = audio.info
        length = int(audio_info.length)
        hours, mins, seconds = audio_duration(length)
        detik = mins * 60 + seconds
        # print('Total Duration: {}:{}:{}'.format(hours, mins, seconds))
        # print('Total detik: {}'.format(detik))
        # print('Total audio tiap 30 detik: {}'.format(detik/30))
        waktu += detik
        sound = AudioSegment.from_file(AUDIO_FILE_1)
        dipotong_tiap = pemotongan_waktu
        first_cut_point = 0  # MiliDetik ke 0 untuk looping pertama
        last_cut_point = dipotong_tiap * 1000  # MiliDetik ke 100.000 untuk looping pertama
        for i in range(int(detik / dipotong_tiap)):
            sound_clip = sound[first_cut_point:last_cut_point]
            first_cut_point += 1000 * int(detik / dipotong_tiap)  # Ditambah 100.000 milidetik untuk looping
            last_cut_point += 1000 * int(detik / dipotong_tiap)  # Ditambah 100.000 milidetik untuk looping
            sound_clip.export("E:\Capstone_Project\Depression\Depression{}.wav".format(loopingke), format="wav")
            loopingke += 1
    print("{} file datasheet".format(int(waktu / dipotong_tiap)))

    Data_gagal = 0
    Data_Sukses = 0
    for i in range(loopingke):
        try:
            y, sr = librosa.load(f'E:\Capstone_Project\Depression/Depression{i}.wav')
            librosa.feature.melspectrogram(y=y, sr=sr)
            S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                               fmax=8000)

            fig, ax = plt.subplots()
            S_dB = librosa.power_to_db(S, ref=np.max)
            img = librosa.display.specshow(S_dB)
            # ax.set(title='Log Mel-frequency spectrogram')

            plt.savefig(f'E:\Capstone_Project\Depression_Folder/Depression{i}.jpg')
            Data_Sukses += 1
        except:
            Data_gagal += 1
            print("Gagal ke{}".format(Data_gagal))
    Total_Sukses = ((Data_Sukses) / (Data_Sukses + Data_gagal) * 100)
    tingkat_running = "{}% Sukses menjadi spectogram".format(Total_Sukses)
    return tingkat_running


running_progam(30)