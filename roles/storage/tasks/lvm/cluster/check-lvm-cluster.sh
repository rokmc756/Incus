
lvmlockctl -i

lvs -a -o +devices

pvs

# vgchange --lock-start
# lvmlockctl --gl-enable

# vgchange --lockstart lvm-cluster-vg06
# sleep 50
# vgremove lvm-cluster-vg06 -f

# vgchange --lockstop lvm-cluster-vg06

