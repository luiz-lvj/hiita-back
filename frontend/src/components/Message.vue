<template>
    <div class="message-container" :class="{error: error}">
        <h2>{{ message }}</h2>
    </div>
</template>

<script>
export default {
  name: 'Message',
  props: {
    message: String,
    error: Boolean,
  },
};
</script>

<style scoped>
.message-container {
    color: #004085;
    background-color: #CCE5FF;
    border: 2px solid #D8DAFF;
    border-radius: 5px;
    padding: 10px;
    max-width: 350px;
    margin: 30px auto;
}

.error {
    color: white;
    background-color: #f83b3b;
}
</style>
