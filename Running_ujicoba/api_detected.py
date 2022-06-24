import matplotlib.pyplot as plt
import librosa
import numpy as np
import librosa.display
import os
from tensorflow.keras import models
from flask import Flask, request


def convert_spectogram(file_audio, save_spectogram_folder):
    y, sr = librosa.load(file_audio)
    librosa.feature.melspectrogram(y=y, sr=sr)
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                       fmax=8000)

    fig, ax = plt.subplots()
    S_dB = librosa.power_to_db(S, ref=np.max)
    img = librosa.display.specshow(S_dB)
    # ax.set(title='Log Mel-frequency spectrogram')
    hasil_gambar = os.path.join(save_spectogram_folder, 'status_kondisi.jpg')
    plt.savefig(hasil_gambar)


convert_spectogram("E:\\Capstone_Project\\Depressionvsnormal\\Depression\\Depression0.wav","E:\\Capstone_Project")
app = Flask(__name__)
version = '1'
path_model_voice = 'E:\\Capstone_Project\\modelh5\\predictive_model.h5'
model_voice = models.load_model(path_model_voice)
det = model_voice.predict("E:\\Capstone_Project\\status_kondisi.jpg")
print(det)