<template>
  <v-row>
    <v-toolbar
        style="background-color: dodgerblue"
        class="d-flex align-content-center"
    >
      <v-col cols="2" v-for="item in menu" :key="item">
        <v-toolbar-title>
          <router-link class="menu" :to="item.link">
            {{ item.title }}
          </router-link>
        </v-toolbar-title>
      </v-col>
      <v-spacer></v-spacer>
      <v-col cols="1">
        <v-btn icon style="color: white">
          <v-icon>mdi-export</v-icon>
        </v-btn>
      </v-col>
    </v-toolbar>
  </v-row>

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
        title: 'Посмотреть доступную технику',
        link: ''
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
  color: white;
  text-decoration: none;

}
</style>