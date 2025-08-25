# Operation recipes for managing the projects and execution environment.
#
# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.
#
# This file is present within multiple projects, simplifying dependency.



PYTHON ?= ../../Execution/python312/bin/python

VENVP ?= .venv-package
VENVD ?= .venv-develop



MAKE_COLOR ?= 6

MAKE_PRINT = @COLOR=$(MAKE_COLOR) \
	$(PYTHON) -Bc 'if 1: \
		from makefile import makeout; \
		makeout("$(1)", "$(2)");'

MAKE_PR1NT = $(call MAKE_PRINT,$(1),text)
MAKE_PR2NT = $(call MAKE_PRINT,$(1),base)
MAKE_PR3NT = $(call MAKE_PRINT,$(1),more)



PROJECT := $(shell \
	$(PYTHON) -Bc 'if 1: \
		from makefile import PROJECT; \
		print(PROJECT);')



.PHONY: help
help: .check-python
	@## Construct this helpful menu of recipes
	$(call MAKE_PRINT)
	@COLOR=$(MAKE_COLOR) \
		$(PYTHON) -B makefile.py
	$(call MAKE_PRINT)



.PHONY: cleanup
cleanup:
	@## Executes all various cleanup for cache
	@$(MAKE) cleanup-pycache
	@$(MAKE) cleanup-pytest
	@$(MAKE) cleanup-coveragepy
	@$(MAKE) cleanup-ruff
	@$(MAKE) cleanup-mypy
	@$(MAKE) cleanup-ansible



.PHONY: linters
linters:
	@## Executes all various linters and tests
	@$(MAKE) flake8
	@$(MAKE) pylint
	@$(MAKE) ruff
	@$(MAKE) mypy
	@$(MAKE) yamllint
	@$(MAKE) ansblint



.PHONY: linters-pass
linters-pass:
	@## Executes all various linters and tests
	@$(MAKE) flake8 || true
	@$(MAKE) pylint || true
	@$(MAKE) ruff || true
	@$(MAKE) mypy || true
	@$(MAKE) yamllint || true
	@$(MAKE) ansblint || true



.PHONY: check
check:
	@## Executes all various linters and tests
	@$(MAKE) linters
	@$(MAKE) pytest



.PHONY: check-revenv
check-revenv:
	@## Executes all various linters and tests
	@$(MAKE) venv-remove
	@$(MAKE) venv-create
	@$(MAKE) check



.PHONY: cleanup-pycache
cleanup-pycache:
	@## Remove temporal generated cache files
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>cleanup-pycache<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Removing <c90>Python<c37> \
		cache files..<c0>)
	@find . \
		-name '__pycache__' \
		-exec rm -rf '{}' \; \
		2>/dev/null || true
	@find . \
		-name '*.pyc' \
		-delete \; \
		2>/dev/null || true
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: cleanup-pytest
cleanup-pytest:
	@## Remove temporal generated cache files
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>cleanup-pytest<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Removing <c90>pytest<c37> \
		cache files..<c0>)
	@find . \
		-maxdepth 1 \
		-name '.pytest_cache' \
		-exec rm -rf '{}' \; \
		2>/dev/null || true
	@find . \
		-maxdepth 1 \
		-name 'pytestdebug.log' \
		-delete \; \
		2>/dev/null || true
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: cleanup-coveragepy
cleanup-coveragepy:
	@## Remove temporal generated cache files
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>cleanup-coveragepy<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Removing <c90>coveragepy<c37> \
		cache files..<c0>)
	@find . \
		-maxdepth 1 \
		-name 'htmlcov' \
		-exec rm -rf '{}' \; \
		2>/dev/null || true
	@find . \
		-maxdepth 1 \
		-name '.coverage' \
		-exec rm -rf '{}' \; \
		2>/dev/null || true
	@find . \
		-maxdepth 1 \
		-name 'coverage.json' \
		-exec rm -rf '{}' \; \
		2>/dev/null || true
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: cleanup-ruff
cleanup-ruff:
	@## Remove temporal generated cache files
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>cleanup-ruff<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Removing <c90>mypy<c37> \
		cache files..<c0>)
	@find . \
		-maxdepth 1 \
		-name '.ruff_cache' \
		-exec rm -rf '{}' \; \
		2>/dev/null || true
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: cleanup-mypy
cleanup-mypy:
	@## Remove temporal generated cache files
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>cleanup-mypy<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Removing <c90>mypy<c37> \
		cache files..<c0>)
	@find . \
		-maxdepth 1 \
		-name '.mypy_cache' \
		-exec rm -rf '{}' \; \
		2>/dev/null || true
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: cleanup-ansible
cleanup-ansible:
	@## Remove temporal generated cache files
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>cleanup-ansible<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Removing <c90>Ansible<c37> \
		cache files..<c0>)
	@find . \
		-maxdepth 2 \
		-name '.ansible' \
		-exec rm -rf '{}' \; \
		2>/dev/null || true
	@find . \
		-maxdepth 1 \
		-name 'collections' \
		-exec rm -rf '{}' \; \
		2>/dev/null || true
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Remove <c90>package<c37> \
		cache files..<c0>)
	@find . \
		-maxdepth 1 \
		-name 'enasisnetwork-*-*.tar.gz' \
		-exec rm '{}' \; \
		2>/dev/null || true
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: venv-create
venv-create: \
	.check-python
	@## Create the virtual Python environments
	@#
	@$(MAKE) cleanup
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>venv-create<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Building <c90>develop<c37> \
		virtual environment..<c0>)
	@$(PYTHON) -m venv $(VENVD)
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Upgrading <c90>develop<c37> \
		virtual environment..<c0>)
	@$(VENVD)/bin/pip install \
		--upgrade pip 1>/dev/null
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Preparing <c90>develop<c37> \
		virtual environment..<c0>)
	@$(VENVD)/bin/pip install \
		-r require/develop.txt 1>/dev/null
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Building <c90>package<c37> \
		virtual environment..<c0>)
	@$(PYTHON) -m venv $(VENVP)
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Upgrading <c90>package<c37> \
		virtual environment..<c0>)
	@$(VENVP)/bin/pip install \
		--upgrade pip 1>/dev/null
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Preparing <c90>package<c37> \
		virtual environment..<c0>)
	@$(VENVP)/bin/pip install \
		-r require/package.txt 1>/dev/null
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: venv-remove
venv-remove:
	@## Remove the virtual Python environments
	@#
	@$(MAKE) cleanup
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>venv-remove<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Removing <c90>develop<c37> \
		virtual environment..<c0>)
	@rm -rf $(VENVD)
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Removing <c90>package<c37> \
		virtual environment..<c0>)
	@rm -rf $(VENVP)
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: pytest
pytest: \
	.check-venv-package
	@## Execute the relevant linters and tests
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>pytest<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>pytest<c37> \
		in <c90>collection<c37>..<c0>)
	$(VENVP)/bin/pytest -v \
		collection/$(subpackage) \
		--numprocesses=4 \
		--cov=collection/$(subpackage) \
		--doctest-modules \
		$(pytest_args)
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Write <c90>coveragepy<c37> \
		output to <c90>htmlcov<c37>..<c0>)
	@$(VENVD)/bin/coverage html 1>/dev/null
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Write <c90>coveragepy<c37> \
		output to <c90>coverage.json<c37>..<c0>)
	@$(VENVD)/bin/coverage json 1>/dev/null
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: mypy
mypy: \
	.check-venv-develop
	@## Execute the relevant linters and tests
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>mypy<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>mypy<c37> \
		in <c90>collection<c37>..<c0>)
	@$(VENVD)/bin/mypy \
		--no-error-summary \
		$(mypy_args) collection
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>mypy<c37> \
		on <c90>makefile.py<c37>..<c0>)
	@$(VENVD)/bin/mypy \
		--no-error-summary \
		$(mypy_args) makefile.py
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: flake8
flake8: \
	.check-venv-develop
	@## Execute the relevant linters and tests
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>flake8<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>flake8<c37> \
		in <c90>collection<c37>..<c0>)
	@$(VENVD)/bin/flake8 \
		collection --allow-star-arg-any
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>flake8<c37> \
		on <c90>makefile.py<c37>..<c0>)
	@$(VENVD)/bin/flake8 ./makefile.py
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: pylint
pylint: \
	.check-venv-develop
	@## Execute the relevant linters and tests
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>pylint<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>pylint<c37> \
		in <c90>collection<c37>..<c0>)
	@$(VENVD)/bin/pylint \
		-E collection \
		--persistent=n \
		-d duplicate-code
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>pylint<c37> \
		on <c90>makefile.py<c37>..<c0>)
	@$(VENVD)/bin/pylint \
		-E makefile.py \
		--persistent=n \
		-d duplicate-code
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: ruff
ruff: \
	.check-venv-develop
	@## Execute the relevant linters and tests
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>ruff<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>ruff<c37> \
		in <c90>collection<c37>..<c0>)
	@$(VENVD)/bin/ruff \
		check -q collection
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>ruff<c37> \
		on <c90>makefile.py<c37>..<c0>)
	@$(VENVD)/bin/ruff \
		check -q makefile.py
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: yamllint
yamllint: \
	.check-venv-develop
	@## Execute the relevant linters and tests
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>yamllint<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>yamllint<c37> \
		in <c90>collection<c37>..<c0>)
	@$(VENVD)/bin/yamllint \
		-s collection
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>yamllint<c37> \
		on <c90>.yamllint<c37>..<c0>)
	@$(VENVD)/bin/yamllint \
		-s .yamllint
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>yamllint<c37> \
		on <c90>.ansible-lint<c37>..<c0>)
	@$(VENVD)/bin/yamllint \
		-s .ansible-lint
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>yamllint<c37> \
		in <c90>collection<c37>..<c0>)
	@$(VENVD)/bin/yamllint \
		-s collection
	$(call MAKE_PR1NT,<cD>DONE<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>yamllint<c37> \
		in <c90>.github<c37>..<c0>)
	@$(VENVD)/bin/yamllint \
		-s .github
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: ansblint
ansblint: \
	.check-venv-develop
	@## Execute the relevant linters and tests
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>ansblint<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>ansible-lint<c37> \
		on <c90>project<c37>..<c0>)
	@( \
		set -e; \
		. $(VENVD)/bin/activate; \
		cd collection; \
		ANSIBLE_JINJA2_EXTENSIONS="jinja2.ext.do" \
		ansible-lint \
			-q --strict \
			--project-dir . \
			--show-relpath \
			--offline \
			-c ../.ansible-lint \
			.; \
		deactivate)
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: outdated
outdated: \
	.check-venv-package
	@## Check outdated packages in requirements
	@#
	@$(MAKE) cleanup
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>outdated<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Process <c90>outdated<c37> \
		installed <c90>packages<c37>..<c0>)
	@$(VENVP)/bin/pip list \
		--outdated \
		| egrep -v '^(pip|setuptools) '
	@$(VENVP)/bin/pip freeze \
		-r require/package.txt \
		> require/.package.txt
	@diff -B -I '^#' \
		--color require/install.txt \
		require/.package.txt || true
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: cloc
cloc:
	@## Breakdown lines of code within the project
	@#
	@$(MAKE) cleanup
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>cloc<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Executing <c90>cloc<c37> \
		in <c90>collection<c37>..<c0>)
	@cloc collection
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: galaxy-build
galaxy-build: \
	.check-venv-develop
	@## Create the Python compatible package
	@#
	@$(MAKE) cleanup
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>galaxy-build<c0>)
	@#
	$(call MAKE_PR3NT,\
		<c37>Create <c90>package<c37> \
		build directory..<c0>)
	ANSIBLE_CONFIG=~/.galaxy.cfg \
		$(VENVP)/bin/ansible-galaxy \
		collection build collection
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.PHONY: galaxy-upload
galaxy-upload: \
	.check-venv-develop
	@## Upload collection to Ansible Galaxy
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>galaxy-upload<c0>)
	@#
	@find . \
		-maxdepth 1 \
		-name 'enasisnetwork-*-*.tar.gz'
	@#
	@$(VENVD)/bin/python -Bc 'if 1:\
		confirm = input(\
			"Are you sure? [y/N] ");\
		assert confirm == "y";'
	@#
	@$(VENVD)/bin/python -Bc 'if 1:\
		confirm = input(\
			"Do you understand this "\
			"is production? [y/N] ");\
		assert confirm == "y";'
	@#
	$(call MAKE_PR3NT,\
		<c37>Upload to <c90>package<c37> \
		to <c90>Galaxy<c37> servers..<c0>)
	ANSIBLE_CONFIG=~/.galaxy.cfg \
		$(VENVP)/bin/ansible-galaxy \
		collection publish \
		./enasisnetwork-certauth-*.tar.gz
	$(call MAKE_PR1NT,<cD>DONE<c0>)



.check-python:
ifndef PYTHON
	$(error PYTHON variable is not defined)
endif

.check-venv-develop:
ifeq (,$(wildcard $(VENVD)))
	$(error Develop environment does not exist)
endif

.check-venv-package:
ifeq (,$(wildcard $(VENVP)))
	$(error Package environment does not exist)
endif
