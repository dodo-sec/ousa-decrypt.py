```
  ___  _   _ ____    _      ____  _____ ____ ______   ______ _____ 
 / _ \| | | / ___|  / \    |  _ \| ____/ ___|  _ \ \ / /  _ \_   _|
| | | | | | \___ \ / _ \   | | | |  _|| |   | |_) \ V /| |_) || |  
| |_| | |_| |___) / ___ \  | |_| | |__| |___|  _ < | | |  __/ | |  
 \___/ \___/|____/_/   \_\ |____/|_____\____|_| \_\|_| |_|    |_|  
```

created by [dodo_sec](https://twitter.com/dodo_sec)

# ousa-decrypt
This is a simple program that implements the decryption routine for zip payloads used by the Ousaban/Javali malware family.

Please keep in mind this is meant to decrypt the zip archive only - **it does not decrypt content from the malware itself.**

# python version
This version gave birth to its C counterpart, available [here](https://github.com/dodo-sec/ousa-decrypt). 

Unlike the C version, this takes no arguments and is supposed to be ran in a python notebook. 

Either rename your encrypted payload to `ciphered.zip` or edit the code to match the filename of the input file.
