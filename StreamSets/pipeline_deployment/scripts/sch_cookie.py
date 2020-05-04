import requests


class sch_cookie():

    def __init__(self):
        pass

    def build_cookie_headers(self):
        headers = {
            'Content-Type': 'application/json',
            'X-Requested-By': 'SCH',
        }
        return headers

    def build_cookie_data(self, username, password):
        data = '{"userName": "%s", "password": "%s"}' % (username, password)
        return data

    def get_cookies(self, cookie_jar, url):
        domain = url.split('//', 1)[1]
        cookie_dict = cookie_jar.get_dict(domain=domain)
        found = ['%s=%s' % (name, value) for (name, value) in cookie_dict.items()]
        return ';'.join(found)

    def get_cookie(self, url, port, username, password):
        url_with_port = url if (port is "") else (url + ":" + port)
        request_url = url_with_port + '/security/public-rest/v1/authentication/login'
        print(request_url)
        headers = self.build_cookie_headers()
        data = self.build_cookie_data(username, password)

        response = requests.post(request_url, headers=headers, data=data)
        print("response.cookies")
        print(response.cookies)
        cookie = self.get_cookies(response.cookies, url)[13:]
        return cookie
