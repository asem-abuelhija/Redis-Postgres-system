# Asem Abuelhija
## _A Simple Redis + Postgres system, automated provisioning_


This project is an Ansible project that provisions an Ubuntu VM using vagrant and virtualbox, and builds a postgresql database, a message broker using Redis, and a simpl service that moves data from the message broker to the database.

## Prerequisites

The project should be run on an Ubuntu machine with the below packages installed

- Make sure Ansible is installed and operational
```sh
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible

ansible --version
```

- build a project directory or clone this project.
- all required configurations are done, no need to edit anything.

- run the first playbook to install prerequisites on the loacalhost and create the project VM.
```sh
ansible-playbook environment_provisioning.yml
```

The above playbook will create a new ubuntu VM using vagrant and virtualbox, and creates the ansible inventory we will be using.
As part of the vagrant process, a provisioning playbook runs, I stuck with a ping playbook so we can inspect and run our playbooks manually.

- now run the remaining three playbooks to deploy the project on the newly created machine.
```sh
ansible-playbook playbook_install_postgres
ansible-playbook playbook_install_redis
ansible-playbook service
```
>The first playbook will install and configure the postgresql database, as well as create the superuser and the needed table.
>The second playbook will prepare Redis for receiving messages.
>The third playbook will create a systemd service from our custom python code, which will keep running in the background moving any new messages from redis to postgres, I named the service rtpg (Redis to Postgresql). it will also copy a script that helps us monitor the database, the queue, and the service.

You can then ssh to the machine to check the project using the watch.sh script 

```sh
./watch.sh
```
or
```sh
watch ./watch.sh        #for an interactive screen
```


- to populate the queue, you can use the provided enqueue_redis.sh script or manually through the redis cli
> the entry should be in the following format `"channel:jawaker" "{\"username\":\"tarneeb\"}"`