echo " -- removing Python cache --"
rm -rf */__pycache__
rm -rf */*/__pycache__
rm -rf __pycache__

echo " -- removing Python virtual environment --"
rm -rf venv
