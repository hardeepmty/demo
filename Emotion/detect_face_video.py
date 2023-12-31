import cv2
from deepface import DeepFace

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(1)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, frame = cap.read()
    result = DeepFace.analyze(img_path=frame, actions=['emotion'], enforce_detection=False)[0]
    print(result)


    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    emotion = result['dominant_emotion']
    txt = str(emotion)

    cv2.putText(frame, txt, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)


    # Display
    cv2.imshow('frame', frame)

    

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()