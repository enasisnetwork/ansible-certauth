"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget roles/params.yml
# NOTE Remember to update README file



from typing import Annotated
from typing import Any
from typing import Literal
from typing import Optional

from encommon.times import Time
from encommon.types import BaseModel

from pydantic import Field
from pydantic import field_validator



class ChildParams(BaseModel, extra='forbid'):
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

    extras: Annotated[
        Optional[list[Literal['pkcs12']]],
        Field(None,
              description='Additional output certificates')]


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
        'extras',
        mode='before')
    @classmethod
    def parse_extras(
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
