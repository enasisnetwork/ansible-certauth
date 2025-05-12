"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from testinfra.host import Host  # type: ignore



def test_default(
    host: Host,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param molecule_scenario: Fixture for testing scenarios.
    :param capfd: pytest object for capturing print message.
    """

    assert host.check_output('hostname') == 'enaspki1'
