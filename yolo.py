import cv2
import numpy as np
import motor
import time
def Start_Detection(key):
    cap=cv2.VideoCapture("/dev/video0",cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    a=1
    while cv2.waitKey(33) < 0:
        ref,frame=cap.read()
        if ref:
            
            if key==1 and a==3:
                frame=cv2.resize(frame,(640,480) )
                print(frame.shape)
                cv2.imwrite("/home/ezlife/ezlife/code/testimg.jpg",frame)
                break
        a=a+1
# 웹캠 신호 받기
# YOLO 가중치 파일과 CFG 파일 로드
    YOLO_net = cv2.dnn.readNet("/home/ezlife/ezlife/code/yolov4_20000.weights","/home/ezlife/ezlife/code/yolov4.cfg")

# YOLO NETWORK 재구성
    classes = []
    with open("/home/ezlife/ezlife/code/obj.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = YOLO_net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in YOLO_net.getUnconnectedOutLayers()]

    # 웹캠 프레임
    img = cv2.imread("/home/ezlife/ezlife/code/testimg.jpg")
    h, w, c = img.shape

    # YOLO 입력
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0),
    True, crop=False)
    YOLO_net.setInput(blob)
    outs = YOLO_net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []

    for out in outs:

        for detection in out:

            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.8:
                # Object detected
                center_x = int(detection[0] * w)
                center_y = int(detection[1] * h)
                dw = int(detection[2] * w)
                dh = int(detection[3] * h)
            # Rectangle coordinate
                x = int(center_x - dw / 2)
                y = int(center_y - dh / 2)
                boxes.append([x, y, dw, dh])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.45, 0.4)
    judgment=[]
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            score = confidences[i]
            confidence=str(round(confidences[i],2))
            # 경계상자와 클래스 정보 이미지에 입력
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(img, label + ""+confidence, (x, y - 10), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 1)
            print(label,confidence)
            judgment.insert(i,label)
    cv2.imshow("YOLOV4", img)
    if not judgment:
        motor.Send_MG('8')
        motor.Start_Separate("return")
        print("It cannot find object.")
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
        return 0
    box=judgment[0]
    print(box)
    for i in judgment:
        if box!=i:
            print("하나이상의 쓰레기가 투입되었습니다.")
            possible = 0
            motor.Send_MG('8')
            motor.Start_Separate("return") 
            cv2.waitKey(3000)
            cv2.destroyAllWindows()
            break
        elif box==i:
            possible = 1
    if possible==1:
        motor.Send_MG('7')
        print("분리수거를 시작합니다.")
        motor.Start_Separate(box) 
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
