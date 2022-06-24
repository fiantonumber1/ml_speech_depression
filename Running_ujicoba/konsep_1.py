from scipy.io.wavfile import write as write_wav
import numpy as np
import librosa
from mutagen.wave import WAVE
from pydub import AudioSegment
import glob
import os
import matplotlib.pyplot as plt
import librosa
import numpy as np
import librosa.display

def zero_runs(a):
    iszero = np.concatenate(([0], np.equal(a, 0).view(np.int8), [0]))
    absdiff = np.abs(np.diff(iszero))
    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
    return ranges

def chunck_split(out_dir):
    loopingke = 0
    waktu = 0
    zero = []
    y = 0
    path = "E:\Capstone_Project\Folder_Datasheet\Depression"
    files = os.listdir(path)

    for filename in glob.glob(os.path.join(path, '*.wav')):
        try:
            zero.append(filename[48:51])
        except:
            print("")

    for i in zero:
        print("looping ke{}".format(i))
        AUDIO_FILE_1 = f"E:\Capstone_Project\Folder_Datasheet\Depression\{i}_AUDIO.wav"
        
        min_length_for_silence = 0.01 # seconds
        percentage_for_silence = 0.01 # eps value for silence
        required_length_of_chunk_in_seconds = 60 # Chunk will be around this value not exact
        sample_rate = 16000 # Set to None to use default

        # Load audio
        waveform, sampling_rate = librosa.load(AUDIO_FILE_1, sr=sample_rate)

        # Create mask of silence
        eps = waveform.max() * percentage_for_silence
        silence_mask = (np.abs(waveform) < eps).astype(np.uint8)

        # Find where silence start and end
        runs = zero_runs(silence_mask)
        lengths = runs[:, 1] - runs[:, 0]

        # Left only large silence ranges
        min_length_for_silence = min_length_for_silence * sampling_rate
        large_runs = runs[lengths > min_length_for_silence]
        lengths = lengths[lengths > min_length_for_silence]

        # Mark only center of silence
        silence_mask[...] = 0
        for start, end in large_runs:
            center = (start + end) // 2
            silence_mask[center] = 1

        min_required_length = required_length_of_chunk_in_seconds * sampling_rate
        chunks = []
        prev_pos = 0
        for i in range(min_required_length, len(waveform), min_required_length):
            start = i
            end = i + min_required_length
            next_pos = start + silence_mask[start:end].argmax()
            part = waveform[prev_pos:next_pos].copy()
            prev_pos = next_pos
            if len(part) > 0:
                chunks.append(part)

        # Add last part of waveform
        part = waveform[prev_pos:].copy()
        chunks.append(part)
        print('Total chunks: {}'.format(len(chunks)))

        new_files = []
        for i, chunk in enumerate(chunks):
            out_file = out_dir + "chunk_{}.wav".format(loopingke)
            print("exporting", out_file)
            write_wav(out_file, sampling_rate, chunk)
            new_files.append(out_file)
            loopingke+=1

chunck_split("E:\\Capstone_Project\\Depression_chunk\\")