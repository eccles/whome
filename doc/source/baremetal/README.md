# Bare Metal Installation Fedora Server

On each node:

## Install Fedora server 40.
   - install all software options except support for running in a VM
   - Enable wireless network point
   - set hostname and domain.
   - use the SSD disk for the root disk - leave the 2TB disk for configuration later.
   - Create a user login with administrative privileges 
   - Create root login but do not allow ssh login for root user.

## After installation:
   - Ensure that cockpit is running on port 9090
   - Install wpa_supplicant - 'sudo dnf install wpa_supplicant'
   - Update all packages and reboot
   - Enable security updates - optionally enable all updates and trigger reboot when upgrade happens.
   - Enable pcp in cockpit so that storage is monitored.
   - On your router, set the DHCP service to allocate the same IP to the same host.
   - Make a note of the hostname and IP address
   - Reboot anod check all functions correctly.
   - Install ssh key from your laptop such that passwordless login to the administrative user is enabled.

## Install k8s etc
   - sudo dnf install kubernetes
   - sudo dnf install kubernetes-ansible
   - sudo dnf install cockpit-podman


