#!/usr/bin/python3
"""Initializes the file storage for the application"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
