<template>
  <div>
    <form style="margin-top: 15%" class="login" @submit.prevent="login">
      <h1>Авторизация</h1>
      <v-row style="justify-content: center; margin-top: 2%">
        <v-col cols="2">
          <input style="border: solid 2px darkgray" required v-model="email" placeholder="Логин"/>
        </v-col>
      </v-row>
      <v-row style="justify-content: center;">
        <v-col cols="2">
          <input style="border: solid 2px darkgray" required v-model="password" type="password" placeholder="Пароль"/>
        </v-col>
      </v-row>
      <v-btn style="margin-top: 1%" type="submit">Войти</v-btn>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: ""
    }
  },
  methods: {
    login: function () {
      let username = this.email
      let password = this.password
      this.$store.dispatch('login', {username, password})
          .then(() => this.$router.push('/'))
          .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>

</style>