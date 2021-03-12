[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
# ***SSH_Bruter***

![](https://github.com/reveng007/SSH_Bruter/blob/main/images/banner.png)

## So, What are the functionalities it can provide ?

It has 3 modes till now:

1. Bruteforce ssh password alone
2. Bruteforce ssh username alone
3. Bruteforce ssh credials (both)

## To test this script:
Clone the repository:
```
$ git clone https://github.com/reveng007/SSH_Bruter.git
```
Install the required python dependencies:
```
$ pip install -r requirement.txt
```
## To run:
### Simply write

```
$ cd scripts
$ python3 ssh_bruter -h
```
![](https://github.com/reveng007/SSH_Bruter/blob/main/images/image1.png)

## For brute forcing username only:
```
$ python3 ssh_bruter -ip <ip> -u_file <username wordlist> -p <password>
```
## For brute forcing password only:
```
$ python3 ssh_bruter -ip <ip> -u <username> -p_file <password wordlist>
```
## For brute forcing both creds:
```
$ python3 ssh_bruter -ip <ip> -u_file <username wordlist> -p_file <password wordlist>
```
## Let's see one of the modes in action:

#### Credentials:

#### username: msfadmin
#### password: msfadmin

![Alt Text](https://github.com/reveng007/SSH_Bruter/blob/main/ssh_brute.gif)

