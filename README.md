**Disclaimer: this is still in beta, if not in alpha**

# RapydFramework, the easy for client development
RapydFramework is an easy way to develop web apps using your Python skills. At his core, however, it's just a
way to generate and compile projects that use RapydML, RapydScript and Sass (all technologies that have a heavily 
inspired or heavily similar syntax to Python). That allows you to make cross-platform clients by just learning an
easy language and little more.

# Installation
RapydFramework needs for these dependencies to be installed manually:
- [Python](https://www.python.org/) (with pip)
- [NodeJS](https://nodejs.org/)
- [Sass](https://sass-lang.com/)
- [GIT](https://https://git-scm.com/)


RapydFramework for now is only for Windows. I have to confess that I don't have high incentives to make a Linux
version (or worse, a Mac), so forking is encouraged. To install or update the package, just paste this command
in the command prompt:

    powershell -command "Invoke-WebRequest -UseBasicParsing https://raw.githubusercontent.com/savethekiddes/rapydframework/main/setup.py -OutFile setup.py; python setup.py"

# About PATH
Some installers of Node.js don't add the "npm" folder to PATH. This is a problem, because then RapydScript-ng (the
Python-like implementation of JavaScript) will not work. If rapydscript.py returns a FileNotFoundError when trying
to compile RapydScript, then run this in a command prompt as administrator::

    setx PATH "%PATH%;%APPDATA%/npm"

You might also to consider to add RapydFramework to PATH to avoid always writing the absolute PATH:

    setx PATH "%PATH%;C:/rapydframework"

If you do this, to call RapydScript you'll use:

    rapydframework

Instead of:

    C:/rapydframework/rapydframework.exe

# Usage
To get started, you can just type the following command:

    C:/rapydframework/rapydframework.exe -h

The output will be the following:

    RapydFramework, the easy way for client development
    usage: rapydframework [-h] [-i | -c] [-t]

    options:
      -h, --help     show this help message and exit
      -i, --init     creates a new project
      -c, --compile  compiles a project
      -t, --test     tests the code for errors, to be used with the --compile argument

# Credits
The credits of course go to:
- [atsepkov](https://github.com/atsepkov/), for making the original RapydML and RapydScript
- [kovidgoyal](https://github.com/kovidgoyal/), for forking RapydScript and make it live again
- [The SASS's developers](https://github.com/sass/), for making easier writing CSS

Awesome work, thanks to all of you!