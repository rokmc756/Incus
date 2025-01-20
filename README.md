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

## Prepare ansible host to run GPFarmer
* MacOS
```!yaml
$ xcode-select --install
$ brew install ansible
$ brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
```


## How to run this Ansible Playbook
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


## Create Storage Pools
#### 1) Local Directory
```yaml
$ make storage r=create s=lvm c=local
$ make storage r=create s=lvm c=dirs
```
#### 2) Logical Volume Groups
```yaml
$ make storage r=create s=lvm c=local
$ make storage r=create s=lvm c=block
$ make storage r=create s=lvm c=vgs
$ make storage r=create s=lvm c=vg
$ make storage r=create s=lvm c=thin
```
#### 3) Btrfs
```yaml
$ make storage r=create s=btrfs c=local
$ make storage r=create s=btrfs c=dirs
$ make storage r=create s=btrfs c=block
```
#### 3) ZFS
```yaml
$ make storage r=create s=zfs c=local
$ make storage r=create s=zfs c=loopback
$ make storage r=create s=zfs c=block
$ make storage r=create s=zfs c=zpool
$ make storage r=create s=zfs c=slice
```
#### 3) Ceph
```yaml
$ make storage r=create s=ceph c=rbd
$ make storage r=create s=ceph c=fs
$ make storage r=create s=ceph c=rgw
```


## Progress
- [O] Initialize ubuntu 24.4 hosts in order to install required packages for incus and exchange ssh keys
- [O] Configure host build system, including installing dependencies and patching host system quirks
- [O] Install/Configure and Uninstall Incus & Web UI Packages
- [O] Add CA Key partially automated
- [O] Enable Cluster with YAML
- [O] Resolve Hosts got hung when adding or removeing several times - It's due to not removing Trust Store
- [O] Add Nodes
- [O] Remove Nodes
- [0] Tested CephRBD and CephFS
- [ ] LVM Cluster Setting
- [ ] Ceph Storage Pool - CephRBD, CephFS, Radosgw
- [ ] Network Settings - OVN

