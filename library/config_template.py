# this is a virtual module that is entirely implemented server side

DOCUMENTATION = """
---
module: config_template
version_added: 2.0.0
short_description: >
  Renders template files providing a create/update override interface
description:
  - The module contains the template functionality with the ability to override
    items in config, in transit, though the use of an simple dictionary without
    having to write out various temp files on target machines. The module
    renders all of the potential jinja a user could provide in both the
    template file and in the override dictionary which is ideal for deployers
    whom may have lots of different configs using a similar code base.
  - The module is an extension of the **copy** module and all of attributes
    that can be set there are available to be set here.
options:
  src:
    description:
      - Path of a Jinja2 formatted template on the local server. This can be a
        relative or absolute path.
    required: true
    default: null
  dest:
    description:
      - Location to render the template to on the remote machine.
    required: true
    default: null
  config_overrides:
    description:
      - A dictionary used to update or override items within a configuration
        template. The dictionary data structure may be nested. If the target
        config file is an ini file the nested keys in the ``config_overrides``
        will be used as section headers.
  config_type:
    description:
      - A string value describing the target config type.
    choices:
      - ini
      - json
      - yaml
author: Kevin Carter
"""

EXAMPLES = """
  - name: run config template ini
    config_template:
      src: templates/test.ini.j2
      dest: /tmp/test.ini
      config_overrides: {}
      config_type: ini

  - name: run config template json
    config_template:
      src: templates/test.json.j2
      dest: /tmp/test.json
      config_overrides: {}
      config_type: json

  - name: run config template yaml
    config_template:
      src: templates/test.yaml.j2
      dest: /tmp/test.yaml
      config_overrides: {}
      config_type: yaml
"""
