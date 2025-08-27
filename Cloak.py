import cv2
import numpy as np
import time

capture_video = cv2.VideoCapture(0)

if not capture_video.isOpened():
    print("Error: Could not open your webcam.")
    exit()

print("Camera warming up...")
time.sleep(3)

background_frames = []
for i in range(60):
    ret, frame = capture_video.read()
    if ret:
        frame = np.flip(frame, axis=1)
        background_frames.append(frame)
    time.sleep(0.05)

if not background_frames:
    print("Error: Failed to capture background frames. Please check your camera.")
    capture_video.release()
    exit()

background = np.median(background_frames, axis=0).astype(np.uint8)
print("Background captured successfully! You can now step into the frame with your red cloak.")

while capture_video.isOpened():
    return_val, img = capture_video.read()
    if not return_val:
        break

    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red_1 = np.array([0, 120, 70])
    upper_red_1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)

    lower_red_2 = np.array([170, 120, 70])
    upper_red_2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red_2, upper_red_2)

    mask_red = mask1 + mask2

    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask_red = cv2.dilate(mask_red, np.ones((3, 3), np.uint8), iterations=1)
    mask_not_red = cv2.bitwise_not(mask_red)

    res1 = cv2.bitwise_and(img, img, mask=mask_not_red)
    res2 = cv2.bitwise_and(background, background, mask=mask_red)

    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisible Man", final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break

capture_video.release()
cv2.destroyAllWindows()