"""Locate a translated synthetic target with OpenCV. Run directly as a self-check."""
import cv2
import numpy as np

def locate(frame, template):
    """Return the (x, y) origin of the best normalized template match."""
    scores = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, origin = cv2.minMaxLoc(scores)
    return origin

def example():
    target = np.zeros((17, 17), dtype=np.uint8)
    cv2.circle(target, (8, 8), 6, 180, 2)
    cv2.circle(target, (10, 6), 2, 255, -1)
    positions = [(15, 20), (23, 17)]
    detected = []
    for x, y in positions:
        frame = np.zeros((64, 80), dtype=np.uint8)
        frame[y:y+17, x:x+17] = target
        detected.append(locate(frame, target))
    assert detected == positions, detected
    (x0, y0), (x1, y1) = detected
    print(f"Target displacement: ({x1-x0}, {y1-y0}) pixels")

if __name__ == "__main__":
    example()
