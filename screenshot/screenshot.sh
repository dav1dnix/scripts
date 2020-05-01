#!/bin/sh
areass() {
	# Copy image to clipboard and send it to /tmp/image.png
    flameshot gui -r && xclip -selection c -t image/png -o > /tmp/image.png

	# Send image to 0x0.st server
    curl -F'file=@/tmp/image.png' https://0x0.st | xclip -selection c

	# When image is in the clipboard, remove everything except after the /
	# then add everything after the / into a variable
	# then add it at the end of new url
	COPY_IMG="xclip -selection c -o | cut -d / -f 4"
	PNG=$(eval $COPY_IMG)
	echo "https://0x0.arikawa-hi.me/$PNG" | xclip -selection c

}
areass
