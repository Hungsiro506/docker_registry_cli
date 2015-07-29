# docker_registry_cli
[![](https://badge.imagelayers.io/so0k/registry-cli:alpine.svg)](https://imagelayers.io/?images=so0k/registry-cli:alpine 'badge by imagelayers.io')

Docker Registry CLI - Currently ONLY Supports the Search capability via Catalog API in the new version of Docker Registry v2. 

To use, run the latest Docker Registry Distribution (distribution master):

**docker-compose.yml**

```yaml
endpoint:
   image: distribution/registry:master
   restart: always
   environment:
    - REGISTRY_STORAGE_FILESYSTEM_ROOTDIRECTORY=/var/lib/registry
   ports:
    - 5000
   volumes:
    - /var/lib/registry/:var/lib/registry/
```

`docker-compose up -p registry -d`


The CLI uses the Catalog API available through /v2/_catalog in the new development version of Docker Registry.

## Usage:

`docker run --rm so0k/registry-cli:alpine <REGISTRY_ENDPOINT> <keyword> <options>`

*   REGISTRY_ENDPOINT : `<REGISTRY_HOST>:<REGISTRY_PORT>`

    example with link to a local registry container launched by `docker-compose` command above:

    `docker run --rm --link registry_endpoint_1:registry so0k/registry-cli:alpine registry:5000 <keyword> <options>`

* KEYWORD :

    * *search* - allows searching for Docker Images. Supports partial search. No RegEx Support yet. 

      eg:-

      `python browser.py 192.168.59.103:5000 search busybox`

      `python browser.py 192.168.59.103:5000 search busy`

      `python browser.py 192.168.59.103:5000 search bu`

      `python browser.py 192.168.59.103:5000 search jenkins`


    * *list* - lists all the Docker images available in the Image Registry with their respective tags 

      eg:- 

      `python browser.py 192.168.59.103:5000 list all`
