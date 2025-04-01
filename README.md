## What is Incus?
Incus is system container, application container, and virtual machine manager. It provides a user experience similar to that of a public or private cloud.
It can easily mix and match both containers and virtual machines, sharing the same underlying storage and network.

Incus is image based and provides images for a wide number of Linux distributions. It provides flexibility and scalability for various use cases, with support for different storage backends and network types and the option to install on hardware ranging from an individual laptop or cloud instance to a full server rack.

When using Incus, you can manage your instances ( Containers and VMs) with a simple command line tool, directly through the REST API or by using third-party tools and integrations.
Incus implements a single REST API for both local and remote access.

## Containers and Virtual Machines
Incus provides support for system containers, application containers, and virtual machines.

When running a system container, Incus simulates a virtual version of a full operating system. To do this, it uses the functionality provided by the kernel running on the host system.
When running an application container, Incus runs isolated applications within the host's operating system using container images, similar to how Docker operates.
![alt text](https://github.com/rokmc756/Incus/blob/main/roles/incus/images/application-vs-system-containers.svg)

When running a virtual machine, Incus uses the hardware of the host system, but the kernel is provided by the virtual machine.\
![alt text](https://github.com/rokmc756/Incus/blob/main/roles/incus/images/virtual-machines-vs-system-containers.svg)

Therefore, virtual machines can be used to run, for example, a different operating system.

## Architecture
### Internal
![alt text](https://github.com/rokmc756/Incus/blob/main/roles/incus/images/incus-architecture-example01.png)
### External
![alt text](https://raw.githubusercontent.com/rokmc756/Incus/refs/heads/main/roles/incus/images/incus-architecture-examples02.webp)

## What is this Incus Github Repostory?
It is ansible playbook to deploy Incus Cluster on Baremetal, Virtual Machines. The main purposes of this project are simple to deploy Incus Cluster quickly and learn knowleges about it.

## Where is it originated?
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
```!sh
$ xcode-select --install
$ brew install ansible
$ brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
```


## How to Run Incus Ansible Playbook
### 1) Configure Ansible Hosts
~~~!yaml
[all:vars]
ssh_key_filename="id_rsa"
remote_machine_username="jomoon"
remote_machine_password="changeme"
ansible_python_interpreter=/usr/bin/python3

[iscsi_target]
rk9-node06   ansible_ssh_host=192.168.1.176

[control]
ubt24-node01  ansible_ssh_host=192.168.1.81  host_id=1

[cluster]
ubt24-node02  ansible_ssh_host=192.168.1.82  host_id=2
ubt24-node03  ansible_ssh_host=192.168.1.83  host_id=3
ubt24-node04  ansible_ssh_host=192.168.1.84  host_id=4
ubt24-node05  ansible_ssh_host=192.168.1.85  host_id=5

[workers:children]
control
cluster
~~~
#### 2) Initialize/Uninstall Linux Hosts
~~~!sh
$ make hosts r=init s=all
$ make hosts r=uninit s=all
~~~
#### 3) Enable/Disable Zabbly Repository
~~~!sh
$ make incus r=enable s=repo
$ make incus r=disable s=repo
~~~
##### 4) Install/Uninstall Incus Packages
~~~!sh
$ make incus r=install s=pkgs
$ make incus r=uninstall s=pkgs
~~~
##### 5) Initialize Incus Cluster
~~~!sh
$ make incus r=init s=host
~~~
##### 6) Install/Uninstall Incus Web UI
~~~!sh
$ make incus r=install s=ui
$ make incus r=uninstall s=ui
~~~
##### 7) Add/Remove Hosts to/at Incus Cluster
~~~!sh
$ make incus r=add s=host
$ make incus r=remove s=host
~~~
##### 8) Deploy Incus Cluster at once
~~~!sh
$ make incus r=install s=all
~~~
##### 9) Enable Incus API Certificate
~~~!sh
$ make incus r=install s=api c=cert
~~~
##### 10) Deploy/Destroy Incus Cluster at once
~~~!sh
$ make incus r=deploy s=all
$ make incus r=destroy s=all
~~~
##### 11) Force Destroy Incus Cluster
~~~!sh
$ make incus r=destroy s=force
~~~


### Create and Delete Various Storage Pools
##### 1) Local Directory
```!sh
$ make storage r=create s=dir c=local
$ make storage r=delete s=dir c=local

$ make storage r=create s=dir c=dirs
$ make storage r=delete s=dir c=dirs
```
##### 2) Logical Volume Groups
```!sh
$ make storage r=create s=lvm c=local
$ make storage r=delete s=lvm c=local

$ make storage r=create s=lvm c=blk
$ make storage r=delete s=lvm c=blk

$ make storage r=create s=lvm c=vgs
$ make storage r=delete s=lvm c=vgs

$ make storage r=create s=lvm c=vg
$ make storage r=delete s=lvm c=vg

$ make storage r=create s=lvm c=thin
$ make storage r=delete s=lvm c=thin


# For Enable and Disable Clustered-LVM Storage Pool with iSCSI
$ make storage r=install s=iscsi c=target
$ make storage r=uninstall s=iscsi c=target

$ make storage r=install s=iscsi c=initiator
$ make storage r=uninstall s=iscsi c=initiator

$ make storage r=create s=lvm c=cluster
$ make storage r=delete s=lvm c=cluster
```
##### 3) Btrfs
```!sh
$ make storage r=create s=btrfs c=local
$ make storage r=delete s=btrfs c=local

$ make storage r=create s=btrfs c=dirs
$ make storage r=delete s=btrfs c=dirs

$ make storage r=create s=btrfs c=blk
$ make storage r=delete s=btrfs c=blk
```
##### 3) ZFS
```!sh
$ make storage r=create s=zfs c=local
$ make storage r=delete s=zfs c=local

$ make storage r=create s=zfs c=loopback
$ make storage r=delete s=zfs c=loopback

$ make storage r=create s=zfs c=blk
$ make storage r=delete s=zfs c=blk

$ make storage r=create s=zfs c=zpool    # Need to fix errors
$ make storage r=delete s=zfs c=zpool    # Need to fix errors

$ make storage r=create s=zfs c=slice    # Need to fix errors
$ make storage r=delete s=zfs c=slice    # Need to fix errors
```
##### 4) Ceph Storage Pool
```!sh
# Enable and Disable Ceph Client for Incus Hosts
$ make storage r=enable s=ceph c=client
$ make storage r=disable s=ceph c=client

# Create and Delete Ceph Storage Pool
$ make storage r=create s=ceph c=rbd
$ make storage r=delete s=ceph c=rbd

$ make storage r=create s=ceph c=fs
$ make storage r=delete s=ceph c=fs

$ make storage r=create s=ceph c=rgw
$ make storage r=delete s=ceph c=rgw
```

##### 4) Linstor Storage Pool
```!sh
# Enable and Disable Linstor Client for Incus Hosts
$ make storage r=enable s=linstor c=client
$ make storage r=disable s=linstor c=client

# Create and Delete Linstor Storage Pool
$ make storage r=create s=linstor c=lvmthin
$ make storage r=delete s=linstor c=lvmthin

$ make storage r=create s=linstor c=zfsthin
$ make storage r=delete s=linstor c=zfsthin

$ make storage r=create s=linstor c=lvm
$ make storage r=delete s=linstor c=lvm

$ make storage r=create s=linstor c=zfs
$ make storage r=delete s=linstor c=zfs

$ make storage r=create s=linstor c=filethin
$ make storage r=delete s=linstor c=filethin
```


### Create Network
##### 1) OVN
```!sh
# For Configure and Install OVN Network
$ make network r=install s=ovn c=cluster
$ make network r=create s=ovn c=cluster

# For Uninstall and Disable OVN network
$ make network r=delete s=ovn c=cluster
$ make network r=uninstall s=ovn c=cluster
```


## Progress
- [X] Initialize Ubuntu 24.x Hosts in order to Install Required Packages for Incus and Exchange SSH Keys
- [X] Install/Configure and Uninstall Incus & Web UI Packages
- [X] Add CA Key Partially Automated
- [X] Enable Cluster with YAML
- [X] Resolve Hosts got hung when adding or removing several times - It's due to not removing Trust Store
- [X] Add Nodes
- [X] Remove Nodes
- [X] Local Storage Pool
- [X] ZFS Storage Pool
- [X] Btrfs Storage Pool
- [X] LVM Storage Pool
- [X] Ceph Storage Pool - CephRBD, CephFS, Rados Gateway Storage Pool with Buckets
- [X] Working LVM Cluster Storage Pool Setting with iSCSI
- [ ] Network Settings - OVN and so on

## References
- https://www.suse.com/ko-kr/support/kb/doc/?id=000018894
- https://discussion.fedoraproject.org/t/iscsi-shared-lvm/128319
- https://github.com/PenningLabs/lxconsole.git
- https://svolence.github.io/DRBD/README/       # Ubuntu PPA for DRBD

