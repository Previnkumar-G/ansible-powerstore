# Copyright: (c) 2021, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock ApiException for PowerStore Test modules"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockApiException(Exception):
    body = "PyPowerStore Error message"
    status = "500"
