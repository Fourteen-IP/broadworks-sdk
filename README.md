# Broadworks SDK

[![Downloads](https://static.pepy.tech/badge/broadworks-sdk)](https://pepy.tech/project/broadworks-sdk)
[![Downloads](https://static.pepy.tech/badge/broadworks-sdk/month)](https://pepy.tech/project/broadworks-sdk)
[![Downloads](https://static.pepy.tech/badge/broadworks-sdk/week)](https://pepy.tech/project/broadworks-sdk)
[![pypi version](https://img.shields.io/pypi/v/broadworks-sdk.svg)](https://pypi.python.org/pypi/broadworks-sdk)

`broadworks-sdk` provides an SDK for interfacing with Broadworks (BWKS) OCIP interface either via TCP or SOAP.

- [Documentation](https://fourteen-ip.github.io/thors-hammer/)

## Overview

`broadworks-sdk` has extensive documentation, automation, and more to better manage BWKS instances. 

The package is currently actively managed by the Dev Team at [Fourteen IP](https://fourteenip.com/). The team is working with the whole company including platform and telephony engineers with decades of experience. 

The goal of the solution is to ease the management of BWKS and give engineers tooling to better configure and administrate. 

## Features

* Interface with Broadworks OCIP SOAP or TCP API
* Command logic to seamlessly use API 
* Asynchronous version of client
* Bulk and automated features (requested by BWKS engineers with decades of experience)
* Reporting capabilities
 
> If you would like to submit a feature request please raise an issue detailing your request.

## Installation

Install Broadworks SDK using pip:

```bash
pip install broadworks-sdk
```

### Basic Usage

Here's a simple example to get you started:

```python
from broadworks-sdk import Client

# TCP Secure Conn. Defaults to TLS port 2209 - can be changed.
client = Client(
    host="url",
    username="username",
    password="password",
    # port=2208 
    # tsl=false
)

# SOAP Conn
client = Client(
    host="url", # Do not include '?wsdl'
    username="username",
    password="password",
    conn_type="SOAP"
)

# example usage
response = client.raw_command("SystemSoftwareVersionGetRequest")

print(response)
# Returns: SystemSoftwareVersionGetResponse(version='24')

print(response.to_dict()) 
# Returns: {'version': '24'}

print(response.to_json()) 
# Returns: '{'version': '24'}'

print(response.to_xml()) 
# Returns: <command ... "SystemSoftwareVersionGetResponse"><version>24</version></command>
```

### Agent Usage (In Development)


```python
from broadworks-sdk import Client, Agent

client = Client(
    host="url",
    username="username",
    password="password",
)

agent = Agent(client)

agent.automate.find_alias(
    "servicePovider",
    "groupId",
    alias=0
) # returns Broadworks enity where alias is assigned.

agent.automate.call_flow(
    "servicePovider",
    "groupId",
    "6001"
) # returns .png file in ./bwks-sdk-reports/ of a call flow to number 6001

agent.bulk.users(
    path="local/file/path"
) # Bulk builds all users in predefined bulk sheet
```

## Credits

This package builds upon the excellent work of the Broadworks OCI-P Interface package. Special thanks to:

[@nigelm (Nigel Metheringham)](https://github.com/nigelm/) – Developer of the original Python version.

Karol Skibiński – For extensive testing, bug reporting, and valuable contributions.

[@ewurch (Eduardo Würch)](https://github.com/ewurch) – For contributing the R25 schema update and other improvements.
