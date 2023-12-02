*** Settings ***
Documentation    Example test
Library          OperatingSystem
Library          TestingLibrary.py

*** Variables ***
${MESSAGE}     Hello, world!

*** Test Cases ***
My Test
    [Documentation]    Example test
    Log     ${MESSAGE}

Test PCAP Read
    [Documentation]    Test reading a pcap file
    Open
