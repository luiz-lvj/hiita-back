<template>
    <tr class="trainheader">
        <td>{{treino.TITULO}}</td>
        <td>{{treino.DESCRICAO}}</td>
        <td><button @click="$emit('showTrain', treino.ID)">
          <i class="fas fa-check"></i></button></td>
    </tr>
</template>

<script>
export default {
  props: {
    treino: Object,
  },
};
</script>

<style scoped>
.trainheader {
    background-color: #2c3e50;
    color: white;
}
</style>
