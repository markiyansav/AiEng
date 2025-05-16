"""
Test cases for the main module.
"""

import pytest
from src.main import greet

def test_greet_with_name():
    """Test greet function with a specific name."""
    result = greet("Alice")
    assert result == "Hello, Alice! Welcome to the Simple Python Project!"
    assert isinstance(result, str)

def test_greet_with_empty_string():
    """Test greet function with an empty string."""
    result = greet("")
    assert result == "Hello, ! Welcome to the Simple Python Project!"
    assert isinstance(result, str)

def test_greet_with_special_characters():
    """Test greet function with special characters."""
    result = greet("@#$%")
    assert result == "Hello, @#$%! Welcome to the Simple Python Project!"
    assert isinstance(result, str) 