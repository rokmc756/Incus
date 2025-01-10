## WIP

## How to run this Ansible Playbook
### Initialize Linux Hosts
~~~!yaml
$ make hosts r=install s=incus
~~~
### Install and Configure Incus Packages
~~~!yaml
$ make incus r=install s=incus
~~~
### Install and Configure Incus Web UI Packages
~~~!yaml
$ make incus r=install s=ui
~~~


## Progress
- [x] Initialize ubuntu 24.4 hosts in order to install required packages for incus and exchange ssh keys
- [x] Configure host build system, including installing dependencies and patching host system quirks
- [x] Install/Configure and Uninstall Incus & Web UI Packages
- [ ] Add CA Key - WIP
- [ ] Enable Cluster - WIP
- [ ] Add Nodes - WIP

