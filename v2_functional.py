import cv2

def save_frame(frame, count):
    filename = f"bad_frame_test/weird_frame{count}.png"
    cv2.imwrite(filename, frame)
    print(f"Saved {filename}")



def bad_frame_detect(frame,previous_sum):

        sum1 = sum(cv2.sumElems(frame))
        diff = abs(sum1 - previous_sum)
        previous_sum = sum1
        ratio = diff/(1920*1080) # 1920x1080 should be dimensions
        return ratio


def main():
    video_path = "demo2_short.mp4"
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create VideoWriter object to save the resulting video
    output_video = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'mp4v'),fps, (width,height))

    ######ESSENTIAL
    temp_sum= 0
    counter = 0
    init = True

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        ######ESSENTIAL
        if init:
            init = False
            sum1 = sum(cv2.sumElems(frame))
            temp_sum = sum1
            continue


        ######ESSENTIAL
        ratio = bad_frame_detect(frame,temp_sum)
        if ratio >4:
             continue


        print(f"frame{counter}",round(ratio,2))
        counter += 1

        ######ESSENTIAL

        cv2.imshow("Video", frame)
        key = cv2.waitKey(1)
    
        if key == ord('q'):
            break
        
        output_video.write(frame)

    output_video.release()
    cap.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

