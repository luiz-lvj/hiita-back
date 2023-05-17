<template>
    <div>
        <LoginRegister @updateLoggedin="updateLoggedin" v-if="!loggedin" />
        <Home :username="username" :loggedin="loggedin" v-else />
    </div>
</template>

<script>
import LoginRegister from '@/views/LoginRegister.vue';
import Home from '@/views/Home.vue';

export default {
  components: {
    LoginRegister,
    Home,
  },
  data() {
    return {
      loggedin: false,
      username: 'neymar',
    };
  },
  async created() {
    const path = 'http://localhost:5000/HIITA/loggedin';

    const req = await fetch(path, {
      method: 'GET',
    });
    const res = await req.json();

    this.loggedin = res.loggedin;
    this.username = res.username;
  },
  methods: {
    updateLoggedin() {
      this.loggedin = true;
    },
  },
};
</script>
