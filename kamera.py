import cv2
import numpy as np

# Kamera qurilmasini yoqish
cap = cv2.VideoCapture(0)  # 0 - asosiy kamera, 1 - birinchi qo'shimcha kamera, va hokazo

while True:
    # Kameradan tasvir olish
    ret, frame = cap.read()

    # Ekran yorug'ligini olish
    brightness = np.mean(frame)

    # Ekran yorug'ligini chiqarish
    print("Ekran yorug'ligi:", brightness)

    # Tasvirlarni ekranga chiqarish
    cv2.imshow("Ekran yorug'ligi", frame)

    # 'q' tugmasi bosilganda dasturni to'xtatish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerani qo'llashni to'xtatish
cap.release()

# Barcha oynalarni yopish
cv2.destroyAllWindows()

