
gw_ip_addr="192.168.0.101"
root_pass="changeme"

ip_range="1 5"


for i in `seq $ip_range`
do

    # echo $i
    sshpass -p "$root_pass" ssh -o StrictHostKeyChecking=no root@$gw_ip_addr "virsh $1 $2-node0$i"

done

