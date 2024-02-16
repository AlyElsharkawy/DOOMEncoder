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

Note: Many aliases are supported for the above. For example, typing `decrypt` has the same effect as having typed in  `decode`. A list of the command alises is below
```bash
- decrypt
- encrypt
- generate hash
- generate combination
- exit
```

Typing the `encode` or `decode` commands will then cause the program to ask for a key. A key can be generated by typing the `generate key` command. Also, the `back` command can be used to return to any previous menu.

## Installation
**Note: Make sure git, python, g++, and gcc are installed beforehand!** On Ubuntu/Debian based distributions, this can usually be done by installing the `build-essential` package. 

## **Windows:**

If you are windows, then the installation is as simple as cloning the git repository, installing the dependencies, and then running the script
```Bash
git clone https://github.com/AlyElsharkawy/DOOMEncoder.git
cd .\DOOMEncoder
pip install -r .\requirements.txt
```

## **Linux**

Installation on linux varies a bit between distributions. This is because `pyperclip`, the package used to copy outputs to the system clipboard, requires xclip. Xclip is not included by default. Furthermore, the `readline` module created by the GNU project must be installed. These are the install instructions for any Ubuntu/Debian, RPM, and Arch based distribution:
1. Ubuntu/Debian
     ```Bash
     git clone https://github.com/AlyElsharkawy/DOOMEncoder.git
     cd ./DOOMEncoder
     pip install -r ./requirements.txt
     sudo apt install xclip libreadline-dev -y
     ```
2. Fedora
     ```Bash
     git clone https://github.com/AlyElsharkawy/DOOMEncoder.git
     cd ./DOOMEncoder
     pip install -r ./requirements.txt
     sudo dnf install xclip readline-devel -y
     ```
3. Arch
   ```Bash
   git clone https://github.com/AlyElsharkawy/DOOMEncoder.git
   cd ./DOOMEncoder
   sudo pacman -Sy xclip readline python-pyperclip --noconfirm
   ```
## Issues
If you find any issues or bugs while running the program, please open an issue in the issues tab.

