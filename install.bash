#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

welcome() {
    echo -e "${RED}Welcome to Metro-API!${NC}"
    echo -e "This guide will deployt the backend on your system."
    echo -e "Please follow the instructions carefully."
    echo -e ""
}

archlinux() {
    echo -e "${RED}Installing dependencies...${NC}"
    sudo pacman -Syyu --noconfirm
    sudo pacman -S --noconfirm --needed git python python-pip python-virtualenv
    echo -e "${GREEN}Dependencies installed.${NC}"
}

ubuntu() {
    echo -e "${RED}Installing dependencies...${NC}"
    sudo apt-get update
    sudo apt-get upgrade -y
    sudo apt-get install -y git python3 python3-pip python3-virtualenv
    echo -e "${GREEN}Dependencies installed.${NC}"
}

fedora() {
    echo -e "${RED}Installing dependencies...${NC}"
    sudo dnf update
    sudo dnf install -y git python3 python3-pip python3-virtualenv
    echo -e "${GREEN}Dependencies installed.${NC}"
}

termux() {
    echo -e "${RED}Installing dependencies...${NC}"
    apt update -y
    apt upgrade -y
    apt install python -y
    pip3 install virtualenv
    echo -e "${GREEN}Dependencies installed.${NC}"
}

other_os() {
    echo -e "${RED}Please install the dependencies manually.${NC}"
    echo -e "${GREEN}Dependencies:${NC}"
    echo -e "${GREEN}1. Python Version 3+${NC}"
    echo -e "${GREEN}2. Git${NC}"
    echo -e "${GREEN}3. Python3-pip${NC}"
}

check_os() {
    echo -e "${RED}What is your OS?${NC}"
    echo -e "${RED}(Please select 4, if you already have dependencies.)${NC}"
    echo -e "${GREEN}Enter 1 for Ubuntu/Debian${NC}"
    echo -e "${GREEN}Enter 2 for Arch/Manjaro${NC}"
    echo -e "${GREEN}Enter 3 for fedora${NC}"
    echo -e "${GREEN}Enter 4 for other${NC}"
    read os

    if [ $os == "1" ]; then
        ubuntu
    elif [ $os == "2" ]; then
        archlinux
    elif [ $os == "3" ]; then
        fedora
    elif [ $os == "4" ]; then
        termux
    elif [ $os == "5" ]; then
        other_os
    else
        echo -e "${RED}Invalid option.${NC}"
        check_os
    fi
}

# Check python virtual environment
check_venv() {
    if [ ! -d ".venv" ]; then
        echo -e "${RED}Python virtual environment not found. Installing...${NC}"
        python3 -m venv .venv
        check_venv
    else
        echo -e "${GREEN}Python virtual environment found.${NC}"
        source .venv/bin/activate
        echo -e "${GREEN}Python virtual environment activated.${NC}"
    fi
}

# Install requirements
install_requirements() {
    echo -e "${RED}Installing requirements...${NC}"
    pip install -r requirements.txt
    echo -e "${GREEN}Requirements installed.${NC}"
}

# Run all functions
run() {
    clear
    uvicorn main:app --reload
}

welcome
check_os
check_dir
check_venv
install_requirements
run