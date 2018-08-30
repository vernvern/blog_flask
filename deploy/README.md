# ansible

## init

- 本地安装ansible

- 服务器安装openssh-server，开启服务

- 服务器添加ssh key(本地执行 `sh-copy-id user@192.168.0.0.1`)

## 使用

本地: ansible-playbook deploy.yml -e mode=local -e code_tag=master

生产环境: ansible-playbook deploy.yml -e mode=production -e code_tag=master

## 参数


- **mode** - 选择服务器
    - local - 本地服务器
    - develop - 测试服务器
    - production - 生产环境服务器
