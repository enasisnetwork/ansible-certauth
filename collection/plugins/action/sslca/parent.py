"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget about params.yml



from typing import Annotated
from typing import Any
from typing import Optional

from encommon.times import Time
from encommon.types import BaseModel

from pydantic import Field
from pydantic import field_validator



class ParentParams(BaseModel, extra='forbid'):
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
