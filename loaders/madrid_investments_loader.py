# -*- coding: UTF-8 -*-
from budget_app.models import *
from budget_app.loaders import InvestmentsLoader
import csv
import re

class MadridInvestmentsLoader(InvestmentsLoader):

    # An artifact of the in2csv conversion of the original XLS files is a trailing '.0', which we remove here
    def clean(self, s):
        return s.split('.')[0]

    def parse_item(self, filename, line):
        # Skip empty/header/subtotal lines
        if line[0] in ['', '*', 'Fondo']:
            return

        # Extract metadata from filename
        year = re.search('municipio/(\d+)/', filename).group(1)
        is_actual = (filename.find('/ejecucion_')!=-1)

        # 2017 data is in a different format to previous years
        if int(year) < 2017:
            project_id = line[3]
            description = line[4]
            gc_code = line[0]
            amount = line[5]
        else:
            project_id = line[7]
            description = unicode(line[8], encoding='iso-8859-1').encode('utf8')
            gc_code = line[9]
            amount = line[28 if is_actual else 23]

        return {
            'is_actual': is_actual,
            'gc_code': self.clean(gc_code).strip(),
            'amount': self.parse_amount(amount),
            'project_id': project_id.strip(),
            'description': project_id.strip() + ' ' + self._titlecase(description)
        }


    # Parse a numerical amount, which can be in English format (for those CSVs generated
    # from XLS via in2csv) or Spanish.
    def parse_amount(self, amount):
        if ',' in amount:
            amount = amount.replace(',', '.')
        return self._read_english_number(amount)

    # Override default input delimiter
    def _get_delimiter(self):
        return ';'
