import unittest
import os
import json
from unittest.mock import patch
import app


documents = []
directories = {}


def setUpModule():
    current_path = str(os.path.dirname(os.path.abspath(__file__)))
    print(current_path)
    f_directories = os.path.join(current_path, '../fixtures/directories.json')
    f_documents = os.path.join(current_path, '../fixtures/documents.json')
    with open(f_documents, 'r', encoding='utf-8') as out_docs:
        documents.extend(json.load(out_docs))
    with open(f_directories, 'r', encoding='utf-8') as out_dirs:
        directories.update(json.load(out_dirs))


@patch('app.documents', documents, create=True)
@patch('app.directories', directories, create=True)
class TestSecretaryProgram(unittest.TestCase):
    def setUp(self):
        self.example_set = {
            'shelf': 33,
            'doc': 22
        }
        self.set_valid_shelf = {
            'doc_number': "187456",
            'doc_type': "passport",
            'doc_owner_name': "Иванов Иван",
            'doc_shelf_number': "3"
        }
        self.set_invalid_shelf = {
            'doc_number': "187456",
            'doc_type': "passport",
            'doc_owner_name': "Иванов Иван",
            'doc_shelf_number': "5"
        }

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(app.get_all_doc_owners_names(), set)
        self.assertGreater(len(app.get_all_doc_owners_names()), 0)

    def test_append_doc_to_shelf(self):
        app.append_doc_to_shelf(self.example_set['doc'], self.example_set['shelf'])
        self.assertIn(self.example_set['doc'], directories.get(self.example_set['shelf']))

    def test_delete_doc(self):
        self.assertTrue(app.check_document_existance("11-2"))

        with patch('app.input', return_value="11-2"):
            app.delete_doc()

        self.assertFalse(app.check_document_existance("11-2"))

    def test_add_new_doc(self):
        self.assertIn(self.set_valid_shelf['doc_shelf_number'], directories.keys())
        self.assertTrue(len(directories.get(self.set_valid_shelf['doc_shelf_number'])) + 1)

        self.assertNotIn(self.set_invalid_shelf['doc_shelf_number'], directories.keys())


if __name__ == '__main__':
    unittest.main()

