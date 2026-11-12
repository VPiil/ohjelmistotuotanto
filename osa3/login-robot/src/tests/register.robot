*** Settings ***
Resource  resource.robot
Test setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallee  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Username should be atleast 3 character long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle!  kalle123
    Output Should Contain  Username long enough but invalid characters

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle1
    Output Should Contain  Username valid but password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Username valid but password contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command