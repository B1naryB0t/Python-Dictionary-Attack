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
The text file in the repo is from weakpass.com. It contains 1.6 million most common passwords. It was chosen because it is a fairly exhaustive list while still returning a result in no less than 45 seconds. When this program was tested with a 304,000 password list, the result was returned within 5 seconds. CPU processing power is the limiting factor on speed. Asyncio module is most responsible for the speed. Prior implementations without asyncio module took 3 hours to run this script with only 304,000 passwords.

## How to Use
Download both the python script and the password file, or use your own password file to test against. If using your own password file, update the filename in the code to your own. Make sure the script and the file are in the same directory as well. Then, simply run the program. It will ask you for a password that you want it to try to guess against those in the password file.
