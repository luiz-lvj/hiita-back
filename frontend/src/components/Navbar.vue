<template>
    <div>
        <nav class="navtop">
            <div>
                <h1>{{ alt }}</h1>
                <router-link to="/" id="logo-url">
                    <img :src="logo" :alt ="alt" id="logo" />
                </router-link>
                <router-link to="/"><i class="fas fa-home"></i>Home</router-link>
                <router-link to="/Profile"><i class="fas fa-user-circle"></i>Perfil</router-link>
                <a @click="logout" href="/"><i
                    class="fas fa-sign-out-alt"></i>Logout</a>
            </div>
        </nav>
    </div>
</template>

<script>
// import route from '../router';

export default {
  name: 'Navbar',
  props: ['logo', 'alt'],
  methods: {
    async logout() {
      const path = 'http://localhost:5000/HIITA/logout';

      await fetch(path, {
        method: 'GET',
      });
    },
  },
};
</script>

<style scoped>
#logo {
    width: 80px;
    height: 40px;
}
.navtop {
    background-color: whitesmoke;
    height: 60px;
    width: 100%;
    border: 0;
}
.navtop div {
    display: flex;
    margin: 0 auto;
    width: 1000px;
    height: 100%;
}
.navtop div h1, .navtop div a {
    display: inline-flex;
    align-items: center;
}
.navtop div h1 {
    flex: 1;
    font-size: 24px;
    padding: 0;
   margin: 0;
    color: #eaebed;
    font-weight: normal;
}
.navtop div a {
    padding: 0 20px;
    text-decoration: none;
    color: #c1c4c8;
    font-weight: bold;
}
.navtop div a i {
    padding: 2px 8px 0 0;
}
.navtop div a:hover {
    color: grey;
}
</style>
