import os
import csv
from mutagen.wave import WAVE
from pydub import AudioSegment
import glob
import os
import matplotlib.pyplot as plt
import librosa
import numpy as np
import librosa.display


def audio_duration(length):
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds

    return hours, mins, seconds  # returns the duration



rootdir = 'E:\Capstone_Project\Folder_Datasheet'
array_length = len(rootdir)
collecting_folder = []
gagal = 0
sukses = 0
audio_normal = 0
audio_depresi = 0
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        collecting_folder.append(d)

jumlah_audio = 0
for folder in collecting_folder:
    folder_file = folder
    angka_folder = folder_file[array_length+1:array_length+4]
    excell = os.path.join(folder_file,"{}_TRANSCRIPT.csv".format(angka_folder))
    with open(excell, newline='') as f:
        reader = csv.reader(f)
        n=0
        array_keterangan = []
        for row in reader:
            split_value = []
            if n==0:
                n+=1
            else:
                try:
                    waktu_awal_akhir = (row[0])[0:14]
                    waktu = (waktu_awal_akhir).split(".")
                    start_time_awal = waktu[0]
                    start_time_akhir = waktu[1][0:3]
                    stop_time_awal = waktu[1][4:]
                    stop_time_akhir = waktu[2][0:3]
                    awal_waktu = start_time_awal +"."+start_time_akhir
                    akhir_waktu = stop_time_awal+"."+stop_time_akhir
                    jenis_class =  (row[0])[14]
                    split_value.append(awal_waktu)
                    split_value.append(akhir_waktu)
                    if jenis_class == "E":
                        split_value.append("Tidak_Depresi")
                    else:
                        split_value.append("Depresi")

                    AUDIO_FILE_1 = os.path.join(folder_file,"{}_AUDIO.wav".format(angka_folder))
                    audio = WAVE(AUDIO_FILE_1)
                    sound = AudioSegment.from_file(AUDIO_FILE_1)
                    first_cut_point = float(split_value[0])*1000 # MiliDetik ke 0 untuk looping pertama
                    last_cut_point =  float(split_value[1])*1000  # MiliDetik ke 100.000 untuk looping pertama
                    sound_clip = sound[first_cut_point:last_cut_point]
                    if split_value[2]=="Tidak_Depresi":
                        sound_clip.export("E:\\Capstone_Project\\Depressionvsnormal\\normal\\normal{}.wav".format(audio_normal),
                                              format="wav")
                        audio_normal += 1
                    elif split_value[2]=="Depresi":
                        sound_clip.export("E:\\Capstone_Project\\Depressionvsnormal\\Depression\\Depression{}.wav".format(audio_depresi),
                                              format="wav")
                        audio_depresi += 1
                    sukses+=1
                except:
                    gagal+=1

print("{} audio sukses".format(sukses))
print("{} audio depresi sukses".format(audio_depresi))
print("{} audio normal sukses".format(audio_normal))
print("{} audio gagal".format(gagal))

