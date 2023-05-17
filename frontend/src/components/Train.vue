<template>
  <div>
    <h1>{{train.TITULO}}</h1>
      <table class="exercisesListTable">
      <tr>
        <th>Ficha</th>
        <th>Descricao</th>
        <th>Escolher</th>
      </tr>
      <tr v-for="exercise in exercises" :key="exercise.ID" >
        <td>{{exercise.NOME_EXERCICIO}}</td>
        <td>{{exercise.DESCRICAO}}</td>
        <td><input type="checkbox"></td>
      </tr>
    </table>
    <button @click="$emit('closeTrain')"><i class="fas fa-times-circle-o">Close</i></button>
    <button @click="$emit('saveTrain')"><i class="fas fa-times-circle-o">Save</i></button>
  </div>
</template>

<script>
export default {
  props: {
    train: Object,
    exercises: Array,
  },
};
</script>

<style scoped>
h2 {
  color: white
}

.exercisesListTable {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

.exercisesListTable td, .exercisesListTable th {
  border: 1px solid #ddd;
  padding: 8px;
}

.exercisesListTable tr:nth-child(even){
  background-color: #f2f2f2;
  color: #2c3e50;
}

.exercisesListTable tr:hover {background-color: #ddd;}

.exercisesListTable th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
