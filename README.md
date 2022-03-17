# CS231aProject
After you clone this repo, run ***git submodule update --init --recursive*** to initiate another clone for Open3D and mirror3d repos.

## Open3D_TrueDepth_registration
It looks like the auther is using Linux, if you have same machine just follow steps: https://github.com/nghiaho12/Open3D_TrueDepth_registration  

If you are using MacOS, M1 chip, like me, here is what I did:  
 - Install brew: https://brew.sh/  
 - Install ceres-solver and eigen: http://ceres-solver.org/installation.html  
 - Follow the auther to install python libraries using pip3.  
 - Note I don't use Ananconda as it created environment for x86_64 but when I build cpp it is arm64, results in incompatible.  
 - Build cpp pose graph file with the Open3D repo instruction.  
 - Back to Open3D root, run *python3 run.py ../Open3D_box_can/*, you should see it runs.  

## mirror3d

If you are using M1 mac, the python and packages may not work as given. Sharing my configuration:

"pip install -e ." command may not work right away. 

1) conda install python=3.9.6  (also tried 3.8.11)
2) I could not install open3d and h5py as-given. You need to first delete these two packages from the setup.py in the mirror3d dir.
3) pip install -e .
4) (Instead of using the script given) CC=clang CXX=clang++ ARCHFLAGS="-arch arm64" python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
5) to install open3d : pip install open3d

(The below steps will downgrade numpy from 1.22.2 to 1.20.3) --> But this is where numpy starts to not work in the environment. (Import error) 
6) to install pytorch: conda install pytorch torchvision -c pytorch
7) to install h5py: conda install h5py
8) to install tensorboard: conda install tensorboard

## kinect
The code to visualize color and depth images taken from Azure Kinect.
