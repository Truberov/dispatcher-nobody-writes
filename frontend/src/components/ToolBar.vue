<template>
  <v-toolbar
      color="blue"
      elevation="4"
      dense
  >
    <v-toolbar-title v-for="item in menu" :key="item">
      <router-link class="menu" :to="item.link">
        {{ item.title }}
      </router-link>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon>
      <v-icon>mdi-export</v-icon>
    </v-btn>
  </v-toolbar>
</template>

<script>

export default {
  name: 'ToolBar',

  data: () => ({
    menu: [
      {
        title: 'Создать заявку',
        link: ''
      },
      {
        title: 'Посмотреть доступную технику',
        link: ''
      },
      {
        title: 'История заявки',
        link: ''
      },
    ]
  })
}
</script>
<style scoped>
.menu{
  color: white;
  text-decoration: none;
}
</style>