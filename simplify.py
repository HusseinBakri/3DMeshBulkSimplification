#!/usr/bin/python3
# Author: Hussein Bakri
import os
import sys
import inspect
import meshlabxml as mlx
import platform
import shutil

'''
Description: A Python tool that simplify or decimate a 3D Model/Mesh (textured or not) into a lower resolution model.
Requirements: Installing Meshlab on the OS + Python3 Package called meshlabxml
            sudo pip3 install meshlabxml 
Usage: python3 simplify.py Original_Mesh_NameOrPath Output_Mesh_NameOrPath Number_Of_Faces TexturesPresentFlag.
Original_Mesh_NameOrPath: Name.Extension if Python script is in the path of 3D models, Use Path otherwise.
Output_Mesh_NameOrPath: Name.Extension if Python script is in the path of 3D models, Use Path otherwise.
Number_Of_Faces: The final number of faces you want to achieve.
TexturesPresentFlag: True or False. If 3D mesh is tectured you have to use True.

Supported Meshes Types are the ones supported normally by Meshlab (.obj, ply etc...).
Meshlab unfortunately till now, does not support .gltf files yet. This might change in the future.

Example: python3 simplify.py Hat.obj Hat_Simplified.obj 150000 True
'''


# Location of Meshlab server (meshlabserver.exe) is normally in Windows 64 Bit installation inside: C:\Program Files\VCG\MeshLab\
# Location of Meshlab server is normally in Mac OS inside: /Applications/meshlab.app/Contents/MacOS/meshlabserver
# Location of Meshlab server in a Linux system Ex Fedora 27 in /usr/bin/meshlabserver (install Meshlab in Fedora 27 as 'sudo dnf install meshlab')
# Otherwise Please change accordingly

THIS_SCRIPTPATH = os.path.dirname(os.path.realpath(inspect.getsourcefile(lambda: 0)))
os.chdir(THIS_SCRIPTPATH)
# ml_version = '2016.12'

# Adding the meshlabserver directory to OS PATH;
print('\n Detecting Meshlab server Hosting Operating System ...')
if(platform.system()=='Windows'):
    print('\n You appear to be on Windows machine ...')
    meshlabserver_path = 'C:\\Program Files\\VCG\\MeshLab'

elif(platform.system()=='Linux'):
    print('\n You appear to be on Linux machine ...')
    meshlabserver_path = '/usr/bin/meshlabserver'

elif(platform.system()=='Darwin'):
    #We are on a Mac OS
    print('\n You appear to be on Mac machine ...')
    meshlabserver_path = '/Applications/meshlab.app/Contents/MacOS/meshlabserver'

else:
    print('\n Unknown OS please set the PATH manually ...')
    print('\n Decimantion might not work ...')

os.environ['PATH'] = meshlabserver_path + os.pathsep + os.environ['PATH']


print ('Number of Arguments Given to the script:', len(sys.argv), 'arguments.')


# File names
FilterScript = 'SimplificationFilter.mlx'  # script file
original_mesh = str(sys.argv[1])  # input file
simplified_mesh = str(sys.argv[2])  # output file
Num_Of_Faces = int(sys.argv[3])  # Final Number of Faces

if(sys.argv[4].lower() == 'false' or sys.argv[4] == '0'):
            TexturesFlag = False 	# Texture Flag
elif(sys.argv[4].lower() == 'true' or sys.argv[4] == '1'):
	TexturesFlag = True	# Texture Flag

print ('TexturesFlag:', TexturesFlag)

#Do the models have textures?
#TexturesFlag=True

#Check the input mesh number of faces (so that we do not decimate to a higher number of faces than original mesh)
MetricsMeshDictionary = {}
MetricsMeshDictionary = mlx.files.measure_topology(original_mesh)
#print (MetricsMeshDictionary)
print('\n Number of faces of original mesh is: ' + str(MetricsMeshDictionary['face_num'] )) 

if(MetricsMeshDictionary['face_num'] <= Num_Of_Faces):
    #exit the script and print a message about it
    print("\n SORRY your decimated mesh can not have higher number of faces that the input mesh.....")
    print("\n ......................................................................................")
    sys.exit()

#Creating a folder named as the Number of faces: named '150000'
print('\n Creating a folder to store the decimated model ...........')
if not os.path.exists(str(Num_Of_Faces)):
    os.makedirs(str(Num_Of_Faces))


simplified_meshScript = mlx.FilterScript(file_in=original_mesh, file_out=str(Num_Of_Faces) + '/' + simplified_mesh,
                                         ml_version='2016.12')  # Create FilterScript object

mlx.remesh.simplify(simplified_meshScript, texture=TexturesFlag, faces=Num_Of_Faces,
                    target_perc=0.0, quality_thr=1.0, preserve_boundary=True,
                    boundary_weight=1.0, preserve_normal=True,
                    optimal_placement=True, planar_quadric=True,
                    selected=False, extra_tex_coord_weight=1.0)
print('\n Beginning the process of Decimation ...........')

simplified_meshScript.run_script()  # Run the script
os.chdir(str(Num_Of_Faces))
print('\n Process of Decimation Finished ...')
print('\n Copying textures (PNG and JPEG) into the folder of decimated model....')

#go back to parent directory so we can copy the textures to the 3D Model folder
os.chdir('..')

#Now checking for textures in the folder of the input mesh.... (plz change if needed)
allfilelist= os.listdir('.')

for Afile in allfilelist[:]: 
    if not(Afile.endswith(".png") or Afile.endswith(".PNG") or Afile.endswith(".jpg") or Afile.endswith(".JPG")):
        allfilelist.remove(Afile)
print('\n Found the LIST of images in PNG and JPEG (textures): ')
print(allfilelist)

for file in allfilelist:
    shutil.copy(file, str(Num_Of_Faces))
