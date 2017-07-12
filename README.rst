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


Performance Comparison
======================

Method
------
Here's bash script able to measure performance of such bitcoin rpc clients

.. code:: bash
   
    RPC_URL='http://username:password@127.0.0.1:8332'
    TASKS=(
      "p.getinfo()"
      "p.getblock(p.getbestblockhash())"
      "map(lambda tx: p.getrawtransaction(tx['txid'], 1), p.listtransactions())"
    )
    SETUPS=(
      "from slickrpc import Proxy; p = Proxy(service_url='$RPC_URL');"
      "from bitcoinrpc.authproxy import AuthServiceProxy; p = AuthServiceProxy(service_url='$RPC_URL');"
      "from bitcoin.rpc import Proxy; p = Proxy(service_url='$RPC_URL');"
    )
    for TASK in "${TASKS[@]}"
    do
      for SETUP in "${SETUPS[@]}"
      do
        python -m timeit -s "$SETUP" -n 1000 "$TASK"
      done
    done


Results
-------

Values are best of 3, msec per loop


+------------+-----------+----------------------------------+--------------------------------------+
|            | getinfo() | p.getblock(p.getbestblockhash()) | map(lambda tx: p.getrawtransaction(  |
|            |           |                                  | tx['txid'], 1), p.listtransactions() |
+============+===========+==================================+======================================+
| slick-     | 1.01 msec | 1.17 msec                        | 27.7 msec                            |
| bitcoinrpc |           |                                  |                                      |
+------------+-----------+----------------------------------+--------------------------------------+
| python-    | 2.53 msec | 3.89 msec                        | 41.9 msec                            |
| bitcoinrpc |           |                                  |                                      |
+------------+-----------+----------------------------------+--------------------------------------+
| python-    | 2.76 msec | DeserializationExtraDataError    | AttributeError                       |
| bitcoinlib |           |                                  |                                      |
+------------+-----------+----------------------------------+--------------------------------------+
