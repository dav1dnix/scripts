#!/bin/sh
areass() {
  RANDOM="$(openssl rand -hex 2)"
  IMG="$RANDOM.png"
  maim -s --format=png /tmp/${IMG} | xclip -selection clipboard -t image/png
  sshpass -p "password" scp /tmp/${IMG} root@ipaddress:/var/domain # replace this with where you upload your images
  echo -n "https://domain/${IMG}" | xclip -selection c
}
areass
