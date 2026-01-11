import serial
import wave
import time

# --- KONFIGURASI ---
SERIAL_PORT = 'COM9'     # <--- Cek lagi port-nya!
BAUD_RATE = 500000
SAMPLE_RATE = 8000       # <--- HARUS SAMA DENGAN KODE ESP32 (8000)
DURATION = 5             # Durasi rekam
OUTPUT_FILENAME = "hasil_rekaman_final.wav"

TOTAL_BYTES = SAMPLE_RATE * 2 * DURATION

print(f"Mencoba koneksi ke {SERIAL_PORT}...")

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    time.sleep(2) # Tunggu ESP32 reset
    ser.reset_input_buffer()
    
    print(f"--- MULAI BICARA! (Rekam {DURATION} detik) ---")
    
    audio_data = ser.read(TOTAL_BYTES)
    
    print("--- SELESAI ---")
    
    with wave.open(OUTPUT_FILENAME, "w") as wav_file:
        wav_file.setnchannels(1)        # Mono
        wav_file.setsampwidth(2)        # 16-bit
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(audio_data)
    
    print(f"Simpan file sukses: {OUTPUT_FILENAME}")
    ser.close()

except Exception as e:
    print(f"Error: {e}")