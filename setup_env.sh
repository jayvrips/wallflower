
# must run this with sudo


apt-get install -y python3

apt-get install -y sqlite3

# pip3
apt-get install -y curl
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

# sqlalchemy
pip3 install sqlalchemy

rm get-pip.py

tar xzf view/web/static/deps.tgz -C view/web/static 

