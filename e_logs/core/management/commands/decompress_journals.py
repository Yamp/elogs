import json
import os
import zipfile
from shutil import copytree, rmtree

from django.core.management.base import BaseCommand

from django.conf import settings

from e_logs.common.all_journals_app.services.journal_builder import JournalBuilder
from e_logs.core.utils.loggers import stdout_logger
from .database_filler import Journal


def decompress_journals():
    for plant_name in os.listdir(settings.JOURNALS_DIR):
        if plant_name[0] != '.':
            if os.path.isdir(settings.JOURNALS_DIR / plant_name):
                for file_name in os.listdir(settings.JOURNALS_DIR / plant_name):
                    if file_name.endswith(f'.{settings.JOURNAL_EXTENSION}'):
                        stdout_logger.info(file_name)
                        journal = JournalBuilder(settings.JOURNALS_DIR / plant_name / file_name, plant_name)
                        journal.create()


class Command(BaseCommand):
    def handle(self, *args, **options):
        decompress_journals()
