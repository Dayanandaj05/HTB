import numpy as np
from scipy.io import wavfile

def mask_audio_to_spectrum(input_file, output_file="masked_transmission.wav"):
    # 1. Load your generated Morse audio
    sample_rate, data = wavfile.read(input_file)
    
    # Normalize data if it's not float
    if data.dtype != np.float32:
        data = data.astype(np.float32) / np.max(np.abs(data))

    t = np.linspace(0, len(data)/sample_rate, len(data))

    # 2. FREQUENCY SHIFTING (The "Secret" Layer)
    # We multiply the Morse signal by a high-frequency carrier (e.g., 16kHz)
    # This "moves" the Morse code up to a range humans can barely hear 
    # but where spectrograms show it clearly.
    carrier_freq = 16000 
    shifted_morse = data * np.sin(2 * np.pi * carrier_freq * t)

    # 3. NOISE MASKING (The "Camouflage" Layer)
    # We add "Pink Noise" or White Noise to drown out the original beeps
    noise = 0.05 * np.random.normal(0, 1, len(data))
    
    # 4. COMBINE
    # We keep the shifted_morse loud enough to be seen, but the noise 
    # covers the rhythmic "beeping" sound.
    final_audio = shifted_morse + noise

    # Save the file
    wavfile.write(output_file, sample_rate, final_audio.astype(np.float32))
    print(f"Masked file created: {output_file}")

# Usage: Ensure your file from the online generator is named 'morse.wav'
mask_audio_to_spectrum("morse.wav")