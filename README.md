# PythonMixer
# Audio Capture and Playback Script

## 1. What is it?

This lightweight script serves a single purpose: capturing audio from input devices (such as your laptop's microphone, headphones, earphones, or earplugs) and playing it back on output devices (including your laptop's speakers, external speakers, TV, amplifier, or headphones, all connected to your laptop.

## 2. What's it for?

This script finds utility in two primary scenarios:

- **Teaching:** In some classrooms, projectors are available, but microphones are not. If your voice tends to be too soft and low, this script comes to the rescue. Connect your earphones via Bluetooth, and your voice will be transmitted clearly through the speakers or projector, accompanying your presentation slides.

- **Karaoke:** For the singing enthusiasts who lack a dedicated karaoke system, simply plug your laptop into your TV, select your favorite karaoke track on YouTube, and sing your heart out.

## 3. Installation

Please note that while this script is designed to work across different platforms (Mac OSX, Linux, and Windows), it has been primarily tested on MacOSX.

Before you can use the script, you need to install two dependencies. Open your terminal and run the following commands:

```bash
$ pip install sounddevice
$ pip install numpy
```

## 4. Usage

Once you've installed the necessary dependencies, you can start using the script:

```bash
$ python3 main.py
```

Upon running the script, you will be prompted to select both the input (microphone) and output (speakers) devices from a list of available devices on your laptop. Ensure your desired devices are connected to your laptop before running the script.

Here's what the selection interface looks like:

```
AVAILABLE INPUT DEVICES:
====================
  0 LC34G55T, Core Audio (0 in, 2 out)
< 1 BlackHole 2ch, Core Audio (2 in, 2 out)
> 2 External Microphone, Core Audio (1 in, 0 out)
  3 External Headphones, Core Audio (0 in, 2 out)
  4 Mac mini Speakers, Core Audio (0 in, 2 out)

====================

Select an input device:
```

In this example, you can choose input device 2 (External Microphone) and output device 0 (speakers on an external monitor). Once your selection is made, return to your laptop, do whatever you want to do, whether it's giving a slideshow presentation or enjoying a karaoke session. Your microphone input will be seamlessly mixed and played through the selected output device.

## 5. Disclaimer

A few important points to note:

- You use this script at your own risk. The developer takes no responsibility for any damage or adverse effects caused by the use of this script.
- The script is simple and may have bugs. 

## 6. Troubleshooting on MacOSX

Please be aware that MacOSX's security system might restrict the script's access to audio devices. If you encounter any issues, follow these steps to grant the necessary permissions:

1. Open your System Settings.

2. Navigate to **Privacy & Security**.

3. Choose **Microphone** from the left-hand menu.

4. Locate **Terminal** in the list of applications and ensure it's turned on. This grants the script permission to access your microphone.

With these settings adjusted, your script should function as expected without any interruptions.

## 7. Credits

This README and the script were generated with the assistance of ChatGPT3.5 (free version). Kudos to the AI wizardry behind it for making this project possible!

Enjoy your audio adventures!
