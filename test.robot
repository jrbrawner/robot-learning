*** Settings ***
Documentation    Example test
Library          OperatingSystem
Library          test_lib.TestingLibrary

*** Variables ***
${MESSAGE}     Hello, world!

*** Test Cases ***
My Test
    [Documentation]    Example test
    Log     ${MESSAGE}

Test Library
    [Documentation]    Test importing a Library
    Print Hello         
