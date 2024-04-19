# Script that increase Nginx traffic

# Changes ULIMIT variable from default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Nginx is restarted
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

