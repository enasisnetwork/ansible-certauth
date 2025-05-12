"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget about params.yml



from pathlib import Path
from typing import Annotated
from typing import Any
from typing import Literal
from typing import Optional

from ansible.plugins.action import ActionBase  # type: ignore

from encommon.times import Time
from encommon.types import BaseModel
from encommon.types import DictStrAny
from encommon.types import sort_dict

from pydantic import Field
from pydantic import field_validator
from pydantic import model_validator



class ParentParams(BaseModel, extra='ignore'):
    """
    Process and validate the Orche configuration parameters.
    """

    name: Annotated[
        str,
        Field(...,
              description='Used for the directory naming',
              min_length=1)]

    password: Annotated[
        str,
        Field(...,
              description='Passphrase for encrypting key',
              min_length=1)]

    parent: Annotated[
        Optional[str],
        Field(None,
              description='Determine to be an intermediate',
              min_length=1)]

    expire: Annotated[
        str,
        Field(...,
              description='When new certificates expire',
              min_length=20,
              max_length=32)]


    @field_validator(
        'expire',
        mode='before')
    @classmethod
    def parse_expire(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> str:
        """
        Perform advanced validation on the parameters provided.
        """

        assert value is not None

        time = Time(value)

        return time.simple



class ChildParams(BaseModel, extra='ignore'):
    """
    Process and validate the Orche configuration parameters.
    """

    name: Annotated[
        str,
        Field(...,
              description='Used for the directory naming',
              min_length=1,
              max_length=50)]

    kind: Annotated[
        Literal['server', 'client', 'person'],
        Field(...,
              description='Kind of certificate to create')]

    common: Annotated[
        str,
        Field(...,
              description='Common name for certificate',
              min_length=1,
              max_length=254)]

    alias: Annotated[
        Optional[list[str]],
        Field(None,
              description='Subject alternative names',
              min_length=1)]

    parent: Annotated[
        str,
        Field(...,
              description='From which authority to sign',
              min_length=1)]

    expire: Annotated[
        Optional[str],
        Field(None,
              description='When new certificates expire',
              min_length=20,
              max_length=32)]


    @field_validator(
        'alias',
        mode='before')
    @classmethod
    def parse_alias(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> list[str]:
        """
        Perform advanced validation on the parameters provided.
        """

        if isinstance(value, list):
            return value

        return [value]


    @field_validator(
        'expire',
        mode='before')
    @classmethod
    def parse_expire(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> Optional[str]:
        """
        Perform advanced validation on the parameters provided.
        """

        if value is None:
            return None

        time = Time(value)

        return time.simple



class DefaultParams(BaseModel, extra='ignore'):
    """
    Process and validate the Orche configuration parameters.
    """

    company: Annotated[
        str,
        Field(...,
              description='Default authority parameter value',
              min_length=1)]

    department: Annotated[
        str,
        Field(...,
              description='Default authority parameter value',
              min_length=1)]

    country: Annotated[
        str,
        Field(...,
              description='Default authority parameter value',
              min_length=1)]

    website: Annotated[
        Optional[str],
        Field(None,
              description='Default authority parameter value',
              min_length=1)]



class PersistParams(BaseModel, extra='ignore'):
    """
    Process and validate the Orche configuration parameters.
    """

    rootkeys: Annotated[
        str,
        Field(...,
              description='Where the root keys are stored',
              min_length=1)]

    rootfiles: Annotated[
        str,
        Field(...,
              description='Where the root files are stored',
              min_length=1)]

    certkeys: Annotated[
        str,
        Field(...,
              description='Where the cert keys are stored',
              min_length=1)]

    certfiles: Annotated[
        str,
        Field(...,
              description='Where the cert files are stored',
              min_length=1)]


    @model_validator(mode='after')
    def check_exists(
        # NOCVR
        self,
    ) -> 'PersistParams':
        """
        Perform advanced validation on the parameters provided.
        """

        checks = [
            'rootkeys',
            'rootfiles',
            'certkeys',
            'certfiles']

        for check in checks:

            value = getattr(self, check)

            exists = (
                Path(value)
                .parent
                .exists())

            if exists is True:
                continue

            raise ValueError(
                f'{check} path does not'
                ' exist on filesystem')

        return self



class RoleParams(BaseModel, extra='ignore'):
    """
    Process and validate the Orche configuration parameters.
    """

    authority: Annotated[
        Optional[list[ParentParams]],
        Field(...,
              description='Certificate authority parameters',
              min_length=1)]

    certificate: Annotated[
        Optional[list[ChildParams]],
        Field(None,
              description='Signed certificate parameters',
              min_length=1)]

    persist: Annotated[
        PersistParams,
        Field(...,
              description='Where certificate files are stored')]

    defaults: Annotated[
        DefaultParams,
        Field(...,
              description='Default authority parameter values')]

    openssl: Annotated[
        str,
        Field('/usr/bin/openssl',
              description='Path to OpenSSL executable binary',
              min_length=5)]


    @field_validator(
        'authority',
        mode='before')
    @classmethod
    def parse_authority(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> Optional[list[ParentParams]]:
        """
        Perform advanced validation on the parameters provided.
        """

        if (isinstance(value, list)
                or value is None):
            return value

        model = ParentParams

        returned: list[ParentParams] = []


        assert isinstance(value, dict)

        items = value.items()

        for key, value in items:

            value = dict(value)
            name = value.get('name')

            if name is None:
                value['name'] = key

            item = model(**value)

            returned.append(item)


        return returned


    @field_validator(
        'certificate',
        mode='before')
    @classmethod
    def parse_certificate(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> Optional[list[ChildParams]]:
        """
        Perform advanced validation on the parameters provided.
        """

        if (isinstance(value, list)
                or value is None):
            return value

        model = ChildParams

        returned: list[ChildParams] = []


        assert isinstance(value, dict)

        items = value.items()

        for key, value in items:

            value = dict(value)
            name = value.get('name')

            if name is None:
                value['name'] = key

            item = model(**value)

            returned.append(item)


        return returned


    @field_validator(
        'openssl',
        mode='before')
    @classmethod
    def parse_openssl(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> str:
        """
        Perform advanced validation on the parameters provided.
        """

        path = Path(value)

        if path.exists():
            return str(path)

        raise ValueError(
            'path for openssl'
            ' does not exist')


    @model_validator(mode='after')
    def check_authority(
        # NOCVR
        self,
    ) -> 'RoleParams':
        """
        Perform advanced validation on the parameters provided.
        """

        authority = self.authority

        if not authority:
            return self

        names = sorted(
            x.name for x in
            authority)

        _names = sorted(set(names))

        if names != _names:
            raise ValueError(
                'duplicate name used'
                ' by an authority')

        for item in authority:

            parent = item.parent
            name = item.name

            if parent is None:
                continue

            if parent in names:
                continue

            raise ValueError(
                'parent for authority'
                f' {name} not exists')

        return self


    @model_validator(mode='after')
    def check_certificate(
        # NOCVR
        self,
    ) -> 'RoleParams':
        """
        Perform advanced validation on the parameters provided.
        """

        authority = self.authority
        certificate = self.certificate

        if not certificate:
            return self

        assert authority is not None

        names = sorted(
            x.name for x in
            certificate)

        _names = sorted(set(names))

        parents = [
            x.name for x in
            authority]

        if names != _names:
            raise ValueError(
                'duplicate name used'
                ' by certificate')

        for item in certificate:

            parent = item.parent
            name = item.name

            if parent in parents:
                continue

            raise ValueError(
                'parent for certificate'
                f' {name} not exists')

        return self



class ActionModule(ActionBase):  # type: ignore
    """
    Perform whatever operation is associated with the file.
    """


    def run(
        # NOCVR
        self,
        tmp: Optional[str] = None,
        task_vars: Optional[DictStrAny] = None,
    ) -> DictStrAny:
        """
        Perform whatever operation is associated with the file.

        :param tmp: Placeholder for since deprecated parameter.
        :param task_vars: Variables associated around this task.
        :returns: Dictionary of results for the module process.
        """

        result: DictStrAny = {
            'params': None,
            'changed': False}

        source = self._task.args


        try:

            params = (
                RoleParams(**source)
                .endumped)

            result['params'] = (
                sort_dict(params))


        except Exception as reason:
            result |= {
                'failed': True,
                'exception': reason}


        return sort_dict(result)
