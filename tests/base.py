#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of gnoll-python.
# https://github.com/gnoll-project/gnoll-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Matthew Conlen <mc@mathisonian.com>

from unittest import TestCase as PythonTestCase
from gnoll import GnollClient
import json

spec = json.loads('{"nodes":[{"id":0,"width":300,"height":300,"component":"DATA_COMPONENT","nodeType":"DATA_NODE","position":{"x":75.453125,"y":152}},{"id":1,"width":300,"height":300,"component":"SCATTER_COMPONENT","nodeType":"SINK_NODE","position":{"x":129.453125,"y":309}}],"edges":{"0":1}}')
transform_spec = json.loads('{"nodes":[{"id":0,"width":300,"height":300,"component":"DATA_COMPONENT","nodeType":"DATA_NODE","position":{"x":107.453125,"y":141}},{"id":1,"width":300,"height":300,"component":"SLIDER_COMPONENT","nodeType":"TRANSFORM_NODE","position":{"x":143.453125,"y":242}},{"id":2,"width":300,"height":300,"component":"SCATTER_COMPONENT","nodeType":"SINK_NODE","position":{"x":119.453125,"y":431}}],"edges":{"0":1,"1":2}}')

class TestCase(PythonTestCase):
    def test_parse_spec(self):
        gnoll = GnollClient()

        nodes = gnoll.parse_spec(spec)
        data_node = nodes.find_by_id(0)
        data_node.set_data([{'x': 0, 'y': 0}])

        gnoll.shutdown()
