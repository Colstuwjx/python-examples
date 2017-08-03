# coding=utf-8

'''
需求：

1、有一组国家+地区的时间服务器；
2、每台服务器需要根据自己所属的子网进行匹配，然后找到自己的组织；
3、将服务器上的ntp配置替换成对应所属时间服务器的ntp server

思路：

0、首先得到该台机器的IP Address；
1、判断该台服务器IP属于哪个地区的子网是一个需要实现的方法；
2、匹配得到所属的ntp server；
3、执行替换

实现：Python or Ansible
'''

from netaddr import IPAddress, IPNetwork
import jinja2


class NtpUpdater(object):
    def __init__(self):
        # TODO: 小菜比，你需要理一下子网归属，然后更新这个配置
        self.locations = [
            # TODO: NameTupple is better!
            ("China", "Taipei", "192.168.0.0/24"),
        ]
        # TODO: 小菜比，把这些换成对应的ntp服务器
        self.ntp_servers = {
            "China": ['china_ntp_servers_here',
                      'china_ntp_servers_here'],
            "Asia": ['asia_ntp_servers_here',
                     'asia_ntp_servers_here'],
            "Europe": ['europe_ntp_servers_here',
                       'europe_ntp_servers_here']
        }

    def __find_location(self, ip):
        ipaddr = IPAddress(ip)
        country = ""
        city = ""
        for loc in self.locations:
            if ipaddr in IPNetwork(loc[2]):
                country = loc[0]
                city = loc[1]
                return country, city

        # we can not find it...
        return country, city

    def __find_servers(self, ip):
        country, city = self.__find_location(ip)
        if all([country, city]) and country in self.ntp_servers:
            own_ntp_servers = self.ntp_servers[country]
            return own_ntp_servers
        else:
            raise Exception("IP {} is not belone to any country/city...".format(SERVER_IP))

    def __render_ntp_conf(self, ip, own_ntp_servers, render_file):
        templateLoader = jinja2.FileSystemLoader(searchpath="./")
        templateEnv = jinja2.Environment(loader=templateLoader)
        TEMPLATE_FILE = "sample_ntp_conf.j2"
        template = templateEnv.get_template(TEMPLATE_FILE)
        outputText = template.render(servers=own_ntp_servers)

        # write data into file.
        with open(render_file, 'w') as fp:
            fp.writelines(outputText)

    def generate_ntp_conf(self, ip, render_file="sample_ntp.conf"):
        own_ntp_servers = self.__find_servers(ip)
        self.__render_ntp_conf(ip, own_ntp_servers, render_file)


def main():
    SERVER_IP = "192.168.0.1"
    nu = NtpUpdater()
    nu.generate_ntp_conf(SERVER_IP)


if __name__ == "__main__":
    main()
