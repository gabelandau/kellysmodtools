<template>
  <div class="login-form">
    <div class="field">
      <div class="control has-icons-left text-input">
        <input class="input" type="text" placeholder="Username">
        <span class="icon is-small is-left">
          <i class="fas fa-user"></i>
        </span>
      </div>

      <div class="control has-icons-left text-input">
        <input class="input" type="password" placeholder="Password">
        <span class="icon is-small is-left">
          <i class="fas fa-lock"></i>
        </span>
      </div>
    </div>

    <div class="field is-grouped">
      <div class="control">
        <button class="button is-primary">Log in</button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.login-form {
  width: 500px;
  margin: 20px auto;

  .icon svg {
    color: #dbdee0;
  }

  .text-input {
    margin-top: 15px;
  }

  input[type="text"], input[type="password"] {
    background-color: #282f2f;
    border-color: rgb(140, 155, 157);
    color: #fff;
  }

  ::placeholder {
      color: #aaa;
      opacity: 1;
    }
}
</style>
