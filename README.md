# ***Insecure_Shell***
![made-with-Python](https://shields.io/badge/Made_With-Python-green?logo=Linux&style=for-the-badge) ![made-with-bash](https://shields.io/badge/Made_With-Bash-green?logo=Linux&style=for-the-badge)


![](https://github.com/reveng007/Insecure_shell/blob/main/images/banner.png)


## Requirement:
```
$ pip install requirement.txt
```

## So, What are the functionalities it can provide ?

It has 3 modes till now:

1. Bruteforce ssh password alone
2. Bruteforce ssh username alone
3. Bruteforce ssh credials (both)


## For Installation Setup:
```
$ cd Insecure_shell/scripts/
$ chmod 744 setup.sh
$ ./setup.sh
```
## To run:
### Simply write:
```
$ insecure_shell.py -h
```
### Then we will be prompted with some options

![](https://github.com/reveng007/Insecure_shell/blob/main/images/image1.png)

### If we want to bruteforce for password:

![](https://github.com/reveng007/Insecure_shell/blob/main/images/image2.png)

### If we want to bruteforce for username:

![](https://github.com/reveng007/Insecure_shell/blob/main/images/image3.png)

### If we want to bruteforce both creds:

![](https://github.com/reveng007/Insecure_shell/blob/main/images/image4.png)

#### The whole summary can be seen with option 4


## Let's see one of the script in action:

#### Credentials:

#### username: msfadmin
#### password: msfadmin

![Alt Text](https://github.com/reveng007/Insecure_shell/blob/main/insecure_ssh.gif)

## In Case you didn't like it:
```
$ bash uninstall.sh
```
## To Do list:

- Adding another script to hunt down ports on which ssh service is running
- Adding default ssh password manipulating feature
- Adding multithreading
- Enabling sudo feature 

