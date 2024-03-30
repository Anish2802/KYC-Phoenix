import cv2
from ultralytics import YOLO
import time
def id_capture():
    model = YOLO(r"D:\Hackathons\standard_chartered\website\weights\id_recog.pt")
    cap = cv2.VideoCapture(0)
    f=0
    while cap.isOpened():
        success, frame = cap.read()
        f=f+1

        if success:
            results = model.track(frame, conf=0.90, persist=True)

            coord_list = results[0].boxes.data.tolist()
            try:
                x1 = int(coord_list[0][0])
                y1 = int(coord_list[0][1])
                x2 = int(coord_list[0][2])
                y2 = int(coord_list[0][3])
                id=coord_list[0][4]
                classes=coord_list[0][6]
                confid=coord_list[0][5]
                cord = (x1, y1, x2, y2)
                roi = frame[y1:y2, x1:x2]
                if classes==0.0:
                    print("aadhar")
                    # cv2.imwrite(f"D:/Hackathons/standard_chartered/website/test_web/aadhar_img1/img.jpg", roi)
                    # D:\Hackathons\standard_chartered\website\test_web\face_img
                elif classes==1.0:
                    print("pan")
                    cv2.imwrite(f"D:/Hackathons/standard_chartered/website/test_web/xp/img.jpg", roi)
                    #D:/Hackathons/standard_chartered/website/test_web/face_img/img.jpg
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
    return "id uploaded"