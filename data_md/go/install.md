## Instalacion:
    - https://go.dev/
    - Remove any previous Go installation by deleting the /usr/local/go folder (if it exists)
    - Then extract the archive you just downloaded into /usr/local, creating a fresh Go tree in /usr/local/go:
        - tar: go: Cannot mkdir: Permission denied
        - sudo  rm -rf /usr/local/go && tar -C /usr/local -xzf go1.22.1.linux-amd64.tar.gz
            - it looks like you're trying to untar go into some directory 
            that you don't have permissions to write into, /usr/local 
            and hence this step has failed completely
        - Could you please run your job under the user with appropriate permissions:
            - sudo chown -R root:root /usr/local/go

##  Permisos:
    - cd /usr/local
    - sudo mkdir go
        drwxr-xr-x 11 root root 4096 mar 10 16:04 ./
        drwxr-xr-x 14 root root 4096 oct 12  2021 ../
        drwxr-xr-x  2 root root 4096 dic  7  2021 bin/
        drwxr-xr-x  2 root root 4096 oct 12  2021 etc/
        drwxr-xr-x  2 root root 4096 oct 12  2021 games/
        drwxr-xr-x  2 root root 4096 mar 10 16:04 go/
        drwxr-xr-x  2 root root 4096 oct 12  2021 include/
        drwxr-xr-x  4 root root 4096 abr 20  2023 lib/
        lrwxrwxrwx  1 root root    9 dic  6  2021 man -> share/man/
        drwxr-xr-x  2 root root 4096 oct 12  2021 sbin/
        drwxr-xr-x  8 root root 4096 abr 20  2023 share/
        drwxr-xr-x  2 root root 4096 oct 12  2021 src/
    - pwd
    /home/gato/Downloads
    - sudo tar -C /usr/local -xzf go1.22.1.linux-amd64.tar.gz
    - cd /usr/local/go
    - La instalacion esta ahi

## Add /usr/local/go/bin to the PATH environment variable:
    - nvim .profile
    - export PATH=$PATH:/usr/local/go/bin

## version:
    - go version
    go version go1.22.1 linux/amd64
    
    
    

