*** Settings ***
Library                ../SSH_library/TestSSH.py
Resource               ../Resource/variables1.robot

*** Test Cases ***
Check Hostname
    ${HOSTNAME}=     Get Hostname
    Log              ${HOSTNAME}
    Should Be Equal  ${HOSTNAME}  waseem-ahmad

Check Network
    ${NETWORK}=      Get Network Configurations
    Log              ${NETWORK}
    Should Contain   ${NETWORK}  ${NET1}
    Should Contain   ${NETWORK}  ${NET2}
    Should Contain   ${NETWORK}  ${NET3}

Make Directory
    Create Directory    directory3
    ${RESULT}           DIRECTORY SHOULD EXIST  directory3
    Should Be Equal As Integers   ${RESULT}  1

Make File
    Create File        file12.txt   my name is waseem   .
    File Should Exist  file12.txt

Put File
    Put File        ./file123.txt   file123.txt
    File Should Exist  file123.txt

Get File
    Get File        file11.txt   ./file13.txt

Remove File From Virtual
    Create File        file2.txt   my name is waseem   dir1
    ${NUM_OF_FILES_BEFORE}   Get Count Of Files  dir1
    Remove File      dir1/file2.txt
    ${NUM_OF_FILES_AFTER}   Get Count Of Files  dir1
    Evaluate  ${NUM_OF_FILES_AFTER} < ${NUM_OF_FILES_BEFORE}

Empty Directory
    Create File        file1.txt   my name is waseem   directory1
    Create File        file2.txt   my name is waseem   directory1
    Remove Files In Directory   directory1
    ${NUM_OF_FILES}    Get Count Of Files  directory1
    Should Be Equal As Integers  ${NUM_OF_FILES}  0
