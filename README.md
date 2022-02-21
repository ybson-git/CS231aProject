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

