"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from os import environ
from pathlib import Path
from sys import executable

from _pytest.capture import CaptureFixture

from pytest_ansible.molecule import MoleculeScenario



def test_default(
    molecule_scenario: MoleculeScenario,
    capfd: CaptureFixture[str],
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param molecule_scenario: Fixture for testing scenarios.
    :param capfd: pytest object for capturing print message.
    """

    environ['PATH'] = (
        f'{Path(executable).parent}'
        f":{environ['PATH']}")

    proc = molecule_scenario.test()

    assert proc.returncode == 1


    stdout, stderr = (
        capfd.readouterr())

    expect = (
        'No key/value '
        'pairs provided')

    assert expect in stdout
