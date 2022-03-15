#!/bin/bash

# Bash script om demo's te installeren op een Raspberry Pi
# Tijmen Muller (tijmen.muller@hu.nl)

echo Updating locales...
sudo dpkg-reconfigure locales

echo Updating packages...

echo Installing extra packages
sudo apt-get install dselect
sudo apt-get

echo Installing Python libraries...
pip install pygame
pip install imdbpy
pip install requests

echo Downloading demonstraton projects...

mkdir ~/workspace
cd ~/workspace

git clone https://github.com/tijmenjoppe/IPASS_MovieEnjoymentPredictor
git clone https://github.com/tijmenjoppe/IPASS_MazeGame
git clone https://github.com/tijmenjoppe/IPASS_Rummi
git clone https://github.com/tijmenjoppe/IPASS_VierOpEenRij
