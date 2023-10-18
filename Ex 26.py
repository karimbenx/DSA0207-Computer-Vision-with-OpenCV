import cv2
img = cv2.imread("C:/Users/Merwin S/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/TempState/32508F53F24C46F685870A075EAAA29C/WhatsApp Image 2023-10-16 at 13.54.13_220efe45.jpg")
wm = cv2.imread("C:/Users/Merwin S/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/TempState/60106888F8977B71E1F15DB7BC9A88D1/WhatsApp Image 2023-10-16 at 13.54.12_99a5e57c.jpg")
h_wm, w_wm = wm.shape[:2]
h_img, w_img = img.shape[:2]
center_x = int(w_img/2)
center_y = int(h_img/2)
top_y = center_y - int(h_wm/2)
left_x = center_x - int(w_wm/2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm
roi = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(roi, 1, wm, 0.3, 0)
img[top_y:bottom_y, left_x:right_x] = result
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

 
