import random
import pytest


@pytest.fixture(autouse=True)
def setup():
    print("\nThis is the setup fixture")
    

@pytest.fixture(autouse=True)
def clean_up():
    yield
    print("\nThis is the teardown fixture")
    
    
@pytest.fixture(autouse=True, scope="session")
def setup_session():
    print("\nThis is the session setup fixture")
    

@pytest.fixture(autouse=True, scope="session")
def clean_up_session():
    yield
    print("\nThis is the session teardown fixture")