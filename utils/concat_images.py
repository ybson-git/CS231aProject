from PIL import Image
import numpy as np
import os
import sys
np.set_printoptions(threshold=sys.maxsize)

data_path = "../chunwei_examples/kinect_mirror3"
new_dir = "concat_results_new"
os.makedirs(data_path + "/" + new_dir, exist_ok=True)
for f in sorted(os.listdir(os.path.join(data_path, "images"))):
    img_p = os.path.join(data_path, "downsampled_images", f)
    BTSdepth_p = os.path.join(data_path, "initial_depth", "BTS_depth", f.split(".")[0] + ".png")
    VNLdepth_p = os.path.join(data_path, "initial_depth", "VNL_depth", f.split(".")[0] + ".png")
    GLPdepth_p = os.path.join(data_path, "initial_depth", "GLP_depth", f.split(".")[0] + ".png")
    DPTdepth_p = os.path.join(data_path, "initial_depth", "DPT_depth", f.split(".")[0] + ".png")
    refined_p = os.path.join(data_path, "refined_depth", "refined_input_txt_pred_depth", f.split(".")[0] + ".png")
    print(img_p)
    img = Image.open(img_p)
    img.save(img_p.split(".")[0] + ".png")
    img = Image.open(img_p.split(".")[0] + ".png")
    BTSdepth = Image.open(BTSdepth_p)
    VNLdepth = Image.open(VNLdepth_p)
    GLPdepth = Image.open(GLPdepth_p)
    DPTdepth = Image.open(DPTdepth_p)
    refined = Image.open(refined_p)
    #BTSrefined = Image.open(refined_p)
    #VNLrefined = Image.open(VNLrefined_p)

    d = np.asarray(BTSdepth).copy()
    d -= np.amin(d)
    d = d / np.amax(d) * 255
    depth = Image.fromarray(d)

    d = np.asarray(VNLdepth).copy()
    d -= np.amin(d)
    d = d / np.amax(d) * 255
    depth2 = Image.fromarray(d)
    
    d = np.asarray(GLPdepth).copy()
    d -= np.amin(d)
    d = d / np.amax(d[30:]) * 255
    depth3 = Image.fromarray(d)

    d = np.asarray(DPTdepth).copy()
    d -= np.amin(d)
    d = 255 - (d / np.amax(d) * 255)
    depth4 = Image.fromarray(d)

    d = np.asarray(refined).copy()
    d -= np.amin(d)
    d = d / np.amax(d) * 255
    depth5 = Image.fromarray(d)

    # d = np.asarray(VNLrefined).copy()
    # d -= np.amin(d)
    # d = d / np.amax(d) * 255
    # depth4 = Image.fromarray(d)
    dst = Image.new('RGB', (img.width * 6, img.height))
    dst.paste(img, (0, 0))
    dst.paste(depth, (img.width, 0))
    dst.paste(depth2, (img.width * 2, 0))
    dst.paste(depth3, (img.width * 3, 0))
    dst.paste(depth4, (img.width * 4, 0))
    dst.paste(depth5, (img.width * 5, 0))
    dst.save(os.path.join(data_path, new_dir, f))
