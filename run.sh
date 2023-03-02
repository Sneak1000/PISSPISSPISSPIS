# if run.sh is present, it will be what runs when you press "Run"

# -q installs quietly
echo 'Installing things'
pip install -q -r requirements.txt

# then we have to manually run
python main.py
