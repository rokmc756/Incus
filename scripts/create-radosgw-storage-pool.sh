$ lxc storage create remote-object cephobject cephobject.radosgsw.endpoint=http://athos.hosts.mtl.stgraber.net:7480
Storage pool remote-object created

$ lxc storage bucket create remote-object foo
Storage bucket foo created

$ lxc storage bucket key create remote-object foo admin --role admin
Storage bucket key admin added
Access key: TNZAYZSYIHM243PS8337
Secret key: xbBTY8exhnXdm3uwEcsBjeBVBFzi4n4NOhtOEYa3

$ lxc storage bucket show remote-object foo
config: {}
description: ""
name: foo
s3_url: http://athos.hosts.mtl.stgraber.net:7480/foo
location: ""

$ time s3cmd put Downloads/Win11_English_x64v1.iso s3://foo --multipart-chunk-size-mb=1000 --no-ssl --host athos.hosts.mtl.stgraber.net:7480 --host-bucket athos.hosts.mtl.stgraber.net:7480 --access_key TNZAYZSYIHM243PS8337 --secret_key xbBTY8exhnXdm3uwEcsBjeBVBFzi4n4NOhtOEYa3
upload: 'Downloads/Win11_English_x64v1.iso' -> 's3://foo/Win11_English_x64v1.iso'  [part 1 of 6, 1000MB] [1 of 1]
 1048576000 of 1048576000   100% in   26s    37.30 MB/s  done
upload: 'Downloads/Win11_English_x64v1.iso' -> 's3://foo/Win11_English_x64v1.iso'  [part 2 of 6, 1000MB] [1 of 1]
 1048576000 of 1048576000   100% in   25s    39.72 MB/s  done
upload: 'Downloads/Win11_English_x64v1.iso' -> 's3://foo/Win11_English_x64v1.iso'  [part 3 of 6, 1000MB] [1 of 1]
 1048576000 of 1048576000   100% in   28s    35.28 MB/s  done
upload: 'Downloads/Win11_English_x64v1.iso' -> 's3://foo/Win11_English_x64v1.iso'  [part 4 of 6, 1000MB] [1 of 1]
 1048576000 of 1048576000   100% in   31s    32.15 MB/s  done
upload: 'Downloads/Win11_English_x64v1.iso' -> 's3://foo/Win11_English_x64v1.iso'  [part 5 of 6, 1000MB] [1 of 1]
 1048576000 of 1048576000   100% in   29s    33.45 MB/s  done
upload: 'Downloads/Win11_English_x64v1.iso' -> 's3://foo/Win11_English_x64v1.iso'  [part 6 of 6, 307MB] [1 of 1]
 322172928 of 322172928   100% in    9s    33.17 MB/s  done

real    2m37.658s
user    0m20.592s
sys     0m4.383s


$ s3cmd get s3://foo/Win11_English_x64v1.iso --multipart-chunk-size-mb=1000 --no-ssl --host athos.hosts.mtl.stgraber.net:7480 --host-bucket athos.hosts.mtl.stgraber.net:7480 --access_key TNZAYZSYIHM243PS8337 --secret_key xbBTY8exhnXdm3uwEcsBjeBVBFzi4n4NOhtOEYa3
download: 's3://foo/Win11_English_x64v1.iso' -> './Win11_English_x64v1.iso'  [1 of 1]
 5565052928 of 5565052928   100% in   31s   170.59 MB/s  done

