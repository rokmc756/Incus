

ssh root@192.168.2.$1 "systemctl list-unit-files --type=service | grep incus"

