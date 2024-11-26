## Exercise 1: Generate and Log Security Tokens
from securityToken import *
log_token()

 ## Exercise 2: Analyze Token Logging Data 
'''
* **1.Log Analysis Module:** Create a Python module token_analysis.py that does the following:<br>

    * *Parse the Logs:* Implement a function parse_logs(file_name) that reads the token_logs.txt file generated by security_token.py. Each entry in the log file has a token and timestamp, separated by a comma. Parse the log file and store the data in a list of dictionaries.
        * Each dictionary should contain the token and timestamp.
    
    *  *Token Analysis:* <br>
         
        *    Find Duplicate Tokens: Write a function find_duplicates(tokens) that checks if any tokens have been used more than once. This could indicate an issue with token generation or a potential attack.
            
        * Find Tokens Older than 24 Hours: Write a function find_old_tokens(tokens) that finds any tokens in the log that are older than 24 hours (using the current date and time from datetime). This could help in identifying long-lived, potentially stale tokens.
    
    * *Generate a Report:* The function generate_report() should summarize the log file's findings:
        * How many tokens are older than 24 hours?
        
        * How many tokens are duplicates?
         
        * Return the result in a structured format: e.g., "Tokens older than 24 hours: X, Duplicate tokens: Y".
'''