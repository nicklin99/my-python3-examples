from io import StringIO
from fabric import Connection
import paramiko


def newConnWithPrivateKey(host, user, privateKey):
    """
        host
        user
        privateKey
        '''\
        privateKey string
        '''
    """
    pkey = paramiko.RSAKey.from_private_key(StringIO(privateKey))
    conn = Connection(host, user, connect_kwargs={
        "pkey": pkey,
    },)
    return conn
