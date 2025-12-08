# Information for compiling
Some of these files have dependencies that require installation before compilation.

I created these files to be run in a virtual environment to get around the pip3 "externally-managed-environment" error.
You can run them the same way I did by following these steps.

Current additional dependencies vary by file, but within this repo include: astropy, matplotlib, scipy.


1. Set up the virtual environment. Within your project directory, open terminal and enter:

```python3 -m venv <your_project_name>  ```
For the LaPlace files, the code must be run with version >= Python3.10, < Python14.0.
Create another VE with the following command:
```python3.10 -m venv <your_project_name2>```
With these files, keep the terminal with your VE2 open.
Run each file from the command line:
```python3 <yourFile.py>```

2. Activate the environment, telling your computer to "look there" for the files.

```source <your_project_name>/bin/activate ```

3. Install the dependency in the new virtual environment:

*For pde, prereqs include: tqdm, numba, and sympy. (and numpy if not autoinstalled when installing numba)
**py-pde may be a preerq to install pde.

```pip3 install <dependency name>```

4. Check your install

```pip3 list```

5. When you're done, deactivate the virtual environment

```deactivate```

6. To restart the environment, repeat step 2 within your project directory.