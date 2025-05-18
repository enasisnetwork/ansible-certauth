# Enasis Network Ansible Certificates Collection

> :warning: This project has not released its first major version.

Project for executing the Ansible playbooks for system automation.

## Playbooks and roles within project
- `sslca` Manage the certificate authority for SSL.
- `sshca` Manage the certificate authority for SSH.

## Variables for Ansible inventory

### Certificate Authority
Validation using [this model](collection/plugins/action/sslca/params.py)
after [Ansible Jinja2 parsing](collection/roles/sslca/tasks/params.yml).
- `sslca_authority`
- `sslca_certificate`
- `sslca_persist`
  - You may specify values here, or in explicit below.
- `sslca_persist_rootkeys`
- `sslca_persist_rootfiles`
- `sslca_persist_certkeys`
- `sslca_persist_certfiles`
- `sslca_defaults`
  - You may specify values here, or in explicit below.
- `sslca_defaults_company`
- `sslca_defaults_department`
- `sslca_defaults_country`
- `sslca_defaults_website`
- `sslca_openssl`


# NOTE Remember to update the README file

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
