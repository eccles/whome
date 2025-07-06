# Proxmox

Home cluster using proxmox

## References

https://proxmox.com/en/

and helper scripts:

https://community-scripts.github.io/ProxmoxVE/scripts

## Preparation

Install proxmox ve on a pc.
Allocate fixed IP address using DHCP and mac address.
Assign a consistent name.
Use wired ethernet only.

To disable all the nags about not having a subscription use the correct
proxmox helper script:

https://community-scripts.github.io/ProxmoxVE/scripts?id=post-pve-install

and execute the following command from the internal pve shell on the web interface
available at http://<ip address>:8006 viz:

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/tools/pve/post-pve-install.sh)"
```

Answer 'yes' to all questions and  reboot.

## Monitoring

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/tools/pve/monitor-all.sh)"
```

## Firmware updates

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/tools/pve/microcode.sh)"

Reboot and check for microcode install:

```bash
journalctl -k | grep -E "microcode" | head -n 1
kernel: microcode: Current revision: 0x08608108
```

## SSD FStrim

Only works on ext4 filesystems.

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/tools/pve/fstrim.sh)"
```

## Enable High availability and clustering



