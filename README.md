# Description
A Meshlab(http://www.meshlab.net/) Python 3 tool to simplify or decimate a 3D Model/Mesh  (With and Without Textures) into a lower resolution mesh taking a specific Number of Faces using the MeshlabXML Library (https://github.com/3DLIRIOUS/MeshLabXML).

The Python tool take a CLI arguments the original mesh, Decimated mesh, Decimated Mesh Number of Faces and Whether the 3D model is textured or not.

The tool also detects the Operating system you are using and then sets the PATH accordingly  (at least the default places where Meshlabserver normally resides on Windows, Mac OS and Linux (like Fedora 27) (Side Note: Meshlabserver is installed with Meshlab itself).
In case you are using another Operating System, please change accordingly.

# Requirements
Installing Meshlab on the Operating System + Installing a Python3 Package called meshlabxml by per example 'sudo pip3 install meshlabxml' or from MeshlabXML repo.

# Usage           
python3 simplify.py Original_Mesh_NameOrPath Output_Mesh_NameOrPath Number_Of_Faces TexturesPresentFlag

Original_Mesh_NameOrPath: Name.Extension if Python script is in the path of 3D models, Use Path otherwise

Output_Mesh_NameOrPath: Name.Extension if Python script is in the path of 3D models, Use Path otherwise

Number_Of_Faces: The final number of decimation you want to achieve

TexturesPresentFlag: True or False. If 3D mesh is tectured you have to use True.

Supported Meshes Types are the ones that are normally supported by Meshlab (.obj, ply etc...)
Meshlab unfortunately till now, does not support .gltf files yet. This might change in the future.

# Example 
python3 simplify.py Hat.obj Hat_Simplified.obj 150000 True
