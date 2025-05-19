"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget roles/params.yml
# NOTE Remember to update README file



from pathlib import Path
from typing import Annotated

from encommon.types import BaseModel

from pydantic import Field
from pydantic import model_validator



class PersistParams(BaseModel, extra='forbid'):
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
