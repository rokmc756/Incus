
POST /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/backups
GET /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/backups/{backupName}/export
DELETE /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/backups/{backupName}

incus --debug storage volume import default backup.tar.gz my-volume


