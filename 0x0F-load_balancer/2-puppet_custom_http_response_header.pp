# Configures Nginx with custom header using Puppet

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update system'],
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}

exec { 'add custom header':
  command => 'sed -i "/server_name _;/a \\\tadd_header X-Served-By \\"$HOSTNAME\\";" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Package['nginx'], Exec['add custom header']],
}