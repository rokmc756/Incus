## What is this Incus Github Repostory?
It is ansible playbook to deploy Incus Cluster on Baremetal, Virtual Machines. The main purposes of this project are simple to deploy Incus Cluster quickly and learn knowleges abot it.

## What is Incus?
Incus is a next-generation system container, application container, and virtual machine manager. It provides a user experience similar to that of a public cloud. With it, you can easily mix and match both containers and virtual machines, sharing the same underlying storage and network.
Incus is image based and provides images for a wide number of Linux distributions. It provides flexibility and scalability for various use cases, with support for different storage backends and network types and the option to install on hardware ranging from an individual laptop or cloud instance to a full server rack.
When using Incus, you can manage your instances (containers and VMs) with a simple command line tool, directly through the REST API or by using third-party tools and integrations. Incus implements a single REST API for both local and remote access.

The Incus project was created by Aleksa Sarai as a community driven alternative to Canonical's LXD.
Today, it's led and maintained by many of the same people that once created LXD.

## Containers and Virtual Machines
Incus provides support for system containers, application containers, and virtual machines.
When running a system container, Incus simulates a virtual version of a full operating system. To do this, it uses the functionality provided by the kernel running on the host system.
When running an application container, Incus runs isolated applications within the host's operating system using container images, similar to how Docker operates.
When running a virtual machine, Incus uses the hardware of the host system, but the kernel is provided by the virtual machine. Therefore, virtual machines can be used to run, for example, a different operating system.
You can learn more about the differences between application containers, system containers and virtual machines in our documentation.

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


[iscsi_target]
rk9-freeipa  ansible_ssh_host=192.168.1.90


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
# For Create Ceph Storage Pool
$ make storage r=create s=ceph c=rbd
$ make storage r=create s=ceph c=fs
$ make storage r=create s=ceph c=rgw

# For Delete Ceph Storage Pool
$ make storage r=delete s=ceph c=rgw
$ make storage r=delete s=ceph c=fs
$ make storage r=delete s=ceph c=rbd
```

#### Create Network
##### 1) OVN
```yaml
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

