import cv2
import os
import time

person_name = "ali"   # change for each person
save_path = f"dataset/train/{person_name}"

os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)  # try 0,1,2 depending on camera

count = 0
max_images = 200

print("Starting automatic capture...")

while count < max_images:
    ret, frame = cap.read()

    if not ret:
        print("Camera not detected")
        break

    cv2.imshow("Capturing Images", frame)

    filename = f"{save_path}/{count}.jpg"
    cv2.imwrite(filename, frame)

    print(f"Saved {filename}")

    count += 1

    time.sleep(0.05)   # small delay so images aren't identical

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

print("Finished capturing images")
