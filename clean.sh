echo " -- removing Python cache --"
rm -rf app/__pycache__
rm -rf __pycache__
echo " -- removing Python virtual environment --"
rm -rf venv
echo " -- removing Python-C leftovers --"
rm *.pyc
rm */*.pyc
