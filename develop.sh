echo "** activating virtual environment **"
source venv/bin/activate
export FLASK_DEBUG=1
export MAIL_SERVER=localhost
export MAIL_PORT=8025
echo "** MAIL_SERVER is being redirected to localhost:8025 **"
# flask run
echo "** you may want to\n\t python -m smtpd -n -c DebuggingServer localhost:8025\n **"
# echo "'run' or 'shell'"
flask $1 $2 $3 $4 $5 $6 $7 $8 $9
