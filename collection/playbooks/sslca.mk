# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: sslca-overview
sslca-overview: \
	.check-stage .check-limit
	@## Dump information related to operation
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>sslca-overview<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] \
			&& set -a \
			&& . ./orchestro.env \
			&& set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=overview \
			enasisnetwork.certauth.sslca; \
		deactivate)



.PHONY: sslca-authority-build
sslca-authority-build: \
	.check-stage .check-limit
	@## Construct the certificate authorities
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>sslca-authority-build<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] \
			&& set -a \
			&& . ./orchestro.env \
			&& set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible_serial="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=authority-build \
			enasisnetwork.certauth.sslca; \
		deactivate)



.PHONY: sslca-certificate-build
sslca-certificate-build: \
	.check-stage .check-limit
	@## Construct and sign the certificates
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>sslca-certificate-build<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] \
			&& set -a \
			&& . ./orchestro.env \
			&& set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible_serial="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags=certificate-build \
			enasisnetwork.certauth.sslca; \
		deactivate)
