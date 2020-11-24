#!/usr/bin/env bash
# Script que ejecuta el archivo de configuracion de la base de datos
cat ./create_database | mysql -hlocalhost -uroot -p