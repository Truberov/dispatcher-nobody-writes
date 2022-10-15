<template>
  <v-card
      style="background-color: dodgerblue"
      height="60px"
      elevation="4"
  >
    <v-row>
      <v-col cols="3" v-for="item in menu" :key="item">
        <router-link class="menu text-body-2" :to="item.link">
          {{ item.title }}
        </router-link>
      </v-col>
      <v-spacer></v-spacer>
      <v-col cols="3">
        <v-btn icon style="color: white">
          <v-icon>mdi-export</v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>

export default {
  name: 'ToolBar',

  data: () => ({
    menu: [
      {
        title: 'Создать заявку',
        link: '/'
      },
      {
        title: 'Просмотр транспорта',
        link: '/view_transport'
      },
      {
        title: 'История заявок',
        link: ''
      }
    ]
  })
}
</script>
<style scoped>
.menu {
  line-height: 45px;
  font-size: 1.2em;
  color: white;
  text-decoration: none;

}
</style>