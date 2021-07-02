"""
Snapd socket transport plugin for HTTPie.
"""
from httpie.plugins import TransportPlugin
from requests_unixsocket import UnixAdapter, DEFAULT_SCHEME
from requests.compat import urlparse, urlunparse, quote

__version__ = '1.0.0'
__author__ = 'Mickaël Schoentgen'
__licence__ = 'BSD'


class SnapdAdapter(UnixAdapter):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__unix_socket_prefix = urlparse(DEFAULT_SCHEME).scheme
        self.__snapd_socket_netloc = quote('/run/snapd.socket', safe='')

    def get_connection(self, url, proxies=None):
        """The given `url` needs to be adapted to something handled by the Unix socket.

        Original URL:
            snapd:///v2/find?name=httpie
        New URL:
            http+unix://%2Frun%2Fsnapd.socket/v2/find?name=httpie

        """
        # Do the transformation
        parsed_url = urlparse(url)
        parsed_url = parsed_url._replace(scheme=self.__unix_socket_prefix)
        parsed_url = parsed_url._replace(netloc=self.__snapd_socket_netloc)

        # Recompute the new URL
        url = urlunparse(parsed_url)

        return super().get_connection(url, proxies=proxies)


class SnapdSocketTransportPlugin(TransportPlugin):

    name = 'Snapd REST API transport'
    prefix = 'snapd://'

    def get_adapter(self):
        return SnapdAdapter()
