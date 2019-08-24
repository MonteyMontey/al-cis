#!/bin/bash

sudo docker save al-cis | gzip > al-cis.tar.gz &&

for ip in "$@"
do
    scp -i ./deploy_key -o StrictHostKeyChecking=no al-cis.tar.gz montey@"$ip":/tmp
    ssh -i ./deploy_key -o StrictHostKeyChecking=no montey@"$ip" << EOF
    sudo systemctl stop cis0;
    sudo systemctl stop cis1;
    cat /tmp/al-cis.tar.gz | gunzip | sudo docker load;
    rm /tmp/al-cis.tar.gz;
    sudo systemctl enable cis0;
    sudo systemctl enable cis1;
    sudo docker system prune -f;
EOF
done

for ip in "$@"
do
    ssh -i ./deploy_key -o StrictHostKeyChecking=no montey@"$ip" 'sudo reboot' || true
done

