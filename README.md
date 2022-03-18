# Code Repo: Detection of Mirrors in 3D Scenes from 2D Images
_AJ Arnolie, Chunwei Chen, and Youngbae Son_

March 2022

## Abstract
Here, we investigate the effect of mirrors in the 3D scene understanding and implement ways to mitigate the existing limitation. Using commercial RGBD sensors, we first show that the presence of mirrors pose challenge for 3D reconstruction, as it is difficult to differentiate mirrored scene from the actual scene using RGB data, and the depth measurements on the mirrors are often inaccurate. Then, we implement Mirror3DNet which uses CNN to detect and segment the mirror from the scene and apply this method to the exactly same RGBD data that showed inaccurate depth sensing from the mirrors. With the captured dataset, we show that this method can be implemented to avoid mirror-induced depth estimation error from the scene.

## Code Setup
After you clone this repo, run ***git submodule update --init --recursive*** to initiate another clone for mirror3d repo.

## Mirror3DNet

In order to set up this module, simply follow the instructions in the README of the Mirror3DNet Github repo.
1) Clone the module and submodules of the Mirror3D module (DPT, GLPDepth, BTS, VTS) with `git clone --recursive https://github.com/3dlg-hcvc/mirror3d.git`
2) Set up Detectron2 with `python -m pip install git+https://github.com/facebookresearch/detectron2.git`
3) Install necessary packages for Mirror3DNet with `cd mirror3d && pip install -e .`.
4) Download the necessary checkpoints and input data with:
```
### Download all pretrained checkpoints
wget http://aspis.cmpt.sfu.ca/projects/mirrors/mirror3d_zip_release/checkpoint.zip
unzip checkpoint.zip

### Download network input json
wget http://aspis.cmpt.sfu.ca/projects/mirrors/mirror3d_zip_release/mirror3d_input.zip
unzip mirror3d_input.zip
```

## Azure Kinect Data

The code to visualize color and depth images is taken from the Azure Kinect Sensor SDK Github Repository (https://github.com/microsoft/Azure-Kinect-Sensor-SDK).
