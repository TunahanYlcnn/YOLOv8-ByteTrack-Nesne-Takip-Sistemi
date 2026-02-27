import cv2
import numpy as np
from ultralytics import YOLO
from bytetrack1.byte_tracker import BYTETracker
from types import SimpleNamespace

args = SimpleNamespace(
    track_thresh=0.2,
    match_thresh=0.8,
    track_buffer=30,
    mot20 = False
)
tracker = BYTETracker(args, frame_rate=30)

cap = cv2.VideoCapture("VİDEO_YOLU.mp4")
model = YOLO("YOLO_MODELİ_AĞILRILIK_DOSYASI.pt", verbose= False)
model.to("cuda") 

frame_id = 0
target_id = None 

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_id += 1
    h, w, _ = frame.shape
    img_size = (h, w)
    results = model(frame, verbose= False)[0]
    detections = []

    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
        conf = box.conf[0].cpu().item()
        detections.append([x1, y1, x2, y2, conf])

    detections = np.array(detections)
    
    if detections.shape[0] > 0:
        online_targets = tracker.update(detections, frame, img_size)

        if len(online_targets) > 0:
            for t in online_targets:
                tlwh = t.tlwh
                tid = t.track_id
                x, y, w, h = tlwh

                if target_id is None:
                    target_id = tid
                    print(f"🎯 Kilitlenilen hedef ID: {target_id}")

               
                if tid == target_id:
                    print(f"🎯 Takip edilen hedef ID: {tid}") # Konsol kirliliği olmaması için yoruma alınabilir
                    cv2.rectangle(frame, (int(x), int(y)), (int(x + w), int(y + h)), (0,0,255), 2)
                    cv2.putText(frame, f'TARGET ID:{tid}', (int(x), int(y) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

    cv2.imshow("YOLOv8 + ByteTrack", frame)
    
    # ESC tuşu ile çıkış
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()