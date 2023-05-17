<template>
    <div class="login_register">
      <h1 v-if="showLogin">Login</h1>
      <h1 v-else>Cadastro</h1>
      <div class="links">
        <a @click="showLogin=true" :class="{active: showLogin }">Login</a>
        <a @click="showLogin=false" :class="{active: !showLogin }">Cadastro</a>
      </div>
      <Login @updateLoggedin="updateLoggedin" v-if="showLogin" />
      <Register v-else />
    </div>
</template>

<script>
import Login from '@/components/Login.vue';
import Register from '@/components/Register.vue';

export default {
  components: {
    Login,
    Register,
  },
  data() {
    return {
      showLogin: true,
    };
  },
  methods: {
    updateLoggedin() {
      this.$emit('updateLoggedin');
    },
  },
};
</script>

<style scoped>
.login_register {
    width: 400px;
    background-color: #ffffff;
    box-shadow: 0 0 9px 0 rgba(0, 0, 0, 0.3);
    margin: 100px auto;
}

h1 {
    text-align: center;
    color: #5b6574;
    font-size: 24px;
    padding: 20px 0 20px 0;
    border-bottom: 1px solid #dee0e4;
}

.links {
    display: flex;
    padding: 0 15px;
}

.links a {
  color: #adb2ba;
  text-decoration: none;
  display: inline-flex;
  padding: 0 10px 10px 10px;
  font-weight: bold;
}

.links a:hover {
    color: #9da3ac;
}

.links a.active {
    border-bottom: 3px solid #3274d6;
    color: #3274d6;
}
</style>
