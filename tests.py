from unittest import TestCase

from httpie.client import build_requests_session
from httpie.plugins.registry import plugin_manager
from httpie_snapdsocket import SnapdSocketTransportPlugin


class TestSnapdSocketTransportPlugin(TestCase):

    def test_simple(self):
        # Package containing unicode characters
        package = 'open-syobon-action'

        plugin_manager.register(SnapdSocketTransportPlugin)
        try:
            session = build_requests_session(True)
            res = session.get('snapd:///v2/find?name=' + package).json()
            self.assertTrue(isinstance(res, dict))
            self.assertEqual(res['result'][0]['name'], package)
        finally:
            plugin_manager.unregister(SnapdSocketTransportPlugin)
