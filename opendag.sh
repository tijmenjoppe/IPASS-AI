#!/bin/bash

# Bash script to install demo projects on Linux
# Tijmen Muller (tijmen.muller@hu.nl)

# Exit on error
set -e

echo Updating locales...
sudo update-locale "LANG=en_US.UTF-8"
sudo locale-gen --purge "en_US.UTF-8"
sudo dpkg-reconfigure --front-end noninteractive locales

echo Updating packages...
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get dist-upgrade
sudo apt autoremove

echo Installing extra packages...
sudo apt-get install dselect
sudo apt-get install firefox-esr
sudo apt-get install python3-pil.imagetk

echo Installing Python libraries...
pip install pygame
pip install imdbpy
pip install requests
pip install termcolor

echo Downloading demonstraton projects...

mkdir -p ~/workspace
cd ~/workspace

git clone https://github.com/tijmenjoppe/IPASS_MovieEnjoymentPredictor
git clone https://github.com/tijmenjoppe/IPASS_MazeGame
git clone https://github.com/tijmenjoppe/IPASS_Rummi
git clone https://github.com/tijmenjoppe/IPASS_VierOpEenRij
git clone https://github.com/tijmenjoppe/IPASS_Scrabble
