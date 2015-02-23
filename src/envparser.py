import ConfigParser

def read_config_variables(config_file, section_name):
  var_dict = {}

  config = ConfigParser.ConfigParser()
  config.read(config_file)

  for key, value in config.items(section_name):
    var_dict[key] = value

  return var_dict

# TODO this method assumes all inputs adher to the split. Fix this.
def double_bracket_state_machine(var_dict, input_string):
  parsed_input = []
  i = 0
  while i < len(input_string):
    if input_string[i] != '{':
      parsed_input.append(input_string[i])
      i += 1
    else:
      i += 2
      while input_string[i] == ' ':
        i += 1
      var_key = []
      while input_string[i] != ' ' and input_string[i] != '}':
        var_key.append(input_string[i])
        i += 1
      if input_string[i] == '}':
        i += 2
      else:
        while input_string[i] != ' ':
          i += 1
        while input_string[i] != '}':
          i += 1
        i += 2
      key_str = ''.join(var_key)
      if key_str in var_dict:
        parsed_input.append(var_dict[key_str])
      else:
        parsed_input.append('{{key not found: ' + key_str + '}}')

  return ''.join(parsed_input)

def env_parser(input_string):
  var_dict = read_config_variables('/Users/omega9/test/static/config/main.config', 'main')
  return double_bracket_state_machine(var_dict, input_string)
