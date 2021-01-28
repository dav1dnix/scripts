# screenshot
## Screenshot an area, upload it and copy the domain with the image to clipboard.

## Dependencies
- maim
- xclip
- sshpass
- openssl (I think that comes with most Linux distributions anyway)

You could also rebind the Print key to this script if you want to, for example on GNOME you can do this: https://askubuntu.com/a/1039949

## If you use ssh key authentication..
You can probably do this https://serverfault.com/a/241593 and then remove sshpass, that shouldn't be needed.

## Windows
If you're on Windows, you can't use this script. Follow [this](https://github.com/dps910/nginx-image-server#configuring-sharex-windows).

## macOS
The script can probably be modified to upload images via FTP, or you can make your own script.
