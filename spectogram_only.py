import glob
import os
import matplotlib.pyplot as plt
import librosa
import numpy as np
import librosa.display


def spectogram_only(folder_asal,folder_dituju,namajenis):
    Data_Sukses=0
    Data_gagal=0
    nama_file = []
    for filename in glob.glob(os.path.join(folder_asal, '*.wav')):
        try:
            nama_file.append(filename)
        except:
            print("Bukan file wav atau error")
    for i in nama_file:
        try:
            y, sr = librosa.load(i)
            librosa.feature.melspectrogram(y=y, sr=sr)
            S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                               fmax=8000)

            fig, ax = plt.subplots()
            S_dB = librosa.power_to_db(S, ref=np.max)
            img = librosa.display.specshow(S_dB)
            # ax.set(title='Log Mel-frequency spectrogram')
            savefigure = os.path.join(folder_dituju, '{}{}.jpg'.format(namajenis,Data_Sukses))
            plt.savefig(savefigure)
            Data_Sukses += 1
            print("Spectogram sukses ke{}".format(Data_Sukses))
        except:
            Data_gagal += 1
            print("Spectogram gagal ke{}".format(Data_gagal))
    Total_Sukses = ((Data_Sukses) / (Data_Sukses + Data_gagal) * 100)
    tingkat_running = "{}% Sukses menjadi spectogram".format(Total_Sukses)
    return tingkat_running


