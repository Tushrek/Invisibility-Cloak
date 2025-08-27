# Invisibility Cloak using OpenCV 🧙‍♂️

This project uses Python and the OpenCV library to create a real-time "invisibility cloak" effect. By detecting a specific color (in this case, red) and replacing it with a pre-captured background, the script creates the illusion that the object covered by the red cloak is invisible.

---

## Demonstration



The script first captures a static background. Then, when a red object enters the frame, the red pixels are replaced by the background, making it seem transparent.

---

## Features

-   **Real-time video processing** using your webcam.
-   **Stable background capture** by calculating the median of multiple frames.
-   **Robust color detection** for the color red in the HSV color space.
-   **Image masking** to segment the cloak from the rest of the frame.
-   **Morphological transformations** to reduce noise and improve the mask quality.

---

## Requirements

You'll need the following libraries to run the script:
-   Python 3.x
-   OpenCV-Python
-   NumPy

---

## Installation

1.  **Clone the repository (or download `Cloak.py`):**
    ```bash
    https://github.com/Tushrek/Invisibility-Cloak.git
    cd invisibility-cloak
    ```

2.  **Install the required libraries using pip:**
    ```bash
    pip install opencv-python numpy
    ```

---

## How to Use

1.  **Run the script from your terminal:**
    ```bash
    python Cloak.py
    ```

2.  **Capture the background:** The script will start by capturing the background. Make sure the area is clear of any red objects (or yourself!) for about 3-5 seconds. The console will print `Background captured successfully!`.

3.  **Use the cloak:** Once the background is captured, you can bring a red-colored cloth or object into the frame. The area covered by the red cloth will now appear "invisible," showing the background behind it.

4.  **Exit the application:** Press the **ESC** key to close the video window and terminate the script.
