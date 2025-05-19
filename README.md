# Enasis Network Ansible Certificates Collection

> This project has not released its first major version.

Ansible content for managing private key infrastructure authorities.

Check out this collection on
[Ansible Galaxy](https://galaxy.ansible.com/ui/repo/published/enasisnetwork/certauth)
for more information.

## Quick start for local development
Start by cloning the repository to your local machine.
```
git clone https://github.com/enasisnetwork/ansible-certauth.git
```
Set up the Python virtual environments expected by the Makefile.
```
make -s venv-create
```

### Execute the linters and tests
The comprehensive approach is to use the `check` recipe. This will stop on
any failure that is encountered.
```
make -s check
```
However you can run the linters in a non-blocking mode.
```
make -s linters-pass
```

## Version management
> :warning: Ensure that no changes are pending.

1. Rebuild the environment.
   ```
   make -s check-revenv
   ```

1. Update the [galaxy.yml](galaxy.yml) file.

1. Push to the `main` branch.

1. Create [repository](https://github.com/enasisnetwork/ansible-certauth) release.

1. Build the Galaxy package.<br>Be sure no uncommited files in tree.
   ```
   make -s galaxy-build
   ```

1. Upload Galaxy package to Ansible servers.
   ```
   make -s galaxy-upload
   ```
