import cv2

def save_frame(frame, count):
    filename = f"deneme_{count}.png"
    cv2.imwrite(filename, frame)
    print(f"Saved {filename}")

def main():
    video_path = "demo2.mp4"
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video file")
        return

    count = 0

    counter = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break
        counter += 1


        cv2.imshow("Video", frame)
        key = cv2.waitKey(100)

   

        if key == ord('s'):
            save_frame(frame, count)
            count += 1
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
