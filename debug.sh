source venv/bin/activate
export FLASK_DEBUG=1
export MAIL_SERVER=localhost
export MAIL_PORT=8025
# flask run
# echo "you should run:\n\t python -m smtpd -n -c DebuggingServer localhost:8025"
echo "MAIL_SERVER is being redirected to localhost:8025"
# echo "'run' or 'shell'"
flask $1