#!/usr/bin/python3
"""Converts modules to package and store them."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
