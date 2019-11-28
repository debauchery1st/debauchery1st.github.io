echo " ** activating python virtual environment **"
source venv/bin/activate

echo "** upgrading database models**"
flask db upgrade
