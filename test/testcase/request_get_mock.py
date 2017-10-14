# coding=utf-8

import mock
import requests
import json
import unittest


def get_request():
    req = requests.get("http://www.baidu.com")
    # do sth...
    return req.status_code == 200


class TestClient(unittest.TestCase):
    @mock.patch('requests.get')
    def test_get_request(self, mock_request):
        mock_request.return_value = mock.MagicMock(
            status_code=200, response=json.dumps({'key': 'value'})
        )
        self.assertEqual(get_request(), True)


if __name__ == '__main__':
    unittest.main()
