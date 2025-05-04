"""
server_health.py

This example shows how to check the server health using the
Talkomatic REST API.
"""

from talkomatic.api.v1 import ServerHealth # we import the ServerHealth class from the Talkomatic API module

from datetime import datetime # we import the datetime module to format the uptime


health = ServerHealth.get() # we get the server health using the get method

print(f"Server status: {health.status}") # we print the server status
if health.status:
    uptime = datetime.fromtimestamp(health.uptime).strftime("%H:%M:%S") # we format the uptime
    print(f"Server uptime: {uptime}") # we print the server uptime
    print(f"Server version: {health.server_version}") # we print the server version
