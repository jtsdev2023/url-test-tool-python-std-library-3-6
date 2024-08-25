# Development Notes
### Argparse Module
- -u/--url argument is limited to 6 inline URLs.<br>
  need to add some logic to enforce this?
  e.g., if input more than 6 URLs on the CLI,
  print argparse help/usage message.
  - COMPLETE: implemented using argparse custom action
- ICANN/IANA TLD: thinking about scrapping this 'class' in favor
  of just using normal HTTP GET and write-to-file functions.

