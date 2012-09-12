#!/usr/bin/env python
# -*- coding: utf-8 -*-
#     
#     types.py
#     
#     This file is part of the RoboEarth Cloud Engine framework.
#     
#     This file was originally created for RoboEearth
#     http://www.roboearth.org/
#     
#     The research leading to these results has received funding from
#     the European Union Seventh Framework Programme FP7/2007-2013 under
#     grant agreement no248942 RoboEarth.
#     
#     Copyright 2012 RoboEarth
#     
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#     
#     http://www.apache.org/licenses/LICENSE-2.0
#     
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#     
#     \author/s: Dominique Hunziker 
#     
#     

""" Message Types of RCE Protocol:
        
        AR  Initialization request
        AI  Routing information
        AC  Connection directives
        
        SC  Container Status
        
        IR  CommID request
        IB  CommID response
        ID  CommID delete
        
        LI  Load Information
        
        RQ  Request message
        CM  Command message
        TG  Tag message
        
        RM  ROS Message
"""

INIT_REQUEST = 'AR'
ROUTE_INFO = 'AI'
CONNECT = 'AC'      # TODO: Used?

CONTAINER_STATUS = 'SC'      # TODO: Used?

ID_REQUEST = 'IR'      # TODO: Used?
ID_RESPONSE = 'IB'      # TODO: Used?
ID_DEL = 'ID'      # TODO: Used?

LOAD_INFO = 'LI'

REQUEST = 'RQ'
COMMAND = 'CM'
TAG = 'TG'

ROS_MSG = 'RM'