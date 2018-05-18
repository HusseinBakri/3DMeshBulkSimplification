# Description
A Meshlab (http://www.meshlab.net/) Python 3 tool to simplify or decimate a 3D Model/Mesh  (With and Without Textures) into a lower resolution mesh taking a specific Number of Faces using the MeshlabXML Library (https://github.com/3DLIRIOUS/MeshLabXML).

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


# Annoying Problem of cannot connect to X server in headless Linux server
Now this tools is tested on Mac OS High Sierra, Linux Fedora 27 and MS Windows 10. Works fine. Please contact me if you find bugs.
The problem you might encounter happens when you want to use Meshlab Server on a Linux/Unix Headless (meaning no GUI no X Server).

You might get the following error: Problem: meshlabserver: cannot connect to X server

That problem caused me a lot of headache when I was using this solution to bulk decimate models on Ubuntu Server 16.04. First you need to install xserver (solution below - similar technique for other Linux distros):

sudo apt-get install xserver-xorg xserver-xorg-core x11-apps x11-xserver-utils
Xvfb :99 &
export DISPLAY=:99

xvfb-run python3 simplify.py Hat.obj Hat_Simplified.obj 150000 True

# Nope Hussein! did not Work! give me other solutions Please
1) change the source code of Meshlab itself. Search for QApplication and put QCoreApplication instead of QApplication
see this for more info: https://sourceforge.net/p/meshlab/discussion/499532/thread/6c3eebe2/
2) Better: I created another Python Tool that do the decimation with impressive results using Blender Python API. It works as a complete headless solution like a charm! Have a look at 



