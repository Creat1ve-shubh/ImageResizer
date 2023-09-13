import cv2


image=cv2.imread("WhatsApp Image 2023-08-31 at 14.23.40.jpg", cv2.IMREAD_UNCHANGED)

if image is None:
    print("error:no image found")
else:
    print('Original Dimensions : ', image.shape)
x=input("what should the scale percent be?: ")
scale_percent = int(x)  # percent of original size

width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape)

cv2.imwrite("Resized_image.jpg", resized)
print("resized image saved as Resized_image.jpg")
cv2.waitKey(0)
cv2.destroyAllWindows()