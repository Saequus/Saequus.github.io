# spetsyian.github.io

Version: 20210517

## Instalation

~~~
bundle install
~~~

### Dev

~~~ bash
npm install sass
~~~

### Production

~~~ bash
get install ruby-dev
get install gcc
get install libffi-dev
get install make
sudo apt-get install build-essential g++

bundle install
~~~

## Running

SASS
~~~ bash
cd sass
sass --watch minima/minima.scss:minima.css
~~~

Rebuild sources and start server
~~~
bundle exec jekyll serve
~~~

Starts on http://127.0.0.1:4000


## Known issues

~~~
# to fix ffi error

export LDFLAGS="-L/usr/local/opt/libffi/lib" && \
export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig" && \
bundle --path vendor/bundle
~~~


