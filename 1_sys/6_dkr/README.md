## docker 

+ [docker](https://docker.com)
  + [reference](https://docs.docker.com/engine/reference/builder/)
  + [python](https://docs.docker.com/language/python/)
+ [engine](https://docs.docker.com/engine/)
+ [docker compose](https://docs.docker.com/compose/)


useful images

+ [redis](https://hub.docker.com/_/redis/) REmote Dictionary server
  start instance
  ```shell
  docker run --name some-redis -d redis
  ```
  start with persistent storage
  ```shell
  docker run --name some-redis -d redis redis-server --save 60 1 --loglevel warning
  ```
+ [python](https://hub.docker.com/_/python)
  + [3.7.13] 

examples

+ [offline-python-deploy](https://realpython.com/offline-python-deployments-with-docker/)
+ [wxPython build docker](https://github.com/foxguardsolutions/wxpython/blob/master/Dockerfile)
