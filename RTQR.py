import cv2
import zbarlight
from PIL import Image


def main():
    # Start capture video
    capture = cv2.VideoCapture(0)
    code = None

    while True:
        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Breaks down the video into frames
        ret, frame = capture.read()

        # Displays the current frame
        cv2.imshow('QR Decode', frame)

        # Converts image to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Uses PIL to convert the grayscale image into a ndary array that ZBar can understand.
        image = Image.fromarray(gray)
        codes = zbarlight.scan_codes('qrcode', image)

        if codes:
            code = codes
            break

    print(code)


if __name__ == "__main__":
    main()
