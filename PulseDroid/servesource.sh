pactl load-module module-simple-protocol-tcp rate=48000 format=s16le channels=2 source=alsa_output.pci-0000_00_1f.3.analog-stereo.monitor record=true port=33333 listen=0.0.0.0
