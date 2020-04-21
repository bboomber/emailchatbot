#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    # MicrosoftAppId = <appId>
    # MicrosoftAppPassword = <appSecret>
    MICROSOFT_APP_ID = "b0700516-25f2-4ebd-a3f8-e2436864e21f"
    MICROSOFT_APP_PASSWORD = "tYFypoc4=@8g?Pfae17gf=stCm:o]ikR"
