#! /usr/bin/bash

echo '#' `date`

echo "# Atualizando o índice PyPL"
cd /home/eleno/Dropbox/Lorena/Website/LOM3260/material/sobre
bash cron-script.sh

echo "# Atualizando o site no Github..."
cd /home/eleno/Dropbox/Lorena/Website/LOM3260
rake build
rake commit

echo "Done!"
