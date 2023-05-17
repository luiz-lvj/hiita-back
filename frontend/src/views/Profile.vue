<template>
<div class="loggedin content">
  <h2>Perfil</h2>
  <div>
      <p>Detalhes pessoais:</p>
      <table>
          <tr>
              <td>CPF:</td>
              <td>{{ account['CPF'] }}</td>
          </tr>
          <tr>
              <td>Nome:</td>
              <td>{{ account['NOME'] }}</td>
          </tr>
          <tr>
              <td>Senha:</td>
              <td>{{ account['SENHA'] }}</td>
          </tr>
          <tr>
              <td>Email:</td>
              <td>{{ account['EMAIL'] }}</td>
          </tr>
      </table>
      <h1>Tabela de treinos realizados</h1>
    <table class="trainheadertable">
      <tr>
        <th>Data</th>
        <th>Hora</th>
        <th>Treino</th>
      </tr>
      <TrainExecuted v-for="(realizado, index) in realizados" :key="index" :treino="realizado"/>
    </table>
  </div>
  <!-- Colocar aqui componente com treinos realizados pelo usuário -->
</div>
</template>

<script>
import TrainExecuted from '../components/TrainExecuted.vue';

export default {
  components: { TrainExecuted },
  data() {
    return {
      account: {
        CPF: '1111',
        NOME: 'neymar',
        EMAIL: 'neymarjr@gmail.com',
        SENHA: 'hexa',
      },
      realizados: [{ DATA: '21/11/2022', HORA: '12:30', TITULO: 'Peito' },
        { DATA: '22/11/2022', HORA: '7:30', TITULO: 'costas' }],
    };
  },
  async created() {
    const path = 'http://localhost:5000/HIITA/loggedin';

    const req = await fetch(path, {
      method: 'GET',
      headers: new Headers(),
    });

    const res = await req.json();
    this.account = res.account;

    const pathRealizados = 'http://localhost:5000/HIITA/realizados';
    const reqRealizados = await fetch(pathRealizados, {
      method: 'GET',
      headers: new Headers(),
    });

    const resRealizados = await reqRealizados.json();
    this.realizados = resRealizados.realizeds;
  },
};
</script>

<style scoped>

.trainheadertable {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

.trainheadertable td, .trainheadertable th {
  border: 1px solid #ddd;
  padding: 8px;
}

.trainheadertable tr:nth-child(even){
  background-color: #f2f2f2;
  color: #2c3e50;
}

.trainheadertable tr:hover tr:nth-child(odd){background-color: #ddd;}

.trainheadertable th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
