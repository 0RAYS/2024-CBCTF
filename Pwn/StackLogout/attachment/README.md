
#!/bin/zsh
sudo pip uninstall questionary qiling -y
sudo apt update
sudo apt-mark hold libc6
sudo apt install ipython3 -y
sudo pip install --upgrade prompt_toolkit
# ubuntu:noble-20240423
