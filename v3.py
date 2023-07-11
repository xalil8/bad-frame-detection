import cv2
import numpy as np
import threading

class FrameProcessor:
    def __init__(self, video_path, threshold=38):
        self.video_path = video_path
        self.threshold = threshold
        self.frame = None
        self.previous_frame = None
        self.frame_counter = 0

    def read_video(self):
        self.cap = cv2.VideoCapture(self.video_path)
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def calculate_frame_difference(self):
        if self.previous_frame is not None:
            sum1 = sum(cv2.sumElems(self.frame))
            sum0 = sum(cv2.sumElems(self.previous_frame))
            diff = abs(sum1 - sum0)
            ratio = diff / (self.width * self.height)
            return ratio
        else:
            return 0

    def process_frame(self):
        ratio = self.calculate_frame_difference()
        print(f"Frame {self.frame_counter}", round(ratio, 2))
        if ratio > self.threshold:
            self.save_frame(self.frame_counter)
            cv2.putText(self.frame, "BROKEN FRAME", (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 8)
            print("BROKEN FRAME DETECTED")

    def save_frame(self, count):
        filename = f"bad_frame_test/weird_frame{count}.png"
        cv2.imwrite(filename, self.frame)
        print(f"Saved {filename}")

    def process_video(self):
        self.read_video()
        while True:
            ret, self.frame = self.cap.read()
            if not ret:
                break

            threading.Thread(target=self.process_frame).start()
            self.previous_frame = self.frame
            self.frame_counter += 1

        self.cap.release()
        cv2.destroyAllWindows()

def main():
    fp = FrameProcessor("demo2.mp4")
    fp.process_video()

if __name__ == '__main__':
    main()
