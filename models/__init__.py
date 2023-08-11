#!/usr/bin/python3
'''
Converts these modules to package.
'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
