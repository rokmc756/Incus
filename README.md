# WIP

# How to run this Ansible Playbook
### Initialize/Uninstall Linux Hosts
~~~!yaml
$ make hosts r=install(or uninstall) s=incus
~~~
### Enable/Disable Zabbly Repository
~~~!yaml
$ make incus r=install(or uninstall) s=repo
~~~
### Install/Uninstall Incus Packages
~~~!yaml
$ make incus r=install(or uninstall) s=pkgs
~~~
### Initialize Incus Cluster
~~~!yaml
$ make incus r=install s=init
~~~
### Install/Uninstall Incus Web UI
~~~!yaml
$ make incus r=install(or uninstall) s=ui
~~~
### Add/Remove Hosts to/at Incus Cluster
~~~!yaml
$ make incus r=install(or uninstall) s=add/remove
~~~


# Progress
- [O] Initialize ubuntu 24.4 hosts in order to install required packages for incus and exchange ssh keys
- [O] Configure host build system, including installing dependencies and patching host system quirks
- [O] Install/Configure and Uninstall Incus & Web UI Packages
- [O] Add CA Key partially automated
- [O] Enable Cluster with YAML
- [O] Resolve Hosts got hung when adding or removeing several times - It's due to not removing Trust Store
- [O] Add Nodes
- [O] Remove Nodes

