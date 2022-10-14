<template>
  <v-row class="mt-10 justify-center">
    <h2>Выберете дату</h2>
  </v-row>
  <v-row class="justify-center mt-10">
    <v-col cols="8">
      <DatePicker v-model="selected" locale="ru" is-expanded/>
    </v-col>
  </v-row>
  <v-row>
    <v-col>
      <v-btn class="mt-10" color="blue" :disabled="selected === null">
        Далее
      </v-btn>
    </v-col>
  </v-row>
</template>

<script>
import 'v-calendar/dist/style.css';
import { DatePicker } from 'v-calendar';

export default {
  name: "ChooseDate",
  components: {
    DatePicker,
  },
  data: ()=> ({
    selected: null
  })
}
</script>

<style scoped>

</style>