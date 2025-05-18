"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget about params.yml
# NOTE Remember to update README file



from typing import Annotated
from typing import Optional

from encommon.types import BaseModel

from pydantic import Field



class DefaultParams(BaseModel, extra='forbid'):
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
