# 2: Your first instances
Incus is image based and can load images from different image servers. In this tutorial, we will use the images: server.

This Incus server is currently empty, you can make sure of that with:

incus list
Start by launching a few instances.

Launch a container called "first" using the Ubuntu 20.04 image:
$ incus launch images:ubuntu/20.04 first

Note that launching this container takes a few seconds, because the image must be downloaded and unpacked first.
Launch a container called "second" using the same image:

$ incus launch images:ubuntu/20.04 second

Launching this container is quicker than launching the first, because the image is already available.
Copy the first container into a container called "third":
$ incus copy first third

Launch a container called "alpine" using the Alpine Edge image:
$ incus launch images:alpine/edge alpine

Launch a virtual machine called "debian" using the Debian 12 image:
$ incus launch images:debian/12 debian --vm



# 3: Inspect the instances
Check the list of instances that you launched:
$ incus list

You will see that all but the third instance are running. This is because you created the third instance by copying the first, but you didn't start it.
You can start the third instance with:
$ incus start third

You can query more information about each instance with:
$ incus info first
$ incus info second
$ incus info third
$ incus info alpine
$ incus info debian


# 4: Stop and delete instances
We don't need all of these instances for the remainder of the tutorial, so let's clean some of them up.
Stop the second instance:
$ incus stop second

Delete the second instance:
$ incus delete second

Delete the third instance:
$ incus delete third

Since this instance is running, you get an error message that you must stop it first. Alternatively, you can force-delete it:
$ incus delete third --force



# 5: Instance configuration
There are several limits and configuration options that you can set for your instances. See Instance configuration for an overview.
Let's create another instance with some resource limits.

Launch a container and limit it to one vCPU and 192 MiB of RAM:
$ incus launch images:ubuntu/20.04 limited -c limits.cpu=1 -c limits.memory=192MiB

Check the current configuration and compare it to the configuration of the first (unlimited) instance:
$ incus config show limited
$ incus config show first

Check the amount of free and used memory on the parent system and on the two instances:
$ free -m
$ incus exec first -- free -m
$ incus exec limited -- free -m

Note that the total amount of memory is identical for the parent system and the first instance, because by default, the container inherits the resources from its parent environment. The limited instance, on the other hand, has only 192 MiB available.
Check the number of CPUs available on the parent system and on the two instances:
$ nproc
$ incus exec first -- nproc
$ incus exec limited -- nproc

Again, note that the number is identical for the parent system and the first instance, but reduced for the limited instance.
You can also update the configuration while your instance is running.

Configure a memory limit for your instance:
$ incus config set limited limits.memory=128MiB

Check that the configuration has been applied:
$ incus config show limited

Check the amount of memory that is available to the instance:
$ incus exec limited -- free -m

Note that the number has changed.


# 6: Interact with an instance
Let's interact with your instances.
Launch an interactive shell in your instance:
$ incus exec first -- bash

Enter some commands, for example, display information about the operating system:
$ cat /etc/*release

Exit the interactive shell:
$ exit

Repeat the steps for your alpine instance:
$ incus exec alpine -- ash
$ cat /etc/*release
$ exit

Instead of logging on to the instance and running commands there, you can run commands directly from the host. For example, you can install a command line tool on the instance and run it:
$ incus exec first -- apt-get update
$ incus exec first -- apt-get install sl -y
$ ncus exec first -- /usr/games/sl




# 7: Access files from the instance
You can access the files from your instance and interact with them.

Pull a file from the instance:
$ incus file pull first/etc/hosts .

Add an entry to the file:
$ echo "1.2.3.4 my-example" >> hosts

Push the file back to the instance:
$ incus file push hosts first/etc/hosts

Use the same mechanism to access log files:
$ incus file pull first/var/log/syslog - | less
$ q




# 8: Snapshots
Incus supports creating and restoring instance snapshots.

Create a snapshot called "clean":
$ incus snapshot create first clean

Confirm that the snapshot has been created:
$ incus snapshot list first

Break the instance:
$ incus exec first -- rm -Rf /etc /usr

Confirm the breakage:
$ incus exec first -- bash

Note that you do not get a shell, because you deleted the bash command.
Restore the instance to the snapshotted state:
$ incus snapshot restore first clean

Confirm that everything is back to normal:
$ incus exec first -- bash
$ exit

Delete the snapshot:
$ incus snapshot delete first clean


