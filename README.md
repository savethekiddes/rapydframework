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


RapydFramework for now is only for Windows. I have to confess that I don't have high incentives to make a Linux
(or worse, a Mac version), so forking is encouraged. To install the package, just paste this command in the command
prompt:

    python -c "import os; os.system('curl -sSL https://raw.githubusercontent.com/savethekiddes/rapydframework/main/setup.py | python -')"

# About PATH
Some installers of Node.js don't add the "npm" folder to PATH. This is a problem, because then RapydScript-ng (the
Python-like implementation of JavaScript) will not work. If rapydscript.py return FileNotFoundError when trying
to fetch JavaScript, then run this command in a command prompt as administrator:

    setx PATH "%PATH%;%APPDATA%/npm"

You might also to consider to add RapydFramework to PATH to avoid boilerplate code:

    setx PATH "%PATH%;C:/rapydframework"

If you do this, to call RapydScript you'll use:

    rapydframework

Instead of:

    C:/rapydframework/rapydframework.exe