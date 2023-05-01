# natural_language

# python 

```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip python3.10-dev -y
```
# env

```bash
virtualenv -p python3.10 virtualenv -p python3.10 /Users/arthurtestard/envs/nlenv
````
```bash
source ${HOME}/envs/nlenv
pip3.10 install -r requirements.txt
```

# Upgrade pip version (necessary if "cannot import name 'html5lib'" error)
wget https://bootstrap.pypa.io/get-pip.py
python3.10 get-pip.py
python3.10 -m pip install --upgrade pip
rm get-pip.py

# Source 

http://aima.cs.berkeley.edu/