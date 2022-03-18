# Code Repo: Detection of Mirrors in 3D Scenes from 2D Images
_AJ Arnolie, Chunwei Chen, and Youngbae Son_

March 2022

## Abstract
Here, we investigate the effect of mirrors in the 3D scene understanding and implement ways to mitigate the existing limitation. Using commercial RGBD sensors, we first show that the presence of mirrors pose challenge for 3D reconstruction, as it is difficult to differentiate mirrored scene from the actual scene using RGB data, and the depth measurements on the mirrors are often inaccurate. Then, we implement Mirror3DNet which uses CNN to detect and segment the mirror from the scene and apply this method to the exactly same RGBD data that showed inaccurate depth sensing from the mirrors. With the captured dataset, we show that this method can be implemented to avoid mirror-induced depth estimation error from the scene.

## Code Setup
After you clone this repo, run ***git submodule update --init --recursive*** to initiate another clone for Open3D and mirror3d repos.
<!-- 
## Open3D_TrueDepth_registration
It looks like the auther is using Linux, if you have same machine just follow steps: https://github.com/nghiaho12/Open3D_TrueDepth_registration  

If you are using MacOS, M1 chip, like me, here is what I did:  
 - Install brew: https://brew.sh/  
 - Install ceres-solver and eigen: http://ceres-solver.org/installation.html  
 - Follow the auther to install python libraries using pip3.  
 - Note I don't use Ananconda as it created environment for x86_64 but when I build cpp it is arm64, results in incompatible.  
 - Build cpp pose graph file with the Open3D repo instruction.  
 - Back to Open3D root, run *python3 run.py ../Open3D_box_can/*, you should see it runs.   -->

## Mirror3DNet

In order to set up this module, simply follow the instructions in the README of the Mirror3DNet Github repo.
1) You will need to download the necessary checkpoints.
2) Clone the submodules of the Mirror3D module (DPT, GLPDepth, BTS, VTS)

<!-- If you are using M1 mac, the python and packages may not work as given. Sharing my configuration:

"pip install -e ." command may not work right away. 

1) conda install python=3.9.6  (also tried 3.8.11)
2) I could not install open3d and h5py as-given. You need to first delete these two packages from the setup.py in the mirror3d dir.
3) pip install -e .
4) (Instead of using the script given) CC=clang CXX=clang++ ARCHFLAGS="-arch arm64" python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
5) to install open3d : pip install open3d

(The below steps will downgrade numpy from 1.22.2 to 1.20.3) -> But this is where numpy starts to not work in the environment. (Import error) 
6) to install pytorch: conda install pytorch torchvision -c pytorch
7) to install h5py: conda install h5py
8) to install tensorboard: conda install tensorboard
 -->
## Kinect
The code to visualize color and depth images taken from Azure Kinect.
