import sys
import unittest

sys.path.append('../src/')
sys.path.append('src/')
import envparser

class TestEnvParser(unittest.TestCase):
  def test_envparser_env_parser_single_parse(self):
    inp_string = 'this is a test string, with name {{ main.name }}'
    self.assertEqual(envparser.env_parser(inp_string), 'this is a test string, with name this')

  def test_envparser_env_parser_multiple_parse(self):
    inp_string = 'this is a test string, with name {{ main.name }} {{main.name}}'
    self.assertEqual(envparser.env_parser(inp_string), 'this is a test string, with name this this')

if __name__ == '__main__':
  unittest.main()
