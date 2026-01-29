"""

Virtual Environment:
- A Virtual Environment is an isolated environment that allows us to run
  Python projects with their own dependencies, Python version and installed 
  packages, independent of other projects or the system Python

Commands:

Create Virtual Environment:
python -m venv env_name

Activate Virtual Environment (Windows - PowerShell):
.\env_name\Scripts\Activate.ps1

Activate Virtual Environment (Windows - CMD):
env_name\Scripts\activate

Deactivate Virtual Environment:
deactivate

--------------------------------------------

Package Management:

Install a package:
pip install package_name

Uninstall a package:
pip uninstall package_name

List all installed packages:
pip list

Save installed packages to file:
pip freeze > requirements.txt

Install packages from file:
pip install -r requirements.txt

"""