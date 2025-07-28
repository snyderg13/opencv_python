import cv2
import sys

def main():
    print("Hello from opencv-test!")
    
    # @TODO: figure out how to get better detect
    #        available cams and choose desired
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Err: Could not open cam")
        sys.exit(1)
    
    print("Cam opened successfully")
    
    # @TODO: err/exc handling to get more info
    #        about the failure
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Err: failed to read frame")
            break

        cv2.imshow("Cam Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;

    cap.release()
    cv2.destroyAllWindows()

    print("Done with first test")


if __name__ == "__main__":
    main()
