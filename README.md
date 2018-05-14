# Description
A Meshlab(http://www.meshlab.net/) Python 3 tool to simplify or decimate a 3D Model/Mesh  (With and Without Textures) into a lower resolution mesh taking a specific Number of Faces using the MeshlabXML Library (https://github.com/3DLIRIOUS/MeshLabXML).

# Requirements
Installing Meshlab on the OS + Python3 Package called meshlabxml by 'sudo pip3 install meshlabxml'

# Usage           
python3 simplify.py Original_Mesh_NameOrPath Output_Mesh_NameOrPath Number_Of_Faces TexturesPresentFlag

Original_Mesh_NameOrPath: Name.Extension if Python script is in the path of 3D models, Use Path otherwise

Output_Mesh_NameOrPath: Name.Extension if Python script is in the path of 3D models, Use Path otherwise

Number_Of_Faces: The final number of decimation you want to achieve

TexturesPresentFlag: True or False. If 3D mesh is tectured you have to use True.

Supported Meshes Types are the ones supported by Meshlab (.obj, ply etc...)
Meshlab unfortunately till now, does not support .gltf files yet. This might change in the future

# Usage 
python3 simplify.py Hat.obj Hat_Simplified.obj 150000 True
