Minimalist micro service web stack in python
remove .env from production and use proper environment variables for storing password

# REDIS
add  'vm.overcommit_memory = 1' to /etc/sysctl.conf 
and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.