import ConfigParser

# TODO handle ConfigParser exceptions.
class EnvContext:
  def __init__(self, config_file=None):
    if config_file == None:
      self.config = {}
    else:
      self.config = ConfigParser.ConfigParser()
      self.config.read(config_file)

  def read_section_param(self, section_name, param_name):
    try:
      return self.config.get(section_name, param_name, 1)
    except ConfigParser.NoOptionError as e:
      return 'key not found: ' + param_name
