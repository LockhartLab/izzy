{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}

   .. rubric:: Methods

   {% block methods %}
   {% for item in methods %}
   .. automethod:: {{ item }}
   {%- endfor %}
   {% endblock %}




