# Thors Hammer

ADD TAGS HERE

`thors-hammer` provides an SDK for interfacing with Broadworks (BWKS) OCIP SOAP interface.

Officially adopted by [Fourteen IP Communications](https://fourteenip.com/) leading supplier of hosted telephony in the hospitality industry. 

- [Documentation](https://docs.jordan-prescott.com/thors_hammer)

![logo](./assets/images/thors-hammer.png)

## Overview

Thors Hammer is a SDK with extensive documentation, automation, and more to better manage BWKS instances. 

The package is currently actively managed by the Dev Team at [Fourteen IP](https://fourteenip.com/). The team is working with the whole company including platform and telephony engineers with decades of experience. 

The goal of the solution is to ease the management of BWKS and give engineers tooling to better configure and administrate.

The tool takes advantage of the amazing work by the developers of [broadworks-ocip](https://github.com/nigelm/broadworks_ocip). Thor's Hammer has been slightly modified to interact with SOAP API instead of using TCP. 

> [!NOTE]  
> If you are are looking to interact with the SOAP API however you do not need the additional features of Thors Hammer
> you can alternatively use [broadworks-ocip-soap](https://github.com/Jordan-Prescott/broadworks-ocip-soap).

## Features

* Interface with Broadworks OCIP SOAP API
* Provides automation features for common issues (requested by BWKS engineers with decades of experience)
* Provides automated reporting 
* Command logic to seamlessly use API 

> [!NOTE]  
> If you would like to submit a feature request please raise an issue detailing your request.

## Installation

Install Thors Hammer using pip:

```bash
pip install thors-hammer
```

### Basic Usage

Here's a simple example to get you started:

```python
from thors_hammer import API, Scripter, Reporter

# Initialize the API with your credentials
api = API(url="https://soap_api_url/", username="john.smith", password="your password", user_agent="Thors Hammer")

assistant = Scripter(api)
# Locate an alias assignment
alias_info = assistant.find_alias('ServiceProviderID', 'GroupID', alias=0)

assistant = Reporter(api)
# Generate visual call flow image. Saved as PNG.
assistant.call_flow(
    'serviceProviderId',
    'groupId',
    '3001',
    'extension',
    'auto_attendant'
)
```

## Credits

This package builds upon the excellent work of the original Broadworks OCI-P Interface package. Special thanks to:

[@nigelm (Nigel Metheringham)](https://github.com/nigelm/) – Developer of the original Python version.

Karol Skibiński – For extensive testing, bug reporting, and valuable contributions.

[@ewurch (Eduardo Würch)](https://github.com/ewurch) – For contributing the R25 schema update and other improvements.

Additionally, thank you to the Dev Team at Fourteen IP for the active manage and development of the tool.
