*** Settings ***
Library                ../SSH_library/TestSSH.py
Suite Setup            Custom Setup
Suite Teardown         Custom Teardown

*** Variables ***
${HOST}                127.0.0.1
${USERNAME}            waseem
${PASSWORD}            123123


*** Keywords ***
Custom Setup
    login_to_host  ${HOST}  port=2222  username=${USERNAME}  password=${PASSWORD}

Custom TearDown
    Logout From Host
