import cv2

cap = cv2.VideoCapture(0) # 0 para webcam padrão

while True:
    ret, frame = cap.read()

    if not ret: break

    # 1. transforma em Cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 2. Detecção de Bordas (Canny)
    edges = cv2.Canny(gray, 100, 200)

    cv2.imshow('Original', frame)
    cv2.imshow('Bordas (OpenCV)', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'): # aperta Q para encerrar
        break

cap.release()
cv2.destroyAllWindows()