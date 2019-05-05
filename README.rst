=================================
Mastodon both using Plaground bot
=================================


Step 1
------

create cred.ini with the following content

.. code-block:: ini

    [config]
    access_token = mastodon_access_token
    url = https://mastodon_server_url

Step 2
------

Connect Circuit playground express port with usb data cable (Important!) then Upload micropython_code.py with mu-editor


Get it to run so the serial connection outputs the list of temperatures.

For on linux try

.. code-block:: bash

    $ cat /dev/ttyASM0

To debug the connection. Successful output will print out a column of temperature values.


Step 3
------

Install mastodon.py

.. code-block:: bash

    $ pip install Mastodon.py


then run mastodon_connect.py