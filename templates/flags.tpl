{% extends "base.tpl" %}
{% block body %}
<div class='row'>
  <div class='col-sm-4 col-sm-offset-4'>
    <h3>Flags</h3>
    <table>
    <tr><th>Name</th><th>Flag</th></tr>
    {% for f in flags %}
      <tr><td>{{f.name}}</td><td>{{f.value}}</td></tr>
    {% endfor %}
    </table>
  </div>
</div>
{% endblock %}
