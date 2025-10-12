## Trying out kali linux on podman from start to end

[Podman](https://docs.podman.io/en/latest/) defined as a daemonless, open source, Linux native tool designed to make it easy to find, run, build, share and deploy applications using Open Containers Initiative (OCI) Containers and Container Images. The containers can be run by root with netavark default n/w which allows a container to have a routable IP address or by a non-privileged user using default network mode of slirp4netns.

### 1. installing podman

To start of, I'm running Debian GNU/Linux 13 (trixie) x86_64 on bash shell 5.2.37 and GNOME 48.4 as my DE.

- `sudo apt update`
- `sudo apt-get -y install podman` # install package
- `podman --version` # confirm installation


### 2. installing kali-linux

Head over to [kali](https://www.kali.org/get-kali/#kali-containers) to get the image in shortname, confirm this by checking the **shortnames.conf**  in */etc/containers/registries.conf.d/shortnames.conf*

Mine has, so, onto the next...

- `podman pull kali-rolling` # to get kali image
- `podman run --tty --interactive kali-rolling` # to run the container

> NB: "the images do not come with the “default” metapackage." and "I will need to apt update && apt -y install (your metapackage)." to install my [metapackage](https://www.kali.org/docs/general-use/metapackages/).  
NB: If exited, resume by running `podman ps -a` to get image ID, then `podman start 'ID'` and finally `podman attach 'ID'`

1. I first need to check if am root.

- `whoami` # since am root I can proceed otherwise, continue with sudo

2. then update as recomended.

- `sudo apt update` && `sudo apt full-upgrade -y`

![kali image](imgs\kali_1.png)

3. Use kali-tweaks to install metapackage groups.

- `apt install kali-tweaks`
- `dpkg -s kali-tweaks` # confirm installation
- `kali-tweaks`

Proceed as follows; I chose 802.11 for Wi-Fi

![kali image](imgs\metapkg.png)
![kali image](imgs\Wifi_tool.png)

