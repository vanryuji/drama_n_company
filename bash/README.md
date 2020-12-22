# Overview
유용한 bash command 모음

# Command
* dpkg -l | grep php | awk '{print $2}' | tr "\n" " "
* $(dirname $0)
* $(cd $(dirname $(dirname $0)); pwd -P)
* screen : https://erwinousy.medium.com/screen-command-%EC%82%AC%EC%9A%A9%EB%B2%95-linux-mac-62bf5dd23110
