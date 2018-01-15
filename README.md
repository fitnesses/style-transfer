# style-transfer
1. 修改start.sh中，APP_CONFIG_FILE配置
2. 安装fatory
    
    ```bash
    docker pull contribsys/faktory
    mkdir faktory-data
    cd faktory-data
    docker run -d -it -v $PWD:/var/lib/faktory -p 127.0.0.1:7419:7419 -p 127.0.0.1:7420:7420 contribsys/faktory:latest /faktory -b 0.0.0.0:7419
    ```
3. flask web端接受请求，faktory worker负责处理任务

