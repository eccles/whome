# Home directory on separate disk

This procedure transfers the /home directory to a separate disk

Note that this procedure was documented from memory and may be incomplete.

## Environment

This procedure was used when installing POP OS 22.04.

This may work for other distros.

## Why

Trying to install /home on a separate disk does not work using the standard
installation procedure using the pop os installer particularly if encrypting
the separate disk is required.

## Overview

- Install Pop OS on one of the 2 disks as normal
- login 
- using the disks application create an encrypted partition on the second disk called 'home'
	- change properties such that is decrypted at startup
	- change properties of the partition and ensure that it mounts at startup and not session defaults
	- make the mount point /newhome
        - sudo mkdir /newhome
	- reboot
- copy /home to /newhome
- ensure that permissions are correct
- rename /home to /oldhome
- sudo mkdir /home
- edit /etc/fstab and change /newhome to /home
- reboot
- delete /oldhome

## Steps

Assuming one has installed Pop os login as user.

## Prepare the external disk

    - create one partition on the external disk using fdisk utility. 
    - alternatively use GNOME disks utility to encrypt and partition disk.

$DEV will typically be /dev/nvme1n1

As sudo execute:

    - sudo cryptsetup -v --verify-passphrase luksFormat $DEV   # Answer YES in CAPITAL
    - sudo cryptsetup luksOpen $DEV home
    - sudo mkfs.ext4 -L Home /dev/mapper/home
    - sudo cryptsetup luksClose /dev/mapper/home

## System configuration

### Mount and unmount external drive.

```
UUID=$(blkid $DEV | cut -d' ' -f2 | cut -d'"' -f2)
```
gives (for example).

```
b0aced4a-0bd6-4560-bc06-3323fdca529d.
```
Create the necessary files:

```bash
echo "luks-$UUID UUID=$UUID /etc/luks-keys/$UUID" >> /etc/crypttab
echo "$PASSWORD" > /etc/luks-keys/$UUID
echo "LABEL=Home /newhome ext4 noatime,errors=remount-ro 0 1" >> /etc/fstab
mkdir /newhome
```

Reload systemd:

```bash
systemctl daemon-reload
```

Check all files touched do not have duplicate entries.

Test that mounting works without requiring passphrase.

```bash
sudo mount /newhome
sudo ls -l /newhome
sudo umount /newhome
```

## Reboot

Check that /newhome is mounted automatically.
Only ONE prompt for the decryption key should occur for the system disk.
/newhome should decrypt and mount successfully

## Move home directory

Login as user $USER

```bash
sudo sed -i "s/newhome/home/" /etc/fstab
sudo cp -r /home/$USER /newhome/$USER
sudo chown -r $USER:$USER /newhome/$USER
sudo mv /home /oldhome
sudo reboot
```
## Tidy up

Remove old home directory:


```bash
sudo rm -rf /oldhome
```
