{% extends "base.tpl" %}
{% block body %}
<div class='row'>
  <div class='col-sm-4 col-sm-offset-4'>
    <form method='post'>
      <input name='username' placeholder='Username' class='form-control'>
      <input type='password' name='password' placeholder='Password'
        class='form-control'>
      <input type='submit' value='Login' class='form-control'>
    </form>
  </div>
</div>
{% endblock %}
