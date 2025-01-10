# WIP

# How to run this Ansible Playbook
### Initialize/Clean Linux Hosts
~~~!yaml
$ make hosts r=install s=incus
or
$ make hosts r=uninstall s=incus
~~~
### Install/Uninstall and Config/Clean Incus Packages
~~~!yaml
$ make incus r=install s=incus
or
$ make incus r=uninstall s=incus
~~~
### Install and Config/Clean Incus Web UI Packages
~~~!yaml
$ make incus r=install s=ui
or
$ make incus r=uninstall s=ui
~~~


# Progress
- [x] Initialize ubuntu 24.4 hosts in order to install required packages for incus and exchange ssh keys
- [x] Configure host build system, including installing dependencies and patching host system quirks
- [x] Install/Configure and Uninstall Incus & Web UI Packages
- [ ] Add CA Key - WIP
- [ ] Enable Cluster - WIP
- [ ] Add Nodes - WIP

