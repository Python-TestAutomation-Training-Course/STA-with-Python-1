import random
import pytest


@pytest.fixture
def random_url():
    random_website = random.choice(["google", "HELLO WORLD"])
    
    return f"https://www.{random_website}.com"