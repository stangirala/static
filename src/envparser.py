import context

# TODO this method assumes all inputs adher to the split. Fix this.
def double_bracket_state_machine(context_object, input_string):
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

      #TODO handle bad string.
      section, param_name = (''.join(var_key)).split('.')
      parsed_input.append(context_object.read_section_param(section, param_name))

  return ''.join(parsed_input)

def env_parser(input_string):
  environment_context = context.EnvContext('config/main.config')
  return double_bracket_state_machine(environment_context, input_string)
