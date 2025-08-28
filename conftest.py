import pytest
import uuid

@pytest.fixture
def unique_email():
    """Generate a unique sharklasers email address for each test run."""
    return f"testuser_{uuid.uuid4().hex[:8]}@sharklasers.com"
