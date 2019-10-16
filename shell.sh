#!/bin/bash
sed -i "38 s|<h3>.*</h3>|<h3>"$1"</h3>|" html/index.html
sudo docker cp html/index.html cont:/usr/share/nginx/html/
sed -i '2 s|\(.*\):".*"\(.*\)|\1:"'$1'"\2|' c.js
mongo < c.js
