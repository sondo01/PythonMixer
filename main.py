import sounddevice as sd
import numpy as np

def select_audio_devices():
    devices = sd.query_devices()
    print()
    print(str.upper("Available Input Devices:"))
    print("====================")
    print(devices)
    print()
    print("====================")
    print()

    input_device_index = int(input("Select an input device: "))
    output_device_index = int(input("Select an output device: "))
    # input_channels = devices[input_device_index]['max_input_channels']
    # output_channels = devices[output_device_index]['max_output_channels']
    input_channels = 1
    return input_device_index, output_device_index, input_channels

def audio_callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata

def main():
    input_device_index, output_device_index, num_channels = select_audio_devices()
    # Configure the input and output parameters
    samplerate = 44100
    blocksize = 1024
    # Set the desired latency and min_latency values
    desired_latency = 0.00001  # Adjust this value as needed
    with sd.Stream(device=(input_device_index, output_device_index),
                   channels=num_channels,  # Set the number of channels
                   callback=audio_callback,
                   samplerate=samplerate,
                   blocksize=blocksize,
                   latency=desired_latency):
        print("Audio is being captured from the input device and played on the output device.")
        print("Press Ctrl+C to stop...")

        try:
            sd.sleep(3600000)  # Run the stream for a very long time (Ctrl+C to stop)
        except KeyboardInterrupt:
            print("\nStopping the audio stream")

if __name__ == "__main__":
    main()
