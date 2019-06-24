# Description
A Meshlab (http://www.meshlab.net/) Python 3 tool to simplify or decimate a 3D Model/Mesh  (With and Without Textures) into a lower resolution mesh taking a specific Number of Faces using the MeshlabXML Library (https://github.com/3DLIRIOUS/MeshLabXML).

The Python tool take a CLI arguments the original mesh, Decimated mesh, target resolution in number of faces and Whether the 3D model is textured or not.

The tool also detects the Operating System (OS) you are using and then sets the PATH accordingly  (at least the default places where Meshlabserver normally resides on MS Windows, Mac OS and Linux (like Fedora 27) (Side Note: Meshlabserver is installed with Meshlab itself). In case you are using another Operating System, please change accordingly. The tool do not decimate above the original resolution. The tool creates a folder (named as the target resolution) for each resolution and copy all the textures of original model to it.

Two versions for bulk decimations are included: one with a threading mechanism and another without threading. With threading, the duration of decimation is considerably reduced, this might be an important consideration for you for the case when you need to generate a lot of lower resolutions' models in bulk and in tandem.

This tool and [BlenderPythonDecimator](https://github.com/HusseinBakri/BlenderPythonDecimator) allow you to decimate a 3D mesh into lower resolutions.

# Requirements
Installing Meshlab on the Operating System + Installing a Python3 Package called meshlabxml by per example 'sudo pip3 install meshlabxml' or from MeshlabXML repo.

As a better approach, always when it comes to Python and its modules, it is advisable to create a Python virtual environment for your application and install through pip any module required in that particular virtual environment. From my experience, this gives no headache!


# Usage           
python3 simplify.py Original_Mesh_NameOrPath Output_Mesh_NameOrPath Number_Of_Faces TexturesPresentFlag

Original_Mesh_NameOrPath: Name.Extension if Python script is in the path of 3D models, Use Path otherwise

Output_Mesh_NameOrPath: Name.Extension if Python script is in the path of 3D models, Use Path otherwise

Number_Of_Faces: The final number of decimation you want to achieve

TexturesPresentFlag: True or False. If 3D mesh is tectured you have to use True.

Supported Meshes Types are the ones that are normally supported by Meshlab (.obj, ply etc...)
Meshlab unfortunately till now, does not support .gltf files yet. This might change in the future.

[NB] Please check the other python scripts (simplifybulknothreading.py and simplifybulkthreaded.py) for the right way to use them.

# Example 
python3 simplify.py Hat.obj Hat_Simplified.obj 150000 True

# Meshlab GUI similarity VS My Python code
The simplification done here mimick "exactly" what you can do in the GUI filter of Meshlab. We are using the Quadric Edge Collapse algorithm preserving UV parametrisations. Meshlab implements the algorithm of Garland and Heckbert (1997, 1998) [1,2] with minor alterations (have a look at the source code of Meshlab to learn more how it is implemented - good exercice for the students of Computer Graphics course out there!).

![alt text](http://url/to/img.png)

The parameters in the figure above (from my experience) produce the most optimum decimated i.e. simplified model. You can of course play around with these parameters and see what works best for you. The following Python code in my scripts is responsible for setting these parameters as required.

```
mlx.remesh.simplify(simplified_meshScript, texture=TexturesFlag, faces=Num_Of_Faces,
                    target_perc=0.0, quality_thr=1.0, preserve_boundary=True,
                    boundary_weight=1.0, preserve_normal=True,
                    optimal_placement=True, planar_quadric=True,
                    selected=False, extra_tex_coord_weight=1.0)
```


# Annoying Problem of cannot connect to X server in headless Linux server
Now this tools is tested on Mac OS High Sierra, Linux Fedora 27 and MS Windows 10. Works fine. Please contact me if you find bugs.
The problem you might encounter happens when you want to use Meshlab Server on a Linux/Unix Headless (meaning no GUI no X Server).

You might get the following error: Problem: meshlabserver: cannot connect to X server

That problem caused me a lot of headache when I was using this solution to bulk decimate models on Ubuntu Server 16.04. First you need to install xserver (solution below - similar technique for other Linux distros):
```
sudo apt-get install xserver-xorg xserver-xorg-core x11-apps x11-xserver-utils
Xvfb :99 &
export DISPLAY=:99

xvfb-run python3 simplify.py Hat.obj Hat_Simplified.obj 150000 True
```
# Nope Hussein! did not Work! give me other solutions Please
1) change the source code of Meshlab itself. Search for QApplication and put QCoreApplication instead of QApplication
see this for more info: https://sourceforge.net/p/meshlab/discussion/499532/thread/6c3eebe2/
2) Better: I created another Python Tool that do the decimation with impressive results using Blender Python API. It works as a complete headless solution like a charm! Have a look at https://github.com/HusseinBakri/BlenderPythonDecimator.

# References
[1] Garland, Michael, and Paul S. Heckbert. "Surface simplification using quadric error metrics." Proceedings of the 24th annual conference on Computer graphics and interactive techniques. ACM Press/Addison-Wesley Publishing Co., 1997.

[2] Garland, Michael, and Paul S. Heckbert. "Simplifying surfaces with color and texture using quadric error metrics." Proceedings Visualization'98 (Cat. No. 98CB36276). IEEE, 1998.

# License
This program is licensed under MIT License - you are free to distribute, change, enhance and include any of the code of this application in your tools. I only expect adequate attribution and citation of this work. The attribution should include the title of the program, the author and the site or the document where the program is taken from.
