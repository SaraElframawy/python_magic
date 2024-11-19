import cv2
import numpy as np
import pyautogui
def take_video_screen():
    screen_width, screen_height = pyautogui.size()
    resolution = (screen_width, screen_height)

    output_file = "scree_recording.mp4"
    # frame per second
    fbs = 30.0
    fourcc = cv2.VideoWriter.fourcc(*"mp4v")
    out = cv2.VideoWriter(output_file, fourcc, fbs, resolution)
    recording_duration = 5
    for _ in range(int(fbs * recording_duration)):
        screen = pyautogui.screenshot()
        # convert the screenshot to a numpy array
        frame = np.array(screen)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

    out.release()
take_video_screen()
