# ESRF_Files
Modified ESRF scripts such as concentration correction

To acces the data go to https://remote.esrf.fr and log in with your user account. 
Search for:   Compute cluster > slurm > pick one of the slurm-nice-devels for example slurm-nice-devel2904 and
log in again with your user account (you might wait a moment untill it is fully loaded).

Our data path on the esrf server: /data/visitor/hc4929/id26/

For more scrips or the un modified version go to https://confluence.esrf.fr/pages/viewpage.action?pageId=50765632.
The official page that proviedes a multitude of scripts for the data analyses.


To run the scrips type in the consol:  
yourusername@slurm-nice-devel2904:~ % module load conda  
yourusername@slurm-nice-devel2904:~ % module load spectroscopy  

The consol shuld change to something like this:  
(/sware/exp/packages/ubuntu20.04/x86_64/spectroscopy/2022.02.15) yourusername@slurm-nice-devel2904:~ % 

Type in:  
yourusername@slurm-nice-devel2904:~ % ipython3

To check if the module is loaded use:  
In [1]: import daxs

Executing a file can be done as followed:  
In [2]: exec(open('filepath/example1.py').read())

If you are you download the file you can acces it with from the download folder by using:   
In [3]: exec(open('Downloads/daxs_xes_EH2_cc_copper.py').read())
