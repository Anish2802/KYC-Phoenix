import cv2
from ultralytics import YOLO
import time
def capture():
    model = YOLO(r"D:\Hackathons\standard_chartered\website\weights\face_capture.pt")
    cap = cv2.VideoCapture(0)
    f=0
    while cap.isOpened():
        success, frame = cap.read()
        f=f+1

        if success:
            results = model.track(frame, conf=0.60, persist=True)

            coord_list = results[0].boxes.data.tolist()
            try:
                x1 = int(coord_list[0][0])
                y1 = int(coord_list[0][1])
                x2 = int(coord_list[0][2])
                y2 = int(coord_list[0][3])
                id=coord_list[0][4]
                confid=coord_list[0][5]
                cord = (x1, y1, x2, y2)
                roi = frame[y1:y2, x1:x2]
                cv2.imwrite(f"D:/Hackathons/standard_chartered/website/test_web/face_img/img.jpg", roi)
            except:
                pass
            annotated_frame = results[0].plot()
            cv2.imshow("YOLOv8 Tracking", annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    return "face uploaded"
# "D:\Hackathons\standard_chartered\website\test_web\face_img"