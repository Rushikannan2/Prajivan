import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import os

def plot_fourier_transform(file_path, animal_name):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File not found for {animal_name}: {file_path}")
        return

    # Read the audio file
    sample_rate, data = wavfile.read(file_path)

    # Perform Fourier Transform
    fourier_transform = np.fft.fft(data)
    frequency = np.fft.fftfreq(len(fourier_transform), d=1/sample_rate)

    # Plotting the results
    plt.figure(figsize=(12, 6))
    plt.plot(frequency[:len(frequency)//2], np.abs(fourier_transform)[:len(frequency)//2])  # plot only positive frequencies
    plt.title(f'Fourier Transform of {animal_name} Distress Call')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.xlim(0, 5000)  # Limiting x-axis for better visibility (adjust as needed)

    # Ensure the processed_data directory exists
    output_dir = 'processed_data'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the plot
    plt.savefig(os.path.join(output_dir, f'{animal_name}_fourier_transform.png'))
    plt.show()

# List of animals and their audio file paths
animals = {
    'elephant': 'C:/Users/Rushi/OneDrive/Desktop/ABCD/data/processed_data/Elephant_processed.wav',
    'wolf': 'C:/Users/Rushi/OneDrive/Desktop/ABCD/data/processed_data/Wolves_processed.wav',
    'crow': 'C:/Users/Rushi/OneDrive/Desktop/ABCD/data/processed_data/Crow_processed.wav',
    'chimpanzee': 'C:/Users/Rushi/OneDrive/Desktop/ABCD/data/processed_data/Chimpanzee_processed.wav',
    'deer': 'C:/Users/Rushi/OneDrive/Desktop/ABCD/data/processed_data/Deer_processed.wav',
    'sparrow': 'C:/Users/Rushi/OneDrive/Desktop/ABCD/data/processed_data/Sparrow_processed.wav',
    'eagle': 'C:/Users/Rushi/OneDrive/Desktop/ABCD/data/processed_data/Eagle_processed.wav',
    'monkey': 'C:/Users/Rushi/OneDrive/Desktop/ABCD/data/processed_data/Monkey_processed.wav'
}

# Loop through each animal and apply Fourier Transform
for animal, file_path in animals.items():
    plot_fourier_transform(file_path, animal)
