import cv2;
#Read The Image Data.
image=cv2.imread('picture.png');
#Write The Image Data.
cv2.imwrite('picture1.jpg', image);
#Load Grey Scale
gray_image=cv2.imread('picture.png', cv2.IMREAD_GRAYSCALE);
cv2.imwrite('picture2.jpg', gray_image);

gray_image=cv2.imread('picture.png', cv2.IMREAD_REDUCED_GRAYSCALE_2);
cv2.imwrite('picture3.jpg', gray_image);

gray_image=cv2.imread('picture.png', cv2.IMREAD_REDUCED_GRAYSCALE_4);
cv2.imwrite('picture4.jpg', gray_image);

gray_image=cv2.imread('picture.png', cv2.IMREAD_REDUCED_GRAYSCALE_8);
cv2.imwrite('picture5.jpg', gray_image);
