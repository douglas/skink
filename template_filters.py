#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Copyright Bernardo Heynemann <heynemann@gmail.com>

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import hashlib

def _parse_email(text):
    if text == None:
        return ""

    result = re.match(".*<(?P<email>.*@.*)>", text)

    if not result:
        return ""

    return result.groupdict()["email"]
    
def gravatar(value):
    gravatar_base_url = "http://gravatar.com/avatar/"

    email = _parse_email(value)
    
    if email == "":
        return gravatar_base_url

    md5 = hashlib.md5()
    md5.update(email)

    image_path = gravatar_base_url + md5.hexdigest()

    return image_path


def email(value):
    return _parse_email(value)