# CS231aProject


## Virtual Environment (venv)
Use Conda to align Python environment, refer to https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html  

If you are using Mac M1 chip, then you can directly create your venv by environment_mac_m1.yml  

In case not compatible, here is step-by-step of dependencies to be installed through conda:  
 - conda create --name cs231a python=3.8  
 - conda activate cs231a  
 - conda install pytorch torchvision torchaudio -c pytorch  
 - conda install torchnet  
 - pip install torchnet  
 - pip install h5py  
Then you can create a environment yml file for your backup: *conda env export > your_venv.yml*  

## Test Code
Under Conda venv, nevigate to /3DMV-master/3dmv, and run *python train.py --help* and *python test.py --help* to see if can successfully see help instructions.  
