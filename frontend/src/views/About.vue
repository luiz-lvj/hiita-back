<template>
  <div class="about loggedin">
    <h1>This is an about page</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
    };
  },
  async created() {
    const path = 'http://localhost:5000/HIITA/loggedin';

    const req = await fetch(path, {
      method: 'GET',
    });
    const res = await req.json();
    console.log(res);
  },
};
</script>
