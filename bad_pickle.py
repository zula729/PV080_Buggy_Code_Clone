# contains bunch of buggy examples
# taken from:
# https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
from cPickle import dumps
from subprocess import call, Popen
from base64 import b64encode


# Input injection
def transcode_file(filename):
    """
    Transcodes a file
    :param filename: file to transcode
    :return: None
    """
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    call(command, shell=True)  # a bad idea!


# Assert statements
def assert_statements(user):
    """
    Runs assert statements
    :param user: User to assert
    :return: None
    """
    assert user.is_admin, 'user does not have access'
    # secure code...


# Pickles
class RunBinSh(object):
    """
    Runs reduce
    """

    def __reduce__(self):
        return Popen('/bin/sh')


print(b64encode(dumps(RunBinSh())))
