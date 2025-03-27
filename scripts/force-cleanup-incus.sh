
systemctl stop incus-user.socket incus-user incus.socket incus incus-startup incus-lxcfs

systemctl disable incus-user.socket incus-user incus.socket incus incus-startup incus-lxcfs

systemctl daemon-reload

apt remove -y incus-client incus-tools incus

apt update -y

dpkg --purge incus-agent incus incus-base

pkill -U incus

fuser -k /var/lib/incus

umount /var/lib/incus/guestapi

umount /var/lib/incus/shmounts

umount  /var/lib/lxcfs

rm -rf /var/lib/incus/guestapi

rm -rf /var/lib/incus/shmounts

rm -rf /var/lib/lxcfs

rm -rf /var/lib/incus/storage-pools

rm -rf /var/lib/incus/database

rm -rf /root/incus-ui.crt

apt remove -y lxcfs

reboot
