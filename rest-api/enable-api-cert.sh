#!/bin/bash


ssl_dir=/root/certs
mkdir -p $ssl_dir

openssl genrsa -out $ssl_dir/incus-api.key 4096

openssl req -new -key $ssl_dir/incus-api.key -out $ssl_dir/incus-api.csr \
-subj "/C=KR/ST=Seoul/L=Guro/O=FuturFusion/OU=GSS/CN=jtest.futurfusion.io/emailAddress=rokmc756@gmail.com"

openssl x509 -req -days 3650 -in {{ _ssl.ssl_dir }}/incus-api.csr \
-subj "/C=KR/ST=Seoul/L=Guro/O=FuturFusion/OU=GSS/CN=jtest.futurfusion.io/emailAddress=rokmc756@gmail.com" \
-signkey $ssl_dir/incus-api.key \
-out $ssl_dir/incus-api.crt

chmod 600 $ssl_dir/incus-api.crt
chmod 600 $ssl_dir/incus-api.csr
chmod 600 $ssl_dir/incus-api.key

incus config trust add $ssl_dir/incus-api.crt
# curl --cert {{ _ssl.ssl_dir }}/incus-api.crt --key {{ _ssl.ssl_dir }}/incus-api.key -k https://192.168.1.81:8443/1.0/instances/test/state?project=default

