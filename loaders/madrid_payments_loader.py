# -*- coding: UTF-8 -*-

import datetime
import re

from budget_app.loaders import PaymentsLoader
from budget_app.models import Budget

class MadridPaymentsLoader(PaymentsLoader):
  # Parse an input line into fields
  def parse_item(self, budget, line):
    # But what we want as area is the programme description
    policy_id = line[1][:2]
    print policy_id
    policy = Budget.objects.get_all_descriptions(budget.entity)['functional'][policy_id]

    # Some descriptions are missing in early years
    description = line[2].strip()
    if description=="":
      description="..."

    # And some payee names have some trailing punctuation marks: one or two instances of " ."
    payee = line[3].strip()
    payee = re.sub(r'( \.)+$', '', payee)

    return {
      'area': policy,
      'fc_code': None,
      'ec_code': None,
      'date': None,
      'contract_type': None,
      'payee': payee,
      'description': description,
      'amount': self._read_english_number(line[4])
    }
