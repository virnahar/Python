#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Find AD User's Email ID.
Install pyad module before running this script using pip install pyad.

Usage:
    ./ADUserInfo.py

Author:
    Virendra Kumar - 11 July 2021
"""
import os
from pyad import adquery

username = os.environ['username']
q = adquery.ADQuery()

# Provide the correct DN where you want to search the user
dn="OU=myorg,DC=example,DC=com"

q.execute_query(
    attributes = ['mail'],
    where_clause = "objectClass = 'user' and mailNickname = '{}'".format(username),
	base_dn = dn
)
for row in q.get_results():
    print("Hey "+username+" Your Mail ID is:"+row["mail"])
