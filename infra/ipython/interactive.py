# coding=utf-8

import cmd

addresses = [
    'here@blubb.com',
    'foo@bar.com',
    'whatever@wherever.org',
]


class MyCmd(cmd.Cmd):
    def do_send(self, line):
        pass

    def complete_send(self, text, line, start_index, end_index):
        if text:
            return [
                address for address in addresses
                if address.startswith(text)
            ]
        else:
            return addresses


if __name__ == '__main__':
    # FIX: mac os x doesn't include real readline implementation.
    # fix here for compatible.
    import rlcompleter
    import readline
    readline.parse_and_bind("bind ^I rl_complete")

    my_cmd = MyCmd()
    my_cmd.cmdloop()
