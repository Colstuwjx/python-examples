# coding=utf-8

import unittest
import retrying
import mock
import requests
import json


class RequestError(Exception):
    def __init__(self, server):
        self.message = "Request failed to {}.".format(server)


class Blog(object):
    '''
    Blog类包含一些博客文章相关的操作封装
    类在初始化后，post方法提供对指定文章链接内容的获取并返回JSON的格式
    '''
    def __init__(self, name):
        self.name = name

    @retrying.retry(stop_max_attempt_number=3, wait_fixed=100)
    def post(self, article_path):
        '''
        根据获取文章的内容
        '''
        response = requests.get("http://{name}/{path}".format(
            name=self.name,
            path=article_path))
        if response.status_code >= 200 and response.status_code < 300:
            return response.text
        else:
            raise RequestError(self.name)

    def __repr__(self):
        return '<Blog: {}>'.format(self.name)


class TestBlog(unittest.TestCase):
    '''
    我们需要测试哪些内容？根据K大的http://docs.python-guide.org/en/latest/writing/tests/
    我们关注本身的功能的覆盖，那么主要需要测试：
    1. 正常请求时是否能获得正确的JSON数据
    2. 异常返回时是否抛出RequestError异常
    3. 遇到错误是否会重试
    '''
    @mock.patch('requests.get')
    def test_blog_post(self, mock_get):
        mocked_content = json.dumps({
            'status': True, 'content': 'This is the post content'
        })
        mocked_success = mock.MagicMock(
                status_code=200,
                headers={'content-type': "application/json"},
                text=mocked_content)
        mock_get.return_value = mocked_success

        # new blog instance and call `post`.
        # confirm return value on succcess.
        b = Blog(name="devopstarter.info")
        content = b.post("three-years-later-test-mock")
        self.assertEqual(content, mocked_content)

        mock_get.reset_mock()  # reset mock, include called count etc.
        mocked_error = mock.MagicMock(
                status_code=500,
                headers={'content-type': "application/json"},
                text="Internal server error")
        # confirm raise exception on failure.
        # due to mock object return_value is always error, retry is also error.
        mock_get.return_value = mocked_error
        with self.assertRaises(RequestError):
            b.post("three-years-later-test-mock")
        # confirm the retry works in failure case, call_count exceeded 3!
        self.assertEqual(mock_get.call_count, 3)

        # confirm the retry works while ONLY one time failed.
        # `side_effect` helped us complete this goal!
        mock_get.reset_mock()  # reset mock, include called count etc.
        mock_get.side_effect = [
            requests.ConnectionError('Test error'),
            mocked_success
        ]
        content = b.post("three-years-later-test-mock")
        self.assertEqual(content, mocked_content)


if __name__ == '__main__':
    unittest.main()
