import sys
import os
from unittest.mock import patch, MagicMock
import pytest

# Adjusting the path to find 'local_manifest.py' in the 'manifest' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import manifest.local_manifest as local_manifest  # This imports 'local_manifest.py' correctly

@pytest.fixture
def mock_manifest_data():
    # Mock data for testing
    return {
        'task_id': '12345',
        'task_name': 'Test Task',
        'related_comments': 'Test Comment'
    }

# Patch the 'json' module used inside the local_manifest module
@patch('manifest.local_manifest.json.load')
@patch('manifest.local_manifest.open')
def test_get_manifest(mock_open, mock_json_load, mock_manifest_data):
    # Mocking the open and json.load methods to simulate loading a manifest from a file
    mock_open.return_value.__enter__.return_value = mock_manifest_data
    mock_json_load.return_value = mock_manifest_data

    result = local_manifest.get_manifest()
    
    # Verify if the result matches the mock data
    assert result == mock_manifest_data
    mock_open.assert_called_once_with('manifest.json', 'r')
    mock_json_load.assert_called_once()

# # Patch the 'json' module used inside the local_manifest module
# @patch('manifest.local_manifest.json.dump')
# @patch('manifest.local_manifest.open')
# def test_create_manifest(mock_open, mock_json_dump, mock_manifest_data):
#     # Mocking open and json.dump methods to simulate creating a manifest
#     mock_open.return_value.__enter__.return_value = MagicMock()
    
#     # Calling create_manifest to test the function's behavior
#     local_manifest.create_manifest(mock_manifest_data)

#     # Verifying that json.dump is called with the correct parameters
#     mock_open.assert_called_once_with('manifest.json', 'w')
#     mock_json_dump.assert_called_once_with(mock_manifest_data, mock_open.return_value.__enter__.return_value)

# @patch('manifest.local_manifest.get_manifest')
# @patch('manifest.local_manifest.open')
# def test_lookup_in_manifest(mock_get_manifest, mock_open, mock_manifest_data):
#     # Mocking get_manifest to return mock data
#     mock_get_manifest.return_value = mock_manifest_data
#     mock_open.return_value.__enter__.return_value = mock_manifest_data

#     # You need to provide both arguments that lookup_in_manifest() expects
#     result = local_manifest.lookup_in_manifest('task_id', mock_manifest_data)
    
#     # Verifying that it returns the correct task_id
#     assert result == '12345'
#     mock_get_manifest.assert_called_once()
