# Overview
유용한 bash command 모음

# Command
* dpkg -l | grep php | awk '{print $2}' | tr "\n" " "
* $(dirname $0)
* $(cd $(dirname $(dirname $0)); pwd -P)
