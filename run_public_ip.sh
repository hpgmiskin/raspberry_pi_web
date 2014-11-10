#!/bin/sh

PATH=usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
#* */1 * * * ~/python/raspberry_pi_web/run_public_ip.sh

cd ~/python/raspberry_pi_web
sudo python3 ~/python/raspberry_pi_web/publicIP.py