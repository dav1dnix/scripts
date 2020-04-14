#!/bin/sh
areass() { 
    gnome-screenshot -a -c && xclip -selection clipboard -t image/png -o > /tmp/image.png
    curl -F'file=@/tmp/image.png' http://0x0.st | xclip -selection clipboard
}
areass
