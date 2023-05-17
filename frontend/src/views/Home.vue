<template>
  <div class="home content">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h2>Home Page</h2>
    <p>Seja bem vindo {{this.name}}</p>
    <Message v-if="showMessage" :message=message :error=false />
    <Train :train="choosedTrain" :exercises="exercises" v-if="isTrainingVisible"
      @saveTrain="saveTrain" @closeTrain="closeTrain"/>
    <table class="trainheadertable">
      <tr>
        <th>Ficha</th>
        <th>Descricao</th>
        <th>Escolher</th>
      </tr>
      <TrainHeader v-for="ficha in fichas" :key="ficha.ID" :treino="ficha"
        @showTrain="showTrain"/>
    </table>
    <!-- Criar componente aqui de treinos Header disponiveis -->
    <!-- Usar props para passar informações de cada treino a serem mostradas -->
    <!-- No clique abre a pagina de treino refernte a aquele componente -->
  </div>
</template>

<script>
// @ is an alias to /src
import TrainHeader from '../components/TrainHeader.vue';
import Train from '../components/Train.vue';
import Message from '../components/Message.vue';

export default {
  name: 'Home',
  components: {
    TrainHeader,
    Train,
    Message,
  },
  data() {
    return {
      name: 'Neymar',
      fichas: [{ ID: '1', TITULO: 'peito', DESCRICAO: 'treino de peito' },
        { ID: '2', TITULO: 'costas', DESCRICAO: 'treino de costas' }],
      isTrainingVisible: false,
      choosedTrain: {},
      exercises: [],
      showMessage: false,
      message: '',
    };
  },
  async created() {
    const pathLoggedin = 'http://localhost:5000/HIITA/loggedin';

    const reqLoggedin = await fetch(pathLoggedin, {
      method: 'GET',
      headers: new Headers(),
    });

    const resLoggedin = await reqLoggedin.json();
    this.loggedin = resLoggedin.loggedin;
    this.name = resLoggedin.account.NOME;

    const pathFichas = 'http://localhost:5000/HIITA/fichas';
    const reqFichas = await fetch(pathFichas, {
      method: 'GET',
      headers: new Headers(),
    });

    const resFichas = await reqFichas.json();
    console.log(resFichas);
    this.fichas = resFichas.fichas;
  },
  methods: {
    async showTrain(tid) {
      this.isTrainingVisible = true;
      const trainId = tid;
      this.choosedTrain = this.fichas.find((el) => el.ID === trainId);

      this.exercises = [{ id: '1', title: 'supino', descricao: '3x10' },
        { id: '2', title: 'barra', descricao: '4x10' }];

      const path = 'http://localhost:5000/HIITA/treino';
      const dataJson = JSON.stringify({ trainID: trainId });

      const req = await fetch(path, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: dataJson,
      });

      const res = await req.json();
      console.log(res.exercises);
      this.exercises = res.exercises;
    },
    async saveTrain() {
      const path = 'http://localhost:5000/HIITA/salvar';
      const trainId = this.choosedTrain.ID;
      const dataJson = JSON.stringify({ trainID: trainId });

      await fetch(path, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: dataJson,
      });

      this.message = `Treino salvo ${this.choosedTrain.TITULO}`;
      this.isTrainingVisible = false;
      this.showMessage = true;
      this.choosedTrain = {};
      setTimeout(() => {
        this.showMessage = false;
        this.message = '';
      }, 3000);
    },
    closeTrain() {
      this.isTrainingVisible = false;
      this.choosedTrain = '';
    },
  },
};
</script>

<style scoped>
h2 {
  color: white
}

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

.trainheadertable tr:hover {background-color: #ddd;}

.trainheadertable th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
