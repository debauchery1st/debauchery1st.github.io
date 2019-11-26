echo " ** creating python virtual environment **"
python3 -m venv venv

echo " ** activating python virtual environment **"
source venv/bin/activate

echo " ** installing wheels **"
pip install wheel

echo " ** installing requirements **"
pip install -r requirements.txt

echo " ** starting application **"
flask run
