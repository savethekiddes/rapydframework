# Imports
import argparse
import os
import subprocess
import shutil
import sys
import re

print("RapydFramework, the easy way for client development")

# Defines arguments
parser = argparse.ArgumentParser()
action = parser.add_mutually_exclusive_group()
action.add_argument("-i", "--init", action="store_true", help="creates a new project")
action.add_argument("-c", "--compile", action="store_true", help="compiles a project")
action.add_argument("-r", "--run", action="store_true", help="starts a Flask dev server")
parser.add_argument("--tailwind", action="store_true", help="adds Tailwind support, to be used with the --init argument")
parser.add_argument("-t", "--test", action="store_true", help="tests the code for errors, to be used with the --compile argument")
args = parser.parse_args()

# Strikes down phantom arguments
if not args.compile and args.test:
	print("You can't use the --test argument without the --compile argument, please see -h or --help")
	sys.exit()

if not args.init and args.tailwind:
	print("You can't use the --tailwind argument without the --init argument, please see -h or --help")
	sys.exit()

# Project initation
if args.init:

	# Makes the source tree
	src = ["src/styles", "src/components", "src/scripts"]
	for item in src:
		if not os.path.exists(item):
			os.makedirs(item)
			print("The '{}' folder was created".format(item))
		else:
			print(
				"A folder called '{}' already exists. That could mean that another project is already here.".format(item)
			)
			sys.exit()

	# Creates the presets
	templates_path = "C:/rapydframework/src/templates/"
	def template(path):
		return templates_path + path + ".template"
	with open(template("pyml"), "r") as f:
		pyml = f.read()
	with open(template("pyj"), "r") as f:
		pyj = f.read()
	with open(template("sass"), "r") as f:
		sass = f.read()
	with open(template("readme"), "r") as f:
		readme = f.read()
	with open(template("eslint"), "r") as f:
		eslint = f.read()
	with open(template("tailwind"), "r") as f:
		tailwind = f.read()
	with open(template("gitignore"), "r") as f:
		gitignore = f.read()
  
	with open("src/app.pyml", "w") as f:
		f.write(pyml)
	with open("src/styles/index.sass", "w") as f:
		f.write(sass)
	with open("src/scripts/main.pyj", "w") as f:
		f.write(pyj)
	with open(".eslintrc.json", "w") as f:
		f.write(eslint)
	with open(".gitignore", "w") as f:
		f.write(gitignore)
	with open("README.md", "w") as f:
		f.write(readme)

	if args.tailwind:
		with open(template("tailwind"), "r") as f:
			tailwind = f.read()
		with open("tailwind.config.js", "w") as t:
			t.write(tailwind)

	print ("A new project was generated.")
	# Terminates the initiation
	sys.exit()


# Project compilation
if args.compile:

	# Makes the build tree
	if not os.path.exists("build/"):
		os.makedirs("build/")
	else:
		shutil.rmtree("build/")
		os.makedirs("build/")
	if not os.path.exists("temp/"):
		os.makedirs("temp/")
	else:
		shutil.rmtree("temp/")
		os.makedirs("temp/")

	# Copies the source tree to build
	src_folder = "src/"
	build_folder = "build/"
	for root, dirs, files in os.walk(src_folder):
		for dir in dirs:
			src_path = os.path.join(root, dir).replace("\\", "/")
			build_path = src_path.replace(src_folder, build_folder, 1)
			if not os.path.exists(build_path):
				# Check if the current file is a directory
				if os.path.isdir(src_path):
					os.makedirs(build_path)

	# Copies all the files that don't have to be compiled to build
	def has_extension(filename, ext_list):
		_, ext = os.path.splitext(filename)
		return ext.lower() in [e.lower() for e in ext_list]
	ext_list = [".pyml", ".sass", ".pyj"]
	for root, dirs, files in os.walk("src/"):
		for file in files:
			if not has_extension(file, ext_list):
				src_path = os.path.join(root, file).replace("\\", "/")
				build_path = src_path.replace("src/", "build/")
				shutil.copy2(src_path, build_path)

	# Modifies source imports with compiled ones
	src_folder = "src/"
	build_folder = "temp/"
	for root, dirs, files in os.walk(src_folder):
		for dir in dirs:
			src_path = os.path.join(root, dir).replace("\\", "/")
			build_path = src_path.replace(src_folder, build_folder, 1)
			if not os.path.exists(build_path):
				if os.path.isdir(src_path):
					os.makedirs(build_path)

	for root, dirs, files in os.walk("src/"):
		for file in files:
			if file.endswith(".pyml"):
				srcpath = os.path.join(root, file).replace("\\", "/")
				pymlpath = srcpath.replace("src/", "temp/")
				shutil.copy2(srcpath, pymlpath)
				with open(pymlpath, "r") as f:
					contents = f.read()
				contents = re.sub(r'(["\']).*\.pyj.*(\1)', lambda m: m.group(1) + m.group()[1:-1].replace(".pyj", ".js") + m.group(2), contents)
				contents = re.sub(r'(["\']).*\.sass.*(\1)', lambda m: m.group(1) + m.group()[1:-1].replace(".sass", ".css") + m.group(2), contents)
				contents = re.sub(r'(["\']).*\.pyml.*(\1)', lambda m: m.group(1) + m.group()[1:-1].replace(".pyml", ".html") + m.group(2), contents)
				with open(pymlpath, "w") as f:
					f.write(contents)
     
	# Compiles Python Markdown to HTML
	for root, dirs, files in os.walk("temp/"):
		for file in files:
			if file.endswith(".pyml"):
				pymlpath = os.path.join(root, file).replace("\\", "/")
				compilepath = os.path.abspath(pymlpath)
				subprocess.run(["python", "C:/rapydframework/rapydml/rapydml.py", "--rapydframework", compilepath], env=os.environ)
				print("{} compiled to HTML".format(pymlpath.replace("temp/", "src/")))

	# Compiles RapydScript files to JavaScript ones
	for root, dirs, files in os.walk("src/"):
		for file in files:
			if file.endswith(".pyj"):
				pyjpath = os.path.join(root, file).replace("\\", "/")
				jspath = pyjpath.replace("src/", "build/").replace(".pyj", ".js")
				with open(jspath, "w") as f:
					f.write("")
				subprocess.Popen(["rapydscript.cmd", pyjpath, "-o", jspath], env=os.environ)
				print("{} compiled to JavaScript".format(pyjpath))

	# Compiles Sass files to CSS ones
	for root, dirs, files in os.walk("src/"):
		for file in files:
			if file.endswith(".sass"):
				sasspath = os.path.join(root, file).replace("\\", "/")
				csspath = sasspath.replace("src/", "build/").replace(".sass", ".css")
				with open(csspath, "w") as f:
					f.write("")
				subprocess.Popen(["sass.exe", sasspath, csspath], env=os.environ)
				print("{} compiled to CSS".format(sasspath))



	# Copies the html files to the build folder
	for root, dirs, files in os.walk("temp/"):
		for file in files:
				if file.endswith(".html"):
					htmlpath = os.path.join(root, file).replace("\\", "/")

					# Tailwind support
					if os.path.exists("tailwind.config.js"):
						with open(htmlpath, "a") as lol:
							lol.write('<script src="https://cdn.tailwindcss.com"></script>\n')
							lol.write('<script>\n')
							with open("tailwind.config.js", "r") as x:
								twconfig = x.read()
							lol.write("{}".format(twconfig))
							lol.write("\n")
							lol.write("</script>")
					
					# Jailbreaked component support

					# Standard component support
					with open(htmlpath, "r") as r:
						content = r.read()
					with open(htmlpath, 'r') as f:
						lines = f.readlines()
					regex = r'<rapydfw:component\s+src="([^"]+)"?'
					matches = re.findall(regex, content)

					for match in matches:
						with open("temp/" + match, "r") as f:
							comptext = f.read()
						content = content.replace(f'<rapydfw:component src="{match}" />', comptext)
						content = re.sub(regex, '', content)

					with open(htmlpath, "w") as w:
						w.write(content)

					# Nested component support
					with open(htmlpath, "r") as r:
						content = r.read()
					with open(htmlpath, 'r') as f:
						lines = f.readlines()
					regex = r'<rapydfw:nested\s+src="([^"]+)"?'
					matches = re.findall(regex, content)

					for match in matches:
						with open("temp/" + match, "r") as f:
							comptext = f.read()
						content = content.replace(f'<rapydfw:nested src="{match}" />', '<iframe style="border: none; margin: 0; padding: 0;" srcdoc="' + comptext + '"></iframe>')
						content = re.sub(regex, '', content)

					with open(htmlpath, "w") as w:
						w.write(content)


					# Commit to build
					buildpath = htmlpath.replace("temp/", "build/")
					shutil.copy2(htmlpath, buildpath)

    # Tests the built javascript
	if args.test:
		for root, dirs, files in os.walk("build/"):
			for file in files:
				if file.endswith(".js"):
					testfile = os.path.join(root, file)
					result = subprocess.run(["eslint.cmd", testfile, "-c", ".eslintrc.json"], 
						stdout=subprocess.PIPE, 
						stderr=subprocess.PIPE,
						env=os.environ)
					print(result.stdout.decode())
					print(result.stderr.decode(), file=sys.stderr)
    
    # Deletes the temporary files
	shutil.rmtree("temp/")
 
	sys.exit()

# Development server
if args.run:
	if not os.path.exists("build/"):
		print("The project wasn't built first. Please run RapydFramework with the --compile option first!")
		sys.exit()
	if not os.path.exists("dev/"):
		os.makedirs("dev/")
	if not os.path.exists("dev/devserver.py"):
		templates_path = "C:/rapydframework/src/templates/"
		def template(path):
			return templates_path + path + ".template"
		with open(template("devserver"), "r") as f:
			devserver = f.read()
		with open ("dev/devserver.py", "w") as f:
			f.write(devserver)
	print("Starting a Flask development server...")
	os.chdir('dev')
	subprocess.run(["python", "devserver.py"])
	sys.exit()


print("No argument submitted, please see -h or --help")