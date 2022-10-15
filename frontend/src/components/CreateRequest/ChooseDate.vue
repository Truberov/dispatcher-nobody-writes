<template>
  <div>
    <v-row style="margin-top: 3%">
      <v-col>
        <h2>Выберете дату</h2>
      </v-col>
    </v-row>
    <v-row style=" justify-content: center">
      <v-col cols="10">
        <v-calendar
            v-model="selected"
        locale="ru"
        ></v-calendar>
      </v-col>
    </v-row>
    <v-row style="margin-top: 3%">
      <v-col>
        <v-btn :disabled="!selected">
          Далее
        </v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "ChooseDate",
  data: () => ({
    selected: null
  })
}
</script>

<style scoped>

</style>