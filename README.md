# Python Dictionary Attack
A simple python script that asks for a password and compares it to a list of the most common passwords

## Introduction
This is a Python script I made for educational purposes in class. It executes a dictionary attack using a dictionary of known, common passwords. Because it is a proof-of-concept, it asks the user to input the correct password, hashes the correct password, then goes through the text file and hashes each password to compare to the correct hash.

## Disclaimer
This is for educational purposes. Using this tool to gain unauthorized access is illegal. Do not use this script for any malicious purposes.

## Scope
This is an educational proof-of-concept. In a real cracking situation, the correct hash is what would be known, so the correct password input step would be omitted.

The best thing a hacker can hack is time. For an automated process, this could be tied into another script to read a table of stolen hashed credentials, and I would recommend a smaller password list for the first run over the data.

## Functionality
The text file in the repo is from weakpass.com. It contains 1.6 million most common passwords. It was chosen because it is a fairly exhaustive list while still returning a result in no less than 45 seconds. When this program was tested with a 304,000 password list, the result was returned within 5 seconds. This script will whip your CPU into shape, meaning that CPU processing power is the limiting factor on speed. Asyncio module is most responsible for the speed. Prior implementations without asyncio module took 3 hours for the same list of 304,000 passwords.

