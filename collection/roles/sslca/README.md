# Description
Provides tasks for creating and operating certificate authority.

# Using this role with tags
- `overview` Information about the role operations
- `authority-build` Construct the certificate authorities
- `certificate-build` Construct the certificate from request

# Example with role and tags
```yaml
- hosts: ...
  tasks:

    - name: Information about the role operations
      import_role:
        name: enasisnetwork.certauth.sslca
      tags: overview
```

# Example from command line
*Information about the role operations*
```
ansible-playbook \
  ...
  --tags "overview" \
  enasisnetwork.certauth.sslca
```

## Variables for Ansible inventory
- `sslca_authority` Certificate authority parameters
    - Expects `list[dict]` or `dict[str, list[dict]]`
    - `name` Used for the directory naming
    - `password` Passphrase for encrypting key
    - `parent` Determine to be an intermediate
    - `expire` When new certificates expire
- `sslca_certificate` Signed certificate parameters
    - Expects `list[dict]` or `dict[str, list[dict]]`
    - `name` Used for the directory naming
    - `kind` Kind of certificate to create
    - `common` Common name for certificate
    - `alias` Subject alternative names
    - `parent` From which authority to sign
    - `expire` When new certificates expire
- `sslca_persist` Where certificate files are stored
    - You may specify values here, or in explicit below.
    - `rootkeys` Where the root keys are stored
    - `rootfiles` Where the root files are stored
    - `certkeys` Where the cert keys are stored
    - `certfiles` Where the cert files are stored
- `sslca_persist_rootkeys` Where the root keys are stored
- `sslca_persist_rootfiles` Where the root files are stored
- `sslca_persist_certkeys` Where the cert keys are stored
- `sslca_persist_certfiles` Where the cert files are stored
- `sslca_defaults` Default authority parameter values
    - You may specify values here, or in explicit below.
    - `company` Default authority parameter value
    - `department` Default authority parameter value
    - `country` Default authority parameter value
    - `website` Default authority parameter value
- `sslca_defaults_company` Default authority parameter value
- `sslca_defaults_department` Default authority parameter value
- `sslca_defaults_country` Default authority parameter value
- `sslca_defaults_website` Default authority parameter value
- `sslca_openssl` Path to OpenSSL executable binary

Check out the parameter model on
[GitHub](https://github.com/enasisnetwork/ansible-certauth/blob/main/collection/plugins/action/sslca/params.py)
for more information.
