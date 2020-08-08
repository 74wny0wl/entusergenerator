# entusergenerator.py 1.0.1
Enterprise usernames wordlist generator

## 1. Usage

```
usage: entusergenerator.py [-h] -i [I] [-s [S]] [-r] [-l] [-u] [-v]

Enterprise usernames wordlist generator

optional arguments:
  -h, --help  show this help message and exit
  -i [I]      input users file
  -s [S]      separators (default: .-_)
  -r          add reversed name and surname
  -l          everything to lowercase
  -u          everything to uppercase
  -v          show program's version number and exit
```

## 2. Example

Input file users.txt:

```
Hugo Bear
```

and command:

```
entusergenerator.py -i users.txt -l > usernames.txt
```

generates file usernames.txt:

```
hugobea
hu-bear
hugo-bear
hug.bear
hugo.b
hu_bear
hugbear
h-bear
hugo_be
hugo
hugo.bear
hugo-b
h_bear
hug-bear
hubear
hbear
hugobear
hugobe
hugo.bea
hugo_bea
hug_bear
hugo-bea
hugo.be
bear
hugo-be
h.bear
hugo_bear
hugo_b
hu.bear
hugob
```