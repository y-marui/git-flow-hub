"""test git-flow Hub."""
from git_flow_hub import __version__


def test_version():
    """Test version."""
    assert __version__ == '0.1.0'
