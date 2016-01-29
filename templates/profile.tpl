{% extends "base.tpl" %}
{% block body %}
<div class='row'>
<div class='col-sm-4 col-sm-offset-4'>
<form method='post'>
  <div class='well'>
    <h6>Change Password</h6>
    <div class='input-group'>
      <input type='password' name='old' placeholder='Old Password'>
    </div>
    <div class='input-group'>
      <input type='password' name='new' placeholder='New Password'>
    </div>
    <div class='input-group'>
      <input type='password' name='new2' placeholder='Repeat New'>
    </div>
  </div>
  <div class='well'>
    <h6>GnuPG Key</h6>
    <p>Use this to upload a key to receive encrypted eMail.</p>
    <div class='input-group'>
      <input name='url' placeholder='URL to Key'>
    </div>
    <div class='input-group'>
      <textarea class='disabled' disabled>
        {{- user.gpg_key|e -}}
      </textarea>
    </div>
  </div>
  <div class='input-group'>
    <input type='submit' value='Save' class='btn btn-primary'>
  </div>
</form>
</div>
</div>
{% endblock %}
