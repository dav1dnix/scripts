#!/bin/sh
areass() { 
    gnome-screenshot -a -c && xclip -selection clipboard -t image/png -o > /tmp/image.png
    curl -F'file=@/tmp/image.png' https://0x0.arikawa-hi.me | xclip -selection clipboard
}
areass
