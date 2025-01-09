[ On Rocky 9.x ]


# RPM packages and their dependencies are not yet available from the Extra Packages for Enterprise Linux (EPEL) repository,
# but via the neil/incus Community Project (COPR) repository for Rocky Linux 9.
# Ensure that the EPEL repository is installed for package dependencies and then install the COPR repository:

dnf -y install epel-release


# Ensure that the CodeReady Builder (CRB) is available for other package dependencies:
dnf config-manager --enable crb


# Then install Incus and optionally, Incus tools:
dnf install incus incus-tools



useradd romoon -g incus-admin

systemctl start incus-startup

systemctl start incus-user



# Incus requires some initial setup for networking and storage. This can be done interactively through:
incus admin init

Would you like to use clustering? (yes/no) [default=no]: yes
What IP address or DNS name should be used to reach this server? [default=192.168.0.121]:
Are you joining an existing cluster? (yes/no) [default=no]:
What member name should be used to identify this server in the cluster? [default=rk9-incus01]:
Do you want to configure a new local storage pool? (yes/no) [default=yes]:
Name of the storage backend to use (dir, lvm) [default=dir]:
Do you want to configure a new remote storage pool? (yes/no) [default=no]:
Would you like to use an existing bridge or host interface? (yes/no) [default=no]:
Would you like stale cached images to be updated automatically? (yes/no) [default=yes]:
Would you like a YAML "init" preseed to be printed? (yes/no) [default=no]:


# You can list all images that are available on this server with:
incus image list images;
+-------+-------------+--------+-------------+--------------+------+------+-------------+
| ALIAS | FINGERPRINT | PUBLIC | DESCRIPTION | ARCHITECTURE | TYPE | SIZE | UPLOAD DATE |
+-------+-------------+--------+-------------+--------------+------+------+-------------+

# Launch a container called first using the Ubuntu 22.04 image
incus launch images:ubuntu/22.04 first

Launching first
Error: Failed instance creation: Fetch project database object: Failed to fetch from "projects" table: Failed to fetch from
"projects" table: Failed to fetch from "projects" table: sql: transaction has already been committed or rolled back


#
[root@rk9-incus01 ~]# incus remote list
+-----------------+------------------------------------+---------------+-------------+--------+--------+--------+
|      NAME       |                URL                 |   PROTOCOL    |  AUTH TYPE  | PUBLIC | STATIC | GLOBAL |
+-----------------+------------------------------------+---------------+-------------+--------+--------+--------+
| images          | https://images.linuxcontainers.org | simplestreams | none        | YES    | NO     | NO     |
+-----------------+------------------------------------+---------------+-------------+--------+--------+--------+
| local (current) | unix://                            | incus         | file access | NO     | YES    | NO     |
+-----------------+------------------------------------+---------------+-------------+--------+--------+--------+


# incus image list remote
+-------+-------------+--------+-------------+--------------+------+------+-------------+
| ALIAS | FINGERPRINT | PUBLIC | DESCRIPTION | ARCHITECTURE | TYPE | SIZE | UPLOAD DATE |
+-------+-------------+--------+-------------+--------------+------+------+-------------+


# incus remote add jrepo01 https://images.linuxcontainers.org --protocol=simplestreams

# incus image list jrepo01
+-------+-------------+--------+-------------+--------------+------+------+-------------+
| ALIAS | FINGERPRINT | PUBLIC | DESCRIPTION | ARCHITECTURE | TYPE | SIZE | UPLOAD DATE |
+-------+-------------+--------+-------------+--------------+------+------+-------------+
[root@rk9-incus01 ~]# incus image list
+-------+-------------+--------+-------------+--------------+------+------+-------------+
| ALIAS | FINGERPRINT | PUBLIC | DESCRIPTION | ARCHITECTURE | TYPE | SIZE | UPLOAD DATE |
+-------+-------------+--------+-------------+--------------+------+------+-------------+
[root@rk9-incus01 ~]# incus image list remote
+-------+-------------+--------+-------------+--------------+------+------+-------------+
| ALIAS | FINGERPRINT | PUBLIC | DESCRIPTION | ARCHITECTURE | TYPE | SIZE | UPLOAD DATE |
+-------+-------------+--------+-------------+--------------+------+------+-------------+


# https://discuss.linuxcontainers.org/t/incus-no-uid-gid-allocation-configured/19002/2
$ vi /etc/subuid
# manolo:100000:65536
# incus:1000000:65536
root:1000000:1000000000

$ vi /etc/subgid
# manolo:100000:65536
# incus:1000000:65536
root:1000000:1000000000

# incus launch images:ubuntu/20.04 first
Launching first
Error: Failed instance creation: Fetch project database object: Failed to fetch from "projects" table: Failed to fetch from "projects" table: Failed to fetch from "projects" table: sql: transaction has already been committed or rolled back

# systemctl restart incus

# incus launch images:ubuntu/20.04 first



# incus launch images:debian/12 debian --vm
Launching debian
Error: Failed instance creation: Failed creating instance record: Instance type "virtual-machine" is not supported on this server: KVM support is missing (no /dev/kvm)


Ensure that your system has hardware virtualization extensions enabled. For Intel-based hosts, Use the following command to confirm if the CPU virtualization extension (vmx) is available:

$ sudo grep -e 'vmx' /proc/cpuinfo
For AMD-based hosts, confirm if the CPU virtualization extension (svm) is available by running the following command:

$ sudo grep -e 'svm' /proc/cpuinfo


# Install KVM
dnf install qemu-kvm libvirt virt-manager virt-install
dnf install epel-release -y
dnf -y install bridge-utils virt-top libguestfs-tools bridge-utils virt-viewer



# vi /etc/sysctl.d/98-incus.conf
net.ipv4.ip_forward = 1
net.ipv4.ip_forward_update_priority = 1
net.ipv4.ip_forward_use_pmtu = 0




# incus launch images:debian/12 debian --vm
Launching debian
Error: Failed instance creation: Failed creating instance record: Instance type "virtual-machine" is not supported on this server: QEMU command not available: exec: "qemu-system-x86_64": executable file not found in $PATH


[root@rk9-incus01 ~]# systemctl enable libvirtd
Created symlink /etc/systemd/system/multi-user.target.wants/libvirtd.service → /usr/lib/systemd/system/libvirtd.service.
Created symlink /etc/systemd/system/sockets.target.wants/libvirtd.socket → /usr/lib/systemd/system/libvirtd.socket.
Created symlink /etc/systemd/system/sockets.target.wants/libvirtd-ro.socket → /usr/lib/systemd/system/libvirtd-ro.socket.
Created symlink /etc/systemd/system/sockets.target.wants/libvirtd-admin.socket → /usr/lib/systemd/system/libvirtd-admin.socket.
[root@rk9-incus01 ~]# systemctl start libvirtd



# ln -sf /usr/libexec/qemu-kvm /usr/bin/qemu-kvm

# ln -sf /usr/libexec/qemu-kvm /usr/bin/qemu-system-x86_64



# Check the list of instances that you launched:
incus list


# You will see that all but the third instance are running. This is because you created the third instance by copying the first, but you didn't start it.
# You can start the third instance with:
incus start third


# You can query more information about each instance with:
incus info first
incus info second
incus info third
incus info alpine
incus info debian



# for qemu-system-x86-64 package
$ dnf --nogpg install https://mirror.ghettoforge.org/distributions/gf/gf-release-latest.gf.el9.noarch.rpm
$ dnf remove  qemu-kvm-common
$ dnf install qemu-system-*

# Same Error
reboot


# Same Error but not PATH displayed
[root@rk9-incus01 ~]# incus launch images:debian/12 debian --vm
Launching debian
Error: Failed instance creation: Failed creating instance record: Instance type "virtual-machine" is not supported on this server: QEMU failed to run feature checks




$ incus admin shutdown
$ incus admin waitready



dnf groupinstall "Virtualization Host"


# 
https://techviewleo.com/solve-qemu-system-x86_64-executable-file-not-found-in-path/


#
https://gitlab.archlinux.org/archlinux/packaging/packages/incus/-/issues/6


$ systemctl daemon-reload


dmidecode -s system-product-name
VMware Virtual Platform


dmidecode | egrep -i 'manufacturer|product'


# incus create myvm --empty --vm -s default --device root,size=5GiB
Creating myvm
Error: Failed creating instance record: Instance type "virtual-machine" is not supported on this server: QEMU command not available: exec: "qemu-system-x86_64": executable file not found in $PATH


# [root@rk9-incus01 ~]# systemd-detect-virt
vmware


# https://discuss.linuxcontainers.org/t/kvm-is-detected-as-qemu-with-systemd-detect-virt/18240/3
$ echo KVM > foo
$ mount -o bind foo /sys/class/dmi/id/sys_vendor
$ cat /sys/class/dmi/id/sys_vendor
KVM
$ systemd-detect-virt
vmware

$ cat /sys/devices/virtual/dmi/id/sys_vendor
KVM



