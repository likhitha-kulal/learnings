import cv2

# Step 1: Start webcam
cap = cv2.VideoCapture(0)

# Step 2: Check if camera opened
if not cap.isOpened():
    print("Error: Cannot open webcam")
    exit()

while True:
    # Step 3: Read frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Can't receive frame")
        break

    # Step 4: Show frame
    cv2.imshow("Webcam Feed", frame)

    # Step 5: Detect key press
    key = cv2.waitKey(1) & 0xFF

    # Step 6: Exit condition
    if key == ord('q') or key == 27: 
        print("Closing webcam...")
        break

# Step 7: Release everything
cap.release()
cv2.destroyAllWindows()