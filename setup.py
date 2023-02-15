import importlib
import subprocess
import os
import shutil

# Windows Check
if not os.path.exists("C:/"):
    print("The installer and RapydFramework itself are made only for the Windows OS for now. Stay tuned for a Linux fork.")
    quit()

# Install required Python modules
required_modules = ["requests", "regex"]
for item in required_modules:
    try:
        importlib.import_module(item)
        print("{} is already installed.".format(item))
    except ImportError:
        subprocess.Popen(["pip", "install", item, "--user"])
        print("{} was installed.".format(item))

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
    
# Install RapydScript-ng
subprocess.run(["npm.cmd", "install", "-g", "rapydscript-ng"], env=os.environ)
print("RapydScript-ng installed/updated.")

# Install eslint
subprocess.run(["npm.cmd", "install", "-g", "eslint"], env=os.environ)
print("eslint installed/updated.")

# Creates the global folder
if not os.path.exists("C:/rapydframework"):
	os.makedirs("C:/rapydframework")
else:
	shutil.rmtree("C:/rapydframework")
	os.makedirs("C:/rapydframework")

os.makedirs("C:/rapydframework/rapydml")
os.makedirs("C:/rapydframework/rapydframework")

# Installs RapydFramework and RapydMl
subprocess.run(["git", "clone", "https://github.com/savethekiddes/RapydML-ng", "C:/rapydframework/rapydml"])
subprocess.run(["git", "clone", "https://github.com/savethekiddes/rapydframework", "C:/rapydframework/rapydframework"])



