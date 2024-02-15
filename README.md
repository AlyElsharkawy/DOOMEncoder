# DOOMEncoder
A simple symmetric encryption program created in Python while I was in high school. **Simple, secure, robust,and efficient.**

## Features
- Full unicode support.
- Security: duplicate keys are nearly impossible to generate.
- Compatibility: Works on Windows, Mac, and Linux.
- Tab Completion: All commands and their aliases can be completing by pressing the tab key

## Usage
The program is launched by running `DOOMEncoder.py` from any terminal. The program will then accept any of four commands:
1. Encode
2. Decode
3. Generate Key
4. Quit

Typing the `encode` or `decode` commands will then cause the program to ask for a key. A key can be generated by typing the `generate key` command. Also, the `back` command can be used to return to any previous menu.

## Installation
_Note: Make sure git and python are installed beforehand!_
**Windows:**
If you are windows, then the installation is as simple as cloning the git repository, installing the dependencies, and then running the script
```Bash
git clone https://github.com/AlyElsharkawy/DOOMEncoder.git
cd .\DOOMEncoder
pip install -r .\requirements.txt
```

**Linux**
Installation on linux varies a bit between distributions. This is because `pyperclip`,the package used to copy outputs to the system clipboard, requires xclip. Xclip is not included by default.These are the install instructions for any Ubuntu/Debian, RPM, and Arch based distribution:
1. Ubuntu/Debian
- ```Bash
     git clone https://github.com/AlyElsharkawy/DOOMEncoder.git
     cd ./DOOMEncoder
     pip install -r ./requirements.txt
     sudo apt install xclip
     ```
2. Fedora
   - ```Bash
     git clone https://github.com/AlyElsharkawy/DOOMEncoder.git
     cd ./DOOMEncoder
     pip install -r ./requirements.txt
     sudo dnf install xclip readline-devel
     ```
3. Arch
- ```Bash
   git clone https://github.com/AlyElsharkawy/DOOMEncoder.git
   cd ./DOOMEncoder
   sudo pacman -Sy xclip readline python-pyperclip
   ```

