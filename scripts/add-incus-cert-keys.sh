openssl genrsa -out incus.key 4096                                              # Generate a private key.
openssl req -new -key incus.key -out incus.csr                                  # Create a certificate request.
openssl x509 -req -days 3650 -in incus.csr -signkey incus.key -out incus.crt    # Generate an auto signed certificate.
incus config trust add incus.crt                                                  # Tells LXC to use this certificate for auth.



# https://discuss.linuxcontainers.org/t/creating-new-instance-over-rest-api/22812


curl -X "POST" "https://incus.xyz.com/1.0/instances" \
     -H 'Authorization: Bearer XYZ' \
     -d $'{
  "source": {
    "alias": "hello-world",
    "protocol": "oci",
    "type": "image",
    "server": "https://docker.io"
  }
}'


# https://discuss.linuxcontainers.org/t/httpclient-cannot-access-the-api-of-incus/19733
# test is name of virtual machine
curl --cert ./incus.crt --key ./incus.key -k https://192.168.1.81:8443/1.0/instances/test/state?project=default

incus config trust add-certificate /root/incus.crt


# incus config set core.debug_address 127.0.0.1:8444
# curl http://127.0.0.1:8444/debug/pprof/goroutine?debug=2


