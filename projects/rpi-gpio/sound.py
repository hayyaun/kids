import time

import RPi.GPIO as GPIO

# Pin configuration
BUZZER_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Create PWM instance
buzzer = GPIO.PWM(BUZZER_PIN, 440)  # Default frequency set to 440 Hz (A4 note)

try:
    # Start the buzzer with 50% duty cycle
    buzzer.start(50)

    # Play some notes
    notes = [440, 494, 523, 587, 659, 698, 784]  # A4, B4, C5, D5, E5, F5, G5
    durations = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0]  # seconds

    for note, duration in zip(notes, durations):
        buzzer.ChangeFrequency(note)  # Change frequency for each note
        time.sleep(duration)

    # Stop the buzzer
    buzzer.stop()

finally:
    GPIO.cleanup()
