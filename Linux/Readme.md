All commands performed on terminal
# Broker (MQTT server)

Installation command: $ sudo apt install -y mosquitto

## Setting up
Defaul configuration **only** allows local connection, publishers and subscriber within the same computer.

### To allow remote anonyomus conections
create a new configuration file and save it to /etc/mosquitto/conf.d with '.conf' extension

File content: 

listener \<port\>[^1]

allow_anonymous True

### Allow firewall to receive connection in \<port\>
sudo ufw allow \<port\>[^1]

## Initializing broker
mosquitto -c /etc/mosquitto/conf.d/\<file_name\>.conf

This will result in the following image, meaning that the broker (MQTT server) is up and running
![image](https://user-images.githubusercontent.com/48689965/197541122-81813f3d-8ac7-44b1-abe3-5dcafce5fe37.png)

# Client

Installation Command: $ sudo apt install -y mosquitto-clients

[^1]: port is an integer between 0-65535
