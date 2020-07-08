# entusergenerator.py 1.0.0
Enterprise usernames wordlist generator

## 1. Usage

```
usage: entusergenerator.py [-h] -i [I] [-s [S]] [-n] [-r] [-l] [-u] [-v]

Enterprise usernames wordlist generator

optional arguments:
  -h, --help  show this help message and exit
  -i [I]      input users file
  -s [S]      separators (default: .)
  -n          no changes
  -r          add reversed name and surname
  -l          everything to lowercase
  -u          everything to uppercase
  -v          show program's version number and exit
```

## 2. Example

```
entusergenerator.py -i users.txt -l > usernames.txt
```