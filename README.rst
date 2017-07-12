================
slick-bitcoinrpc
================

Just another Python bitcoin-rpc client.
Built as faster alternative to python-bitcoinlib rpc (https://github.com/petertodd/python-bitcoinlib) and python-bitcoinrpc (https://github.com/jgarzik/python-bitcoinrpc) using pycurl and ujson.

Installation
============

    pip install slick-bitcoinrpc

Example
=======
.. code:: python

    from slickrpc import Proxy

    bitcoin = Proxy("http://%s:%s@127.0.0.1:8332"%(rpcuser, rpcpassword))
    print(bitcoin.getblock(bitcoin.getbestblockhash()))
