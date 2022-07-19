sudo cp ./wol.service /etc/systemd/system/

sudo systemctl daemon-reload

sudo systemctl enable wol.service