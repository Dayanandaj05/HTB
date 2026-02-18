#!/usr/bin/env python3
"""
Artifact Beta Generator
Creates a WAV file with spectrogram containing the hidden flag
Real flag: HTB{psg_sonic_exfil} -> Caesar +7 -> OAI{wzn_zvupj_lempss}
"""

import numpy as np
import wave

def create_rogue_signal_audio():
    """
    Create a WAV file with a spectrogram that visualizes the flag.
    Real flag: HTB{psg_sonic_exfil}
    Encoded (Caesar +7): OAI{wzn_zvupj_lempss}
    
    The flag is encoded as ASCII frequencies in the ultrasonic range
    """
    
    hidden_flag = "OAI{wzn_zvupj_lempss}"
    
    # Audio parameters
    sample_rate = 44100  # Standard CD quality
    duration = 4.5
    num_samples = int(sample_rate * duration)
    
    # Create audio data
    audio_data = np.zeros(num_samples, dtype=np.int16)
    
    # Encode the flag as a series of frequency sweeps
    time = np.arange(num_samples) / sample_rate
    
    # Background ultrasonic carrier (mimics interference)
    background = np.sin(2 * np.pi * 20000 * time) * 0.1
    audio_data = np.int16(background * 32767)
    
    # Encode each character as a frequency in the ultrasonic range
    chunk_size = sample_rate // 2  # 0.5 seconds per character
    
    for idx, char in enumerate(hidden_flag):
        # Convert ASCII to frequency (offset to ultrasonic range)
        ascii_val = ord(char)
        frequency = 15000 + (ascii_val * 20)
        
        start = idx * chunk_size
        end = min(start + chunk_size, num_samples)
        
        if end > start:
            chunk_time = (np.arange(end - start) / sample_rate)
            # Create frequency sweep for visual clarity in spectrogram
            chirp_freq = np.linspace(frequency - 100, frequency + 100, end - start)
            sweep = np.sin(2 * np.pi * chirp_freq * chunk_time)
            audio_data[start:end] += np.int16(sweep * 16384)
    
    # Add ultrasonic pulsing patterns
    pulse_freq = 25000
    for i in range(0, num_samples, sample_rate // 4):
        end = min(i + sample_rate // 8, num_samples)
        pulse_time = np.arange(end - i) / sample_rate
        pulse = np.sin(2 * np.pi * pulse_freq * pulse_time)
        audio_data[i:end] += np.int16(pulse * 8192)
    
    # Normalize to prevent clipping
    max_val = np.max(np.abs(audio_data))
    if max_val > 32767:
        audio_data = np.int16(audio_data * (32767 / max_val))
    
    # Write to WAV file
    with wave.open('rogue_signal.wav', 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_data.tobytes())
    
    print("✓ Artifact Beta created: rogue_signal.wav")
    print(f"  Hidden flag in spectrogram: {hidden_flag}")
    print("  Real flag (Caesar -7 decoded): HTB{psg_sonic_exfil}")
    print(f"  Duration: {duration} seconds")
    print(f"  Sample rate: {sample_rate} Hz")
    print("  Encoding: ASCII characters mapped to ultrasonic frequencies")
    print("  To extract: Use spectrogram analysis (Audacity, Sonic Visualiser, or scipy)")
    print("\nTechnical Details:")
    print(f"  - Carrier frequency: 20 kHz (ultrasonic)")
    print(f"  - Character frequencies: 15000 + (ASCII * 20) Hz")
    print(f"  - Chirp sweep width: ±100 Hz per character")
    print(f"  - Pulse frequency: 25 kHz")
    
    return 'rogue_signal.wav'


if __name__ == "__main__":
    try:
        create_rogue_signal_audio()
        print("\n✓ Audio file generation complete!")
    except ImportError:
        print("Installing required package: numpy...")
        import subprocess
        subprocess.check_call(['pip', 'install', 'numpy', '-q'])
        create_rogue_signal_audio()
