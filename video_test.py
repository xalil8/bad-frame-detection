import cv2

def save_frame(frame, count):
    filename = f"weird_frame{count}.jpg"
    cv2.imwrite(filename, frame)
    print(f"Saved {filename}")


def main():
    video_path = "bad_frame.mp4"
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create VideoWriter object to save the resulting video
    output_video = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'mp4v'),fps, (width, 930-60))

    temp_sum= 0
    counter = 0
    temp_frame = None

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame = frame[60:930,:]

        print(frame.shape)
        #for first frame we pass and assing into temp value 
        if counter ==0:
            temp_frame = frame
            counter += 1
            sum1 = sum(cv2.sumElems(frame))
            temp_sum = sum1
            continue

        #frame = frame[60:930, :]

        sum1 = sum(cv2.sumElems(frame))
        diff = abs(sum1 - temp_sum)
        temp_sum = sum1
        ratio = diff/(1920*(1080-(930-60)))


        print(f"frame{counter}",round(ratio,2))
        counter += 1

        if ratio > 38:
            try:
                save_frame(frame, counter)
                cv2.putText(frame, "BROKEN FRAME", (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 8)
                print("BROKEN FRAME DETECTED")
            except Exception as e:
                print("Error occurred while saving frame:", e)

        cv2.imshow("Video", frame)
        key = cv2.waitKey(1)
    
        if key == ord('q'):
            break
        output_video.write(frame)
        temp_frame = frame
    output_video.release()
    cap.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

