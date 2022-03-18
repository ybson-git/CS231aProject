from PIL import Image
import numpy as np
import os

data_path = "../custom_data4"
f = "IMG_5482.jpg"

img_p = os.path.join(data_path, "downsampled_images", f)
BTSdepth_p = os.path.join(data_path, "BTS_depth", f.split(".")[0] + ".png")
VNLdepth_p = os.path.join(data_path, "VNL_depth", f.split(".")[0] + ".png")
GLPdepth_p = os.path.join(data_path, "GLP_depth", f.split(".")[0] + ".png")
DPTdepth_p = os.path.join(data_path, "DPT_depth", f.split(".")[0] + ".png")

pts = [[233, 170], [177, 455], [100, 360]]

img = Image.open(img_p)

d = np.asarray(Image.open(BTSdepth_p)).copy()
print("BTS:", [d[p[0]][p[1]] for p in pts])

d = np.asarray(Image.open(VNLdepth_p)).copy()
print("VNL:", [d[p[0]][p[1]] for p in pts])

d = np.asarray(Image.open(GLPdepth_p)).copy()
print("GLP:", [d[p[0]][p[1]] for p in pts])

d = np.asarray(Image.open(DPTdepth_p)).copy()
print("DPT:", [d[p[0]][p[1]] for p in pts])
