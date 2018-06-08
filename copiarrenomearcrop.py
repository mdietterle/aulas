import glob
import shutil
import os
import cv2

src_dir = "C:\Python36-32\Scripts\downloads\pos\\bottlevodka"
dst_dir = "C:\Python36-32\Scripts\downloads\pos\\bottlevodka\\resized"
max_height = 500
max_width = 500
scaling_factor=1
for filefile in glob.iglob(os.path.join(src_dir, "*.*")):
    scaling_factor=1
    img = cv2.imread(filefile)
    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]
    if max_height < height or max_width < width:
    # get scaling factor
        scaling_factor = max_height / float(height)
    if max_width/float(width) < scaling_factor:
        scaling_factor = max_width / float(width)
    # resize image
    img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    cv2.imshow("Imagem",img)
    cv2.imwrite(filefile,img)
    shutil.copy2(filefile,dst_dir)