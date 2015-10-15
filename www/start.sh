#!/bin/bash
# Diretorio e arquivo de log
set -e
LOGFILE=/home/philippe/projeto/api-django/Api-chat/www/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
# Numero de processo simultaneo, modifique de acordo com seu processador
NUM_WORKERS=3
# Usuario/Grupo que vai rodar o gunicorn
USER=myusr
#GROUP=root
# Endereço local que o gunicorn irá rodar
ADDRESS=127.0.0.1:8000
# Ativando ambiente virtual e executando o gunicorn para este projeto
source /home/philippe/projeto/api-django/lib/bin
cd /home/philippe/projeto/api-django/Api-chat/
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn -w $NUM_WORKERS --bind=$ADDRESS --user=$USER --log-level=debug --log-file=$LOGFILE 2>>$LOGFILE myproject.wsgi:application
