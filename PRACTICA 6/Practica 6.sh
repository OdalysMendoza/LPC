#!/bin/bash

ifconfig

#ip 192.168.0.13

nmap -sP 192.168.0.13/24 | base64
nmap 192.168.0.13/24 | base64
