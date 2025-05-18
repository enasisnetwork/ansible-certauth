"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget about params.yml
# NOTE Remember to update README file



from pathlib import Path
from typing import Annotated
from typing import Any
from typing import Optional

from ansible.plugins.action import ActionBase  # type: ignore

from encommon.types import BaseModel
from encommon.types import DictStrAny
from encommon.types import sort_dict

from pydantic import Field
from pydantic import field_validator
from pydantic import model_validator

from .child import ChildParams
from .default import DefaultParams
from .parent import ParentParams
from .persist import PersistParams



class RoleParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    authority: Annotated[
        Optional[list[ParentParams]],
        Field(None,
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
        Field(...,
              description='Path to OpenSSL executable binary',
              min_length=5)]


    def __init__(
        # NOCVR
        self,
        /,
        **data: Any,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """


        fields = (
            'persist',
            'defaults')

        for key in list(data):

            if '_' not in key:
                continue

            base, name = (
                key.split('_', 1))

            if base not in fields:
                continue

            if base not in data:
                data[base] = {}

            _data = data[base]
            value = data[key]

            _data[name] = value

            del data[key]


        super().__init__(**data)


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

        args = self._task.args

        assert task_vars is not None

        prefix = args['prefix']
        source = task_vars

        source = {
            k[len(prefix):]: v
            for k, v in source.items()
            if k.startswith(prefix)
            and v not in [None, '']}


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
