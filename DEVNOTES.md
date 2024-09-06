# Development Notes
### Argparse Module
- -u/--url argument is limited to 6 inline URLs.<br>
  need to add some logic to enforce this?
  e.g., if input more than 6 URLs on the CLI,
  print argparse help/usage message.
  - COMPLETE: implemented using argparse custom action
- ICANN/IANA TLD: thinking about scrapping this 'class' in favor
  of just using normal HTTP GET and write-to-file functions.
- need to modularize the URL validation, URL request, and file writing portion of this


### URL Handling Module
- function to break URL into its constituent pieces <br>
  the function will return the pieces, the full URL, or nothing ?
    - scheme (http://)
    - domain name (www.example.com)
    - port (80/443)
    - path to file (/path/to/file)
    - parameters (?key1=value1&key2=value2)
    - anchor (#SomewhereInTheDocument)
- function arguments
    - URL


### URL Request Module
- function that performs the actual URL request
    - returns:
        - URL
        - data


### File Name Creation Module
- function to create output file name from the URL
    - function arguments
        - URL


### Write to File Module
- function to write URL data to file
- function arguments
    - output file name
    - encoding