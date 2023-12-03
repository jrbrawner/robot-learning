*** Settings ***
Documentation    Example test
Library          OperatingSystem
Library          REST    http://localhost:8000  
Library          TestingLibrary.py

*** Variables ***
${MESSAGE}     Hello, world!

*** Test Cases ***
My Test
    [Documentation]    Example test
    Log     ${MESSAGE}

Test PCAP Read
    [Documentation]    Test reading a pcap file
    Read Pcap

HTTP Request
    [Documentation]    Make an HTTP Request
    GET     /api/mitre/tactics/basic
    Output Schema     response body
