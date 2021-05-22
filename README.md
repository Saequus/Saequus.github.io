# spetsyian.github.io
v2020

## Instalation

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
sass --watch main.scss:main.css

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

