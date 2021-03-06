{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}
.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/workflows/Tests/badge.svg?branch=master
     :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions?workflow=Tests
     :alt: CI Status

{{ cookiecutter.description }}

Installation
============
.. code-block:: console

   pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git

Usage
=====

CLI
---
.. code-block:: console

   {{ cookiecutter.project_slug }} --help

Module
------
.. code-block:: console

   python3 -m {{ cookiecutter.project_slug }} --help

License
=======
Copyright {% now 'utc', '%Y' %} {{ cookiecutter.full_name }}

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
