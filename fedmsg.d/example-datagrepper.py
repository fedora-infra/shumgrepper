config = {
    # This is just a key to tell the fedmsg-hub to initialize us.
    'summershum.enabled': True,
    'summershum.sqlalchemy.url': 'sqlite:////var/tmp/summershum.sqlite',
    'summershum.lookaside': 'http://pkgs.fedoraproject.org/lookaside/pkgs/',
    'summershum.datagrepper': 'https://apps.fedoraproject.org/datagrepper/',
}
