import importlib
import subprocess
import os
import shutil

# Windows Check
if not os.path.exists("C:/"):
    print("The installer and RapydFramework itself are made only for the Windows OS for now. Stay tuned for a Linux fork.")
    quit()

# Check if Node is installed
try:
    result = subprocess.run(["where", "npm"], capture_output=True, check=True, env=os.environ)
except subprocess.CalledProcessError:
    print("Node is not in PATH. Are you sure that is installed?")
    quit()

# Check if Sass is installed 
try:
    result = subprocess.run(["where", "sass"], capture_output=True, check=True, env=os.environ)
except subprocess.CalledProcessError:
    print("Sass is not in PATH. Are you sure that is installed?")
    quit()

# Check if GIT is installed 
try:
    result = subprocess.run(["where", "git"], capture_output=True, check=True, env=os.environ)
except subprocess.CalledProcessError:
    print("GIT is not in PATH. Are you sure that is installed?")
    quit()

# Install required Python modules
required_modules = ["requests", "regex", "PyInstaller", "flask"]
for item in required_modules:
    try:
        importlib.import_module(item)
        print("{} is already installed.".format(item))
    except ImportError:
        subprocess.Popen(["pip", "install", item, "--user"])
        print("{} was installed.".format(item))

# Install required Node modules
node_modules = ["eslint", "minify", "webpack", "webpack-cli", "pwa-asset-generator"]
for item in node_modules:
    try:
        result = subprocess.run(["where", item], capture_output=True, check=True, env=os.environ)
        print("{} is already installed.".format(item))
    except subprocess.CalledProcessError:
        subprocess.Popen(["npm.cmd", "install", "-g", item,])
        print("{} was installed.".format(item))

# Install RapydScript-ng
subprocess.run(["npm.cmd", "install", "-g", "rapydscript-ng"], env=os.environ)
print("RapydScript-ng installed/updated.")

# Creates the global folder
if not os.path.exists("C:/rapydframework"):
	os.makedirs("C:/rapydframework")
else:
    for root, dirs, files in os.walk("C:/rapydframework"):
        for dir in dirs:
            os.chmod(os.path.join(root, dir), 0o777)
        for file in files:
            os.chmod(os.path.join(root, file), 0o777) 
    shutil.rmtree("C:/rapydframework")
    os.makedirs("C:/rapydframework")

os.makedirs("C:/rapydframework/rapydml")
os.makedirs("C:/rapydframework/src")

# Installs RapydFramework and RapydMl
subprocess.run(["git", "clone", "https://github.com/savethekiddes/RapydML-ng", "C:/rapydframework/rapydml"])
subprocess.run(["git", "clone", "https://github.com/savethekiddes/rapydframework", "C:/rapydframework/src"])

# Package the RapydFramework into an executable
import PyInstaller.__main__
script_path = 'C:/rapydframework/src/rapydframework.py'
options = [
    '--onefile',  # Package the script as a single executable
    '--console',  # Create a console application
    '--name=RapydFramework',  # Set the name of the executable
]
PyInstaller.__main__.run([
    *options,
    f"""--distpath={'C:/rapydframework'}""",
    script_path
])

# Announces succesfull installation
print("RapydFramework was installed/updated successfully")
