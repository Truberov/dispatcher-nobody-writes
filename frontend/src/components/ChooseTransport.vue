<template>
  <v-row class="mt-10 justify-center">
    <h2>Выберете транспорт</h2>
  </v-row>
  <v-row class="mt-10 mb-10 justify-space-around">
    <v-col class="item" cols="3" v-for="item in transport" :key="item" @click="select(item)">
      <v-list-item :class="{'selected' : selected && selected.type === item.type}">
        <v-img max-height="250" :src="item.img"></v-img>
        <h3>{{ item.name }}</h3>
      </v-list-item>
    </v-col>
  </v-row>
  <v-row class="mt-10 justify-center" @click="next">
    <v-btn color="blue" :disabled="!selected">
      Далее
    </v-btn>
  </v-row>
</template>

<script>
export default {
  name: "CreateRequest",

  data: () => ({
    transport: [
      {
        img: require('@/assets/aerialplatform.png'),
        name: 'Автовышка',
        type: 'aerialplatform'
      },
      {
        img: require('@/assets/loader.png'),
        name: 'Погрузчик',
        type: 'loader'
      },
      {
        img: require('@/assets/truckcrane.png'),
        name: 'Кран',
        type: 'truckcrane'
      }
    ],
    selected: null,
    isSelected: false
  }),
  methods: {
    select(item) {
      this.selected = item
    },
    next() {
      this.$emit('choosed-transport')
    }
  }
}
</script>

<style scoped lang="scss">
.fade-enter-active, .fade-leave-active {
  transition: all .4s;
}

.fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */
{
  position: absolute;
  opacity: 0;
}

.item {
  cursor: pointer;
  transform: scale(1);
  transition: all 0.3s;
}

.item:hover {
  background: rgba(217, 217, 217, 0.5);
  border-radius: 10px;
  transition: all 0.3s;
  transform: scale(1.1);
}

.selected {
  border-radius: 10px;
  transform: scale(1.05);
  background: rgba(217, 217, 217, 0.5);
  transition: all 0.3s;
}
</style>