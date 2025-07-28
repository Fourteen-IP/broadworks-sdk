[chronicl](https://github.com/minimal-mind/chronicl)

## CODEBASE OVERVIEW
- Thor's Hammer is a Python library for interacting with BroadWorks servers.
- It is designed to be a simple and easy to use library for interacting with BroadWorks servers.
- It introduces command classes for each BroadWorks command, and a client class for interacting with the server.
- It has a command dispatch table for each client, and a requester class for sending requests to the server.
- It allows users to decide whether to use synchronous or asynchronous clients.
- It allows users to decide whether to use TCP or SOAP connections.

## TECH STACK
- Entirely Python 3.10+
- Uses attrs for object instantiation and validation
- Uses httpx for HTTP requests
- Uses logging for logging
- Uses pytest for testing

## CONTRIBUTORS
- @Jordan-Prescott
- @KiPageFault
- @malkin0xb8

## DESIGN DECISIONS
- Command classes are used to represent BroadWorks commands.
- Client classes are used to represent connections to BroadWorks servers.
- Requester classes are used to send requests to BroadWorks servers.
- The dispatch table is used to map command names to command classes.
- In the command classes we will maintain latest version of command but allow the user to specify the version of the command they want to use.
- Definition of a feature that will be added to agent must meet the following criteria:
    - Needs to take more than ten mins 
	- A task that can be done in bulk 
	- Needs at least 3 steps to complete 
	- Needs at least 5 people to request it
	- Frequency is at least 4 times a month 
- Response classes will have to_dict, to_csv, etc to allow the user to export the data in a variety of formats.
- Agent scripts will be classes and those that are purely informational will have to_file() to allow the user to export the data in a variety of formats.

## RISKS
- The library is not yet tested, and may not work as expected.
- The library is not yet documented, and may not be easy to use.
- The library is not yet production-ready, and may not be stable.

## OPEN ENDED
- How the client receives responses from the server needs flushing out

## NEXT STEPS
- Add tests for classes
- Add documentation to the library

## NOTES

## JOURNAL
@malkin0xb8 25.07.2025
- Discovered that the password signing is incorrect, after testing with raw password the login succeeded.
- Online suggestions say that since the socket and connection is SSL encrypted the OCI backend expects a different charset or format for the signed password.

@Jordan-Prescott 22.07.2025
- Added absolute import statements as this is a python package its best practuice 
- Imports should follow order: standard packages, internal packages, external packages at the bottom

@Jordan-Prescott 15.07.2025
- Added tests for the client class found in tests/client_tests.py
- Adjusted the _receive_response in client which will use the response object from requester to capture class to return

@Jordan-Prescott 14.07.2025
- Client class now first draft with most of the functionality in place, yet some things still need flushing out.
- Both client and AsycClient done
- Added exceptions for the library in exceptions.py
- Decided to add _receive_response to the client class to handle the response from the server. How this is done needs flushing out.
- Still need to add tests to the library which will start with the client class. 
- Still need to add documentation to the library.

@KiPageFault 22.07.2025
- Added Parser class designed for Type/Request/Response type translation between class objects, xml, and dictionaries.
- Added OCI base classes to encapsulate Type/Request/Response objects and provide parser utility.
- Finalised Client _receive_response in accordance with Requester object. It is designed to take a raw string on a successful response or \
  a tuple object containing an exception object and message.
- All above implementations require documentaiton.

