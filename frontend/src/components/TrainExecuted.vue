<template>
    <tr class="trainexecuted">
        <td>{{treino.DATA}}</td>
        <td>{{treino.HORA}}</td>
        <td>{{treino.TITULO}}</td>
    </tr>
</template>

<script>
export default {
  props: {
    treino: Object,
  },
};
</script>
