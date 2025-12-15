# Information for compiling
Some of these files have dependencies that require installation before compilation.

I created these files to be run in a virtual environment to get around the pip3 "externally-managed-environment" error.
You can run them the same way I did by following the below steps.

Current additional dependencies vary by file, but within this repo include: astropy, matplotlib, scipy, specutils, glob2, rasterio, earthpy.

For the LaPlace files, the code must be run with version >= Python3.10, < Python14.0.
Additional build instructions are below, under "LaPlace Build Instructions."

For the satelliteImageryVisualizer.py file, I ran into issues with dependencies in my virtual environment. I used the "myVirtualEnv" environment as opposed to the "VEversion10" version. I installed additional dependencies including: setuptools.
Error: The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
Note to self and maybe you: this package install may need to be updated soon given the package's slated removal, be advised.


1. Set up the virtual environment. Within your project directory, open terminal and enter:

```python3 -m venv <your_project_name>  ```

2. Activate the environment, telling your computer to "look there" for the files.

```source <your_project_name>/bin/activate ```

3. Install the dependency in the new virtual environment:

```pip3 install <dependency name>```

4. Check your install

```pip3 list```

5. When you're done, deactivate the virtual environment

```deactivate```

6. To restart the environment, repeat step 2 within your project directory.

# Information for compiling LaPlace Files
1. Set up the virtual environment. Within your project directory, open terminal and enter:
For the LaPlace files, the code must be run with version >= Python3.10, < Python14.0.
Create another VE with the following command:

```python3.10 -m venv <your_project_name2>```

2. Activate the environment, telling your computer to "look there" for the files.

```source <your_project_name2>/bin/activate ```

3. Install the dependency in the new virtual environment:
The LaPlace files require 4 additional dependecies including pde. I had some issues getting this install to work.
For pde, prereqs include: tqdm, numba, and sympy (and numpy if not autoinstalled when installing numba), please install these first using the following command.

** Note: py-pde may be also prerequisite to install pde.

```pip3 install <dependency name>```

4. Check your install

```pip3 list```

5. Compile Files

With these files, keep the terminal with your new Virtual Environment open.
Run each file from that command line:

```python3 <yourFile.py>```

6. When you're done, deactivate the virtual environment

```deactivate```

7. To restart the environment, repeat step 2 within your project directory.

