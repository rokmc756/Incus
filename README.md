## What is this Incus Github Repostory?
It is ansible playbook to deploy Incus Cluster on Baremetal, Virtual Machines.
The main purposes of this project are simple to deploy Incus Cluster quickly and learn knowleges abot it.

## Where is it?
It's originated by Jack Moon.

## Supported Incus Version
* Incus 6.x

## Supported Platform and OS
* Virtual Machines
* Baremetal
* Ubuntu 24.x

## Prerequisite
MacOS or Linux should have installed ansible as ansible host.
Supported OS for ansible target host should be prepared with package repository configured such as yum, dnf and apt
At least a Normal User which has Sudo Privileges
Root User should have Password ans Allow access with Password login via SSH

## Prepare ansible host to run this playbook
* MacOS
```!yaml
$ xcode-select --install
$ brew install ansible
$ brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
```


## How to run this Ansible Playbook
#### Configure Ansible Hosts
~~~!yaml
$ vi ansible-hosts
[all:vars]
ssh_key_filename="id_rsa"
remote_machine_username="jomoon"
remote_machine_password="changeme"
ansible_python_interpreter=/usr/bin/python3

[control]
ubt24-node01 ansible_ssh_host=192.168.1.81

[workers]
ubt24-node01 ansible_ssh_host=192.168.1.81
ubt24-node02 ansible_ssh_host=192.168.1.82
ubt24-node03 ansible_ssh_host=192.168.1.83
ubt24-node04 ansible_ssh_host=192.168.1.84
ubt24-node05 ansible_ssh_host=192.168.1.85

[cluster]
ubt24-node04 ansible_ssh_host=192.168.1.84
ubt24-node05 ansible_ssh_host=192.168.1.85
~~~
#### Initialize/Uninstall Linux Hosts
~~~!yaml
$ make hosts r=init(or uninit) s=all
~~~
#### Enable/Disable Zabbly Repository
~~~!yaml
$ make incus r=enable(or disable) s=repo
~~~
##### Install/Uninstall Incus Packages
~~~!yaml
$ make incus r=install(or uninstall) s=pkgs
~~~
##### Initialize Incus Cluster
~~~!yaml
$ make incus r=init s=host
~~~
##### Install/Uninstall Incus Web UI
~~~!yaml
$ make incus r=install(or uninstall) s=ui
~~~
##### Add/Remove Hosts to/at Incus Cluster
~~~!yaml
$ make incus r=add(or remove) s=host
~~~
##### Deploy Incus Cluster at once
~~~!yaml
$ make incus r=install s=all
~~~
##### Deploy/Destroy Incus Cluster at once
~~~!yaml
$ make incus r=deploy(or destroy) s=all
~~~
##### Force Destroy Incus Cluster
~~~!yaml
$ make incus r=destroy s=force
~~~


#### Create Storage Pools
##### 1) Local Directory
```yaml
$ make storage r=create s=lvm c=local
$ make storage r=create s=lvm c=dirs
```
##### 2) Logical Volume Groups
```yaml
$ make storage r=create s=lvm c=local
$ make storage r=create s=lvm c=block
$ make storage r=create s=lvm c=vgs
$ make storage r=create s=lvm c=vg
$ make storage r=create s=lvm c=thin

# For Enable Clustered-LVM Storage Pool with iSCSI
$ make storage r=install s=iscsi c=target
$ make storage r=install s=iscsi c=initiator
$ make storage r=create s=lvm c=cluster

# For Disable Clustered-LVM Storage Pool with iSCSI
$ make storage r=delete s=lvm c=cluster
$ make storage r=uninstall s=iscsi c=initiator
$ make storage r=uninstall s=iscsi c=target
```
##### 3) Btrfs
```yaml
$ make storage r=create s=btrfs c=local
$ make storage r=create s=btrfs c=dirs
$ make storage r=create s=btrfs c=block
```
##### 3) ZFS
```yaml
$ make storage r=create s=zfs c=local
$ make storage r=create s=zfs c=loopback
$ make storage r=create s=zfs c=block
$ make storage r=create s=zfs c=zpool
$ make storage r=create s=zfs c=slice
```
##### 4) Ceph
```yaml
$ make storage r=create s=ceph c=rbd
$ make storage r=create s=ceph c=fs
$ make storage r=create s=ceph c=rgw
```


## Progress
- [O] Initialize Ubuntu 24.x Hosts in order to Install Required Packages for Incus and Exchange SSH Keys
- [O] Install/Configure and Uninstall Incus & Web UI Packages
- [O] Add CA Key Partially Automated
- [O] Enable Cluster with YAML
- [O] Resolve Hosts got hung when adding or removeing several times - It's due to not removing Trust Store
- [O] Add Nodes
- [O] Remove Nodes
- [O] Local Storage Pool
- [O] ZFS Storage Pool
- [O] Btrfs Storage Pool
- [O] LVM Storage Pool
- [O] Ceph Storage Pool - CephRBD, CephFS, Rados Gateway Storage Pool with Buckets
- [O] Working LVM Cluster Storage Pool Setting with iSCSI  -  https://discussion.fedoraproject.org/t/iscsi-shared-lvm/128319
- [X] Network Settings - OVN and so on


## References
- https://www.suse.com/ko-kr/support/kb/doc/?id=000018894

