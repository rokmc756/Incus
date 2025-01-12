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
$ make hosts r=install(or uninstall) s=incus
~~~
#### Enable/Disable Zabbly Repository
~~~!yaml
$ make incus r=install(or uninstall) s=repo
~~~
##### Install/Uninstall Incus Packages
~~~!yaml
$ make incus r=install(or uninstall) s=pkgs
~~~
##### Initialize Incus Cluster
~~~!yaml
$ make incus r=install s=init
~~~
##### Install/Uninstall Incus Web UI
~~~!yaml
$ make incus r=install(or uninstall) s=ui
~~~
##### Add/Remove Hosts to/at Incus Cluster
~~~!yaml
$ make incus r=install(or uninstall) s=add/remove
~~~


## Progress
- [O] Initialize ubuntu 24.4 hosts in order to install required packages for incus and exchange ssh keys
- [O] Configure host build system, including installing dependencies and patching host system quirks
- [O] Install/Configure and Uninstall Incus & Web UI Packages
- [O] Add CA Key partially automated
- [O] Enable Cluster with YAML
- [O] Resolve Hosts got hung when adding or removeing several times - It's due to not removing Trust Store
- [O] Add Nodes
- [O] Remove Nodes

