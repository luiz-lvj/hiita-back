<template>
    <div class="login">
        <Message v-if="showMessage" :message=message :error=error />
        <form @submit="login($event)" method="post">
            <label for="username">
                <i class="fas fa-user"></i>
            </label>
            <input type="text" name="username" placeholder="CPF"
                            id="username" required v-model="form.username">
            <label for="password">
                <i class="fas fa-lock"></i>
            </label>
            <input type="password" name="password" placeholder="Senha"
              id="password" required v-model="form.password">
            <input type="submit" value="Login">
        </form>
    </div>
</template>

<script>
import Message from '@/components/Message.vue';
// import router from '../router';

export default {
  name: 'Login',
  components: {
    Message,
  },
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
      message: '',
      error: true,
      showMessage: false,
    };
  },
  methods: {
    async messageCreation(res) {
      this.message = res.message;
      this.error = res.error;
      this.showMessage = true;
      setTimeout(() => {
        this.showMessage = false;
        this.message = '';
        this.error = false;
      }, 3000);
    },
    async login(e) {
      const path = 'http://localhost:5000/HIITA/login';
      e.preventDefault();
      const Form = this.form;
      const dataJson = JSON.stringify(Form);

      const req = await fetch(path, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: dataJson,
      });
      console.log(req);
      const res = await req.json();
      this.messageCreation(res);
      console.log(res);
      if (!res.error) {
        this.$emit('updateLoggedin');
      }
    },
  },
};
</script>

<style scoped>
form {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding-top: 20px;
}

form label {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 50px;
    height: 50px;
    background-color: #3274d6;
    color: #ffffff;
}

form input[type="password"], form input[type="email"], form input[type="text"] {
    width: 310px;
    height: 50px;
    border: 1px solid #dee0e4;
    margin-bottom: 20px;
    padding: 0 15px;
}

form input[type="submit"] {
    width: 100%;
    padding: 15px;
    margin-top: 20px;
    background-color: #3274d6;
    border: 0;
    cursor: pointer;
    font-weight: bold;
    color: #ffffff;
    transition: background-color 0.2s;
}

form input[type="submit"]:hover {
    background-color: #2868c7;
    transition: background-color 0.2s;
}
</style>
