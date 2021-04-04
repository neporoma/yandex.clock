#!/bin/sh
#echo "Hello, Yandex!" >> data.txt
git pull https://github.com/neporoma/yandex.clock.git
docker restart nginx
