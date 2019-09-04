#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © Nekoka.tt 2019
#
# This file is part of Hikari.
#
# Hikari is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hikari is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Hikari. If not, see <https://www.gnu.org/licenses/>.
import datetime
from unittest import mock

import pytest

from hikari.core.model import integration
from hikari.core.model import model_cache


@pytest.mark.model
class TestIntegration:
    def test_Integration(self):
        test_state = mock.MagicMock(state_set=model_cache.AbstractModelCache)

        user_dict = {
            "username": "Luigi",
            "discriminator": "0002",
            "id": "96008815106887111",
            "avatar": "5500909a3274e1812beb4e8de6631111",
        }

        account_dict = {"id": "123456789", "name": "lasagna"}

        inte = integration.Integration(
            test_state,
            {
                "id": "1234567",
                "name": "peepohappy",
                "type": "twitch",
                "enabled": True,
                "syncing": False,
                "role_id": "69696969",
                "expire_behavior": 2,
                "expire_grace_period": 420,
                "user": user_dict,
                "account": account_dict,
                "synced_at": "2016-03-31T19:15:39.954000+00:00",
            },
        )

        assert inte.id == 1234567
        assert inte.name == "peepohappy"
        assert inte.type == "twitch"
        assert inte.enabled is True
        assert inte.syncing is False
        assert inte._role_id == 69696969
        assert inte.expire_grace_period == 420
        assert inte.synced_at == datetime.datetime(2016, 3, 31, 19, 15, 39, 954000, tzinfo=datetime.timezone.utc)
        test_state.parse_user.assert_called_with(user_dict)


@pytest.mark.model
class TestIntegrationAccount:
    def test_IntegrationAccount(self):
        test_state = mock.MagicMock(state_set=model_cache.AbstractModelCache)

        inteacc = integration.IntegrationAccount(test_state, {"id": "1234567", "name": "memes"})

        assert inteacc.id == 1234567
        assert inteacc.name == "memes"